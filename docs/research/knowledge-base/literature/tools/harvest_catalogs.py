#!/usr/bin/env python3
"""Harvest bibliography metadata, retaining every catalog entry for later screening.

Raw pages and abstracts stay in --cache, outside the published library. Dependencies:
requests and lxml. A retrieved catalog is NOT a completed subject review.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import hashlib
from html import unescape
import json
from pathlib import Path
import re
from urllib.parse import urlencode, urljoin
import warnings
warnings.filterwarnings('ignore', message='urllib3 v2 only supports OpenSSL')
import requests
from lxml import html, etree

CUTOFF = '2026-11-12'
CCS_PARENTS = {2021:'10.1145/3460120', 2022:'10.1145/3548606',
               2023:'10.1145/3576915', 2024:'10.1145/3658644',
               2025:'10.1145/3719027', 2026:'10.1145/3830454'}
UA = {'User-Agent':'SidechannelResearchBibliography/0.1 (public scholarly metadata)'}

def clean(s):
    return ' '.join(unescape(s or '').split())

def node_text(nodes):
    return clean(' '.join(n.text_content() for n in nodes))

def digest(data):
    return hashlib.sha256(data).hexdigest()

def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def write_jsonl(path, values):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(''.join(json.dumps(v,ensure_ascii=False,sort_keys=True)+'\n' for v in values),encoding='utf-8')

class Harvest:
    def __init__(self, cache, output):
        self.cache, self.output = cache, output
        cache.mkdir(parents=True, exist_ok=True)

    def get(self, key, url):
        raw, info = self.cache/(key+'.raw'), self.cache/(key+'.meta.json')
        meta = json.loads(info.read_text()) if info.exists() else {}
        if raw.exists() and meta.get('url') == url and meta.get('status') == 200:
            if digest(raw.read_bytes()) != meta.get('sha256'):
                raise ValueError('Cached response hash mismatch: '+key)
            meta['source_id']=key
            if 'retrieved_at' not in meta:
                meta['retrieved_at']=datetime.fromtimestamp(raw.stat().st_mtime,timezone.utc).isoformat()
                meta['retrieval_time_basis']='local cache creation timestamp'
                write_json(info,meta)
            return raw.read_bytes(), meta
        r=requests.get(url,headers=UA,timeout=45)
        raw.write_bytes(r.content)
        meta={'source_id':key,'url':url,'response_url':r.url,'status':r.status_code,
              'retrieved_at':datetime.now(timezone.utc).isoformat(),
              'sha256':digest(r.content),'bytes':len(r.content),
              'content_type':r.headers.get('content-type','')}
        write_json(info,meta)
        r.raise_for_status()
        if r.status_code != 200:
            raise ValueError('Unexpected non-200 success response; not treated as a catalog')
        return r.content,meta

    def crossref_list(self,key,base,params):
        params=dict(params,rows=1000,cursor='*')
        records, metas, seen = [], [], set()
        total = None
        for page in range(1,100):
            raw,meta=self.get(f'{key}-page{page}',base+'?'+urlencode(params))
            obj=json.loads(raw)['message']
            if total is None: total=int(obj['total-results'])
            if total != int(obj['total-results']): raise ValueError('Crossref result count changed during pagination')
            items=obj.get('items',[])
            for item in items:
                doi=item['DOI'].lower()
                if doi in seen: raise ValueError('Repeated DOI during pagination: '+doi)
                seen.add(doi)
                item['_source_id']=meta.get('source_id',key+'-page'+str(page))
                records.append(item)
            metas.append(dict(meta,reported_total=total,returned_items=len(items)))
            if len(records)==total: return records,metas,total
            if not items or not obj.get('next-cursor'): raise ValueError('Pagination ended before reported count')
            params['cursor']=obj['next-cursor']
        raise ValueError('Pagination safety limit reached')

    def normalize_crossref(self,item,venue,year):
        doi=item['DOI'].lower()
        dates={k:item[k]['date-parts'][0] for k in ['published','published-online','published-print','issued']
               if item.get(k,{}).get('date-parts')}
        return {'id':'doi:'+doi,'title':clean(' '.join(item.get('title',[]))),
                'authors':[clean(' '.join([a.get('given',''),a.get('family','')])) for a in item.get('author',[])],
                'venue':venue,'venue_year':year,'doi':doi,'url':'https://doi.org/'+doi,
                'publisher_url':item.get('resource',{}).get('primary',{}).get('URL'),
                'type':item.get('type'),'publication_dates':dates,'pages':item.get('page'),
                'container_title':item.get('container-title',[]),'source_ids':[item['_source_id']],
                'metadata_read_level':'catalog_metadata','abstract_available':bool(item.get('abstract')),
                'references_deposited':len(item.get('reference',[])),
                'screening_status':'pending','scientific_claims_verified':False}

    def tches(self):
        items,metas,total=self.crossref_list('tches-crossref','https://api.crossref.org/journals/2569-2925/works',
                  {'filter':'from-pub-date:2020-01-01,until-pub-date:'+CUTOFF})
        records=[]
        excluded=[]
        for item in items:
            m=re.search(r'tches\.v(\d{4})\.i(\d+)\.',item['DOI'],re.I)
            if not m:
                raise ValueError('Unrecognized TCHES DOI, inspect rather than silently omit: '+item['DOI'])
            year,issue=map(int,m.groups())
            if year<2021:
                excluded.append({'doi':item['DOI'],'reason':'volume before 2021; lookback only'})
                continue
            rec=self.normalize_crossref(item,'TCHES',year)
            rec['issue']=issue
            records.append(rec)
        write_jsonl(self.output/'catalogs/tches.jsonl',sorted(records,key=lambda r:(r['venue_year'],r['issue'],r['doi'])))
        write_json(self.output/'provenance/tches.json',{'sources':metas,'reported_total':total,
                   'parsed_total':len(items),'retained_total':len(records),'excluded':excluded,
                   'count_reconciled':len(items)==total,'external_toc_crosscheck':'pending',
                   'subject_screening':'pending','citation_chasing':'pending'})
        return {'venue':'TCHES','records':len(records),'source_total':total,'status':'catalog collected; review pending'}

    def ccs_metadata_probe(self,year):
        parent=CCS_PARENTS[year]
        raw,meta=self.get('ccs-parent-'+str(year),'https://api.crossref.org/works/'+parent)
        p=json.loads(raw)['message']
        title=' '.join(p.get('title',[]))
        if str(year) not in title or 'Computer and Communications Security' not in title:
            raise ValueError('CCS parent title/year mismatch: '+title)
        isbns=p.get('ISBN',[])
        if not isbns: raise ValueError('CCS parent has no ISBN')
        allitems={};sources=[meta];totals=[]
        for isbn in isbns:
            items,metas,total=self.crossref_list(f'ccs-{year}-{isbn}','https://api.crossref.org/works',{'filter':'isbn:'+isbn})
            sources.extend(metas);totals.append({'isbn':isbn,'reported':total,'parsed':len(items)})
            for item in items: allitems[item['DOI'].lower()]=item
        records=[];excluded=[]
        for item in allitems.values():
            doi=item['DOI'].lower()
            if doi==parent:
                excluded.append({'doi':doi,'reason':'proceedings container, not an individual paper'})
                continue
            if not doi.startswith(parent+'.'):
                raise ValueError('Unexpected DOI in ISBN result: '+doi)
            records.append(self.normalize_crossref(item,'CCS',year))
        if not records:
            raise ValueError('ISBN query only returned the container; not a paper catalog')
        write_jsonl(self.output/f'catalogs/ccs-{year}.jsonl',sorted(records,key=lambda r:r['title'].casefold()))
        write_json(self.output/f'provenance/ccs-{year}.json',{'sources':sources,'parent_doi':parent,'parent_title':title,
                   'isbn_counts':totals,'retained_total':len(records),'excluded':excluded,
                   'count_reconciled':all(t['reported']==t['parsed'] for t in totals),
                   'external_toc_crosscheck':'pending','subject_screening':'pending','citation_chasing':'pending',
                   'date_note':'2026 conference is 15–19 November; distinguish publicly listed/forthcoming records from published papers' if year==2026 else None})
        return {'venue':'CCS','year':year,'records':len(records),'status':'catalog collected; review pending'}

    def ccs(self,year):
        urls={2021:'https://www.sigsac.org/ccs/CCS2021/accepted-papers.html',
              2022:'https://www.sigsac.org/ccs/CCS2022/program/accepted-papers.html',
              2023:'https://www.sigsac.org/ccs/CCS2023/assets/data/accepted_papers.xml',
              2024:'https://www.sigsac.org/ccs/CCS2024/program/accepted-papers.html',
              2025:'https://www.sigsac.org/ccs/CCS2025/assets/accepted-papers.json',
              2026:'https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html'}
        key='ccs-official-'+str(year);raw,meta=self.get(key,urls[year])
        sources=[meta];records=[];abstracts={};counts={}
        if year==2025:
            data=json.loads(raw)
            for cycle,items in data.items():
                if not isinstance(items,list): raise ValueError('Unexpected CCS 2025 JSON section')
                counts[cycle]=len(items)
                for item in items:
                    rec={'title':clean(re.sub(r'^\(#\d+\)\s*','',item['title'])),
                         'source_title':item['title'],'url':item['url'],
                         'authors':[clean(a['name']) for a in item['authors']],
                         'cycle':cycle}
                    m=re.search(r'10\.1145/\d+\.\d+',rec['url'])
                    if m: rec.update(doi=m.group(),id='doi:'+m.group())
                    records.append(rec)
            selector='official JSON firstCycle + secondCycle'
        elif year==2023:
            xml=etree.fromstring(raw,etree.XMLParser(resolve_entities=False,no_network=True))
            ar,am=self.get('ccs-authors-2023','https://www.sigsac.org/ccs/CCS2023/assets/data/author_profiles.xml')
            authors_xml=etree.fromstring(ar,etree.XMLParser(resolve_entities=False,no_network=True));sources.append(am)
            amap={n.findtext('id'):clean(n.findtext('name')) for n in authors_xml.findall('.//author')}
            nodes=xml.findall('.//paper');counts['paper_nodes']=len(nodes)
            for node in nodes:
                aids=[a.strip() for a in (node.findtext('authors') or '').split(',') if a.strip()]
                if any(a not in amap for a in aids): raise ValueError('Unresolved author ID')
                pid=node.findtext('id')
                rec={'id':'catalog:ccs:2023:'+pid,'catalog_record_id':pid,
                     'title':clean(node.findtext('title')),'authors':[amap[a] for a in aids],
                     'url':'https://www.sigsac.org/ccs/CCS2023/program.html',
                     'source_keywords':clean(node.findtext('keywords')),'source_track':node.findtext('track')}
                if node.findtext('abstract'): abstracts[rec['id']]=clean(node.findtext('abstract'))
                records.append(rec)
            selector='official accepted_papers.xml paper nodes joined with public author_profiles.xml'
        else:
            d=html.fromstring(raw)
            if str(year) not in node_text(d.xpath('//title')): raise ValueError('CCS page year mismatch')
            if year==2021:
                nodes=d.xpath('//div[contains(concat(" ",normalize-space(@class)," ")," papers-item ")]')
                for node in nodes:
                    records.append({'title':node_text(node.xpath('.//b')),'authors_display':node_text(node.xpath('.//p')),'url':urls[year]})
                selector='div.papers-item title and author paragraph'
            else:
                nodes=d.xpath('//tr[td]')
                for node in nodes:
                    cells=node.xpath('./td')
                    if len(cells)!=2: raise ValueError('Unexpected CCS table row')
                    records.append({'title':clean(cells[0].text_content()),'authors_display':clean(' '.join(cells[1].itertext())),'url':urls[year]})
                selector='two-column title/author table, excluding header rows'
            counts['paper_nodes']=len(nodes)
        if not records or any(not r['title'] for r in records): raise ValueError('Empty CCS catalog/title')
        for ordinal,rec in enumerate(records,1):
            rec.setdefault('id','title:ccs:'+str(year)+':'+digest(rec['title'].casefold().encode())[:16])
            rec.update(venue='CCS',venue_year=year,source_ids=[key],catalog_ordinal=ordinal,
                       metadata_read_level='catalog_metadata',abstract_available=rec['id'] in abstracts,
                       screening_status='pending',scientific_claims_verified=False)
            if year==2026: rec['publication_status']='officially listed; conference forthcoming at cutoff'
        if len({r['id'] for r in records})!=len(records): raise ValueError('Duplicate CCS records require reconciliation')
        write_jsonl(self.output/f'catalogs/ccs-{year}.jsonl',sorted(records,key=lambda r:r['title'].casefold()))
        write_json(self.cache/f'ccs-{year}.abstracts.json',abstracts)
        write_json(self.output/f'provenance/ccs-{year}.json',{'sources':sources,'selector':selector,'section_counts':counts,
            'retained_total':len(records),'source_sections_reconciled':sum(counts.values())==len(records),
            'count_reconciled':False,'external_toc_crosscheck':'pending','subject_screening':'pending','citation_chasing':'pending',
            'warnings':['ISBN-only Crossref lookup was insufficient; official catalog used instead'],
            'date_note':'Conference 2026-11-15 to 2026-11-19, after cutoff' if year==2026 else None})
        return {'venue':'CCS','year':year,'records':len(records),'status':'official catalog parsed; review pending'}

    def html_catalog(self,venue,year):
        urls={'USENIX':f'https://www.usenix.org/conference/usenixsecurity{str(year)[-2:]}/technical-sessions',
              'NDSS':f'https://www.ndss-symposium.org/ndss{year}/accepted-papers/',
              'SP':f'https://www.ieee-security.org/TC/SP{year}/'+('program-papers.html' if year<=2023 else 'accepted-papers.html')}
        key=f'{venue.lower()}-{year}'
        raw,meta=self.get(key,urls[venue]);d=html.fromstring(raw)
        page_title=node_text(d.xpath('//title'))
        warnings=[];records=[];abstracts={};nonpapers=[]
        if str(year) not in page_title and str(year)[-2:] not in page_title:
            warnings.append('Page title does not confirm requested year')
        if venue=='USENIX':
            nodes=d.xpath('//article[contains(concat(" ",normalize-space(@class)," ")," node-paper ")]')
            for node in nodes:
                links=node.xpath('.//h2/a[contains(@href,"/presentation/")]')
                if not links: continue
                a=links[0];url=urljoin(meta.get('response_url',urls[venue]),a.get('href'))
                rec={'id':'url:'+url,'title':clean(a.text_content()),'url':url,
                     'authors_display':node_text(node.xpath('.//*[contains(@class,"field-name-field-paper-people-text")]'))}
                presented_by=node_text(node.xpath('.//*[contains(@class,"field-name-field-presented-by")]'))
                if not rec['authors_display'] and (presented_by or rec['title'].startswith('Panel: ')):
                    rec.update(presented_by=presented_by,source_ids=[key],
                               disposition='nonpaper_schedule_entry',
                               reason='Official presenter/speaker field instead of research-paper authors; invited/keynote/Enigma/panel entry')
                    nonpapers.append(rec)
                    continue
                abstract=node_text(node.xpath('.//*[contains(@class,"field-name-field-paper-description-long")]'))
                if abstract: abstracts[rec['id']]=abstract
                records.append(rec)
            selector='article.node-paper > h2 > presentation link'
            all_presentation_links={urljoin(urls[venue],x.get('href')) for x in d.xpath('//a[contains(@href,"/presentation/")]')}
            if all_presentation_links-{r['url'] for r in records+nonpapers}:
                warnings.append('Some presentation links are outside parsed paper nodes; reconcile separately')
        elif venue=='NDSS':
            nodes=d.xpath('//h2/a[contains(@href,"/ndss-paper/")]')
            for a in nodes:
                node=a.getparent().getparent();url=urljoin(urls[venue],a.get('href'))
                records.append({'id':'url:'+url,'title':clean(a.text_content()),'url':url,
                    'authors_display':node_text(node.xpath('.//*[contains(@class,"pt-cv-ctf-display_authors")]'))})
            selector='h2 > ndss-paper link'
            if d.xpath('//*[contains(@class,"pt-cv-pagination") or contains(@class,"pt-cv-loadmore")]'):
                warnings.append('Pagination/load-more markup present: inspect before claiming full source coverage')
        else:
            nodes=d.xpath('//div[contains(concat(" ",normalize-space(@class)," ")," list-group-item ")]')
            for node in nodes:
                titles=node.xpath('./b/a|./strong/a|./b[not(a)]|./strong[not(a)]')
                if not titles: continue
                title=node_text(titles[:1])
                if title in ['TBD','To Be Determined']:
                    nonpapers.append({'title':title,'url':urls[venue],'source_ids':[key],
                                      'disposition':'placeholder','reason':'Official page contains no paper title or authors for this placeholder'})
                    continue
                anchor=titles[0].get('href','').lstrip('#')
                url=urls[venue]+('#'+anchor if anchor else '')
                authors=node_text(node.xpath('.//*[contains(@class,"authorlist")]'))
                if not authors:
                    whole=clean(node.text_content())
                    authors=whole[len(title):].strip() if whole.startswith(title) else None
                records.append({'id':'title:sp:'+str(year)+':'+digest(title.casefold().encode())[:16],
                    'title':title,'url':url,'authors_display':authors})
            selector='div.list-group-item > bold title'
            headings=[clean(x.text_content()) for x in d.xpath('//h2|//h3')]
            if any(re.search(r'20\d\d',h) and str(year) not in h for h in headings):
                warnings.append('Cycle heading has another year; verify proceedings against official page')
        if not records: raise ValueError('Zero parsed papers; inspect layout, redirects, or access challenge')
        unique={}
        for rec in records:
            rec.update({'venue':venue,'venue_year':year,'source_ids':[key],
                        'metadata_read_level':'catalog_metadata','abstract_available':rec['id'] in abstracts,
                        'screening_status':'pending','scientific_claims_verified':False})
            if rec['id'] in unique and rec['title']!=unique[rec['id']]['title']:
                raise ValueError('Same identity with conflicting titles')
            unique[rec['id']]=rec
        write_jsonl(self.output/f'catalogs/{key}.jsonl',sorted(unique.values(),key=lambda r:r['title'].casefold()))
        if nonpapers: write_jsonl(self.output/f'catalog-exclusions/{key}.jsonl',nonpapers)
        write_json(self.cache/(key+'.abstracts.json'),abstracts)
        write_json(self.output/f'provenance/{key}.json',{'sources':[meta],'page_title':page_title,
                   'selector':selector,'matched_nodes':len(nodes),'parsed_records':len(records),
                   'retained_total':len(unique),'duplicate_occurrences':len(records)-len(unique),
                   'nonpaper_entries':len(nonpapers),
                   'reported_total':None,'count_reconciled':False,'warnings':warnings,
                   'external_toc_crosscheck':'pending','subject_screening':'pending','citation_chasing':'pending'})
        return {'venue':venue,'year':year,'records':len(unique),'warnings':warnings,
                'status':'catalog parsed; completeness and review pending'}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cache',type=Path,required=True)
    parser.add_argument('--output',type=Path,default=Path(__file__).resolve().parents[1])
    parser.add_argument('--venues',nargs='+',default=['TCHES','CCS','USENIX','NDSS','SP'])
    parser.add_argument('--years',nargs='+',type=int,default=list(range(2021,2027)))
    args=parser.parse_args();h=Harvest(args.cache,args.output)
    jobs=[];results=[]
    with ThreadPoolExecutor(max_workers=3) as pool:
        if 'TCHES' in args.venues: jobs.append(pool.submit(h.tches))
        for year in args.years:
            if 'CCS' in args.venues: jobs.append(pool.submit(h.ccs,year))
            for venue in ['USENIX','NDSS','SP']:
                if venue in args.venues: jobs.append(pool.submit(h.html_catalog,venue,year))
        for job in as_completed(jobs):
            try: result=job.result()
            except Exception as e: result={'status':'failed','error':str(e)}
            results.append(result);print(json.dumps(result,ensure_ascii=False),flush=True)
    write_json(args.cache/'harvest-last-run.json',results)

if __name__=='__main__': main()
