#!/usr/bin/env python3
"""Build coverage and reading queues. Keyword hits NEVER decide inclusion/exclusion."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
from lxml import html
from harvest_catalogs import clean, write_json, write_jsonl

PQC=re.compile(r'\b(?:kyber|dilithium|falcon|sphincs\+?|mceliece|bike|hqc|ntru|saber|frodokem|sike|sidh|sqisign|haetae)\b|ML[- ]?(?:KEM|DSA)|SLH[- ]?DSA|post[- ]quantum|lattice[- ]based|\bNTT\b|number[- ]theoretic|isogen|\bLWE\b|\bRLWE\b|\bMLWE\b',re.I)
SCA=re.compile(r'side[- ]?channels?|leakage|\bmask(?:ed|ing)\b|probing|constant[- ]time|timing|power analysis|electromagnetic|\bSASCA\b|\bDPA\b|\bCPA\b|\bSIFA\b|hamming|cache|speculat|transient execution|cold boot|rowhammer|microarchitectur|shuffling|plaintext[- ]checking|template attack',re.I)

def md(s): return str(s).replace('|','\\|').replace('\n',' ')

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--cache',type=Path,required=True)
    p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    args=p.parse_args();root=args.root
    catalogs=[]
    for path in sorted((root/'catalogs').glob('*.jsonl')):
        catalogs.extend(json.loads(line) for line in path.read_text().splitlines() if line)
    abstracts={}
    for path in args.cache.glob('*.abstracts.json'):
        abstracts.update(json.loads(path.read_text()))
    for path in args.cache.glob('tches-crossref-page*.raw'):
        for item in json.loads(path.read_bytes())['message']['items']:
            raw=item.get('abstract')
            if raw:
                abstracts['doi:'+item['DOI'].lower()]=clean(html.fromstring(raw).text_content())
    decisions_path=root/'screening/decisions.jsonl'
    decisions={r['id']:r for r in (json.loads(x) for x in decisions_path.read_text().splitlines())} if decisions_path.exists() else {}
    queue=[]
    for record in catalogs:
        title=record['title'];abstract=abstracts.get(record['id'],'')
        combined=title+' '+abstract
        pqc=PQC.search(combined);sca=SCA.search(combined)
        priority='pqc_and_sca_terms' if pqc and sca else 'pqc_terms' if pqc else 'sca_terms' if sca else 'unmatched_pending'
        matches={}
        for field,text in [('title',title),('abstract',abstract)]:
            matches[field]={'pqc':sorted(set(m.group().lower() for m in PQC.finditer(text))),
                            'sca':sorted(set(m.group().lower() for m in SCA.finditer(text)))}
        queue.append({'id':record['id'],'venue':record['venue'],'venue_year':record['venue_year'],
                      'title':title,'url':record['url'],'priority':priority,'keyword_matches':matches,
                      'screening_status':decisions.get(record['id'],{}).get('decision','pending'),
                      'abstract_available_locally':bool(abstract),'automatically_excluded':False})
    write_jsonl(root/'screening/reading-queue.jsonl',queue)
    write_json(args.cache/'abstract-index.json',abstracts)
    pqcqueue=[r for r in queue if r['priority'].startswith('pqc')]
    lines=['# 后量子相关候选阅读队列','','状态：自动安排阅读顺序，**不是全部已经纳入的论文清单**。标题或摘要命中关键词可能是假阳性；未命中条目仍保留待筛查。','',
           f'当前目录记录 {len(catalogs)} 条，其中 {len(pqcqueue)} 条命中后量子相关关键词。','',
           '| 年份/会议 | 候选论文 | 阅读判定 |','|---|---|---|']
    for r in sorted(pqcqueue,key=lambda x:(-x['venue_year'],x['venue'],x['title'].casefold())):
        lines.append(f"| {r['venue_year']} {r['venue']} | [{md(r['title'])}]({r['url']}) | {r['screening_status']} |")
    (root/'PQC_QUEUE.md').write_text('\n'.join(lines)+'\n')
    counts=Counter((r['venue'],r['venue_year']) for r in catalogs)
    cells=[];lines=['# 目录覆盖与未完成工作','','更新：2026-11-12。目录记录数不是相关论文数，也不是版本去重后的论文数。',
       '“已提取”只说明已从指定来源解析记录；独立目录核对、逐条主题筛查、全文阅读和引用追踪另行判定。','',
       '| 会议/卷 | 年份 | 已提取记录 | 交叉核对 | 主题筛查 | 来源与数量证据 |','|---|---:|---:|---|---|---|']
    for venue in ['TCHES','SP','USENIX','CCS','NDSS']:
        for year in range(2021,2027):
            n=counts.get((venue,year),0)
            filename='tches' if venue=='TCHES' else venue.lower()+'-'+str(year)
            provpath=root/'provenance'/f'{filename}.json'
            prov=json.loads(provpath.read_text()) if provpath.exists() else {}
            reviewed=sum(1 for r in queue if r['venue']==venue and r['venue_year']==year and r['screening_status']!='pending')
            cell={'venue':venue,'year':year,'catalog_records':n,'catalog_parsed':n>0,
                  'provenance_file':f'provenance/{filename}.json' if prov else None,
                  'independent_toc_crosscheck':'pending','screened_records':reviewed,
                  'citation_chasing':'pending','complete':False}
            cells.append(cell)
            link=f'[记录](provenance/{filename}.json)' if prov else '待取得'
            lines.append(f'| {venue} | {year} | {n if n else "待补齐"} | 待核对 | {reviewed}/{n} | {link} |')
    lines.extend(['','## 当前已知缺口','',
      '- 全部核心目录仍需与独立出版目录/正式论文集核对；同一个来源的 JSON 与 HTML 不算独立证据。',
      '- IEEE S&P 2026 页面标题与目录年度为 2026，但有一个 cycle 小标题写 2025，保留为需复核的页面不一致。',
      '- CCS 2026 为截至截点的官方录用目录；会议尚未举行，不能统一标为已正式发表。',
      '- Crossref 的 ISBN 查询只返回 CCS 论文集容器，不能用于证明其中没有论文；已改用官方网站目录。',
      '- TCHES 按卷年与出版日期分别处理，回看 2020 年元数据以补齐 2021 卷首期。Crossref 未提交引用列表不等于没有引用。',
      '- CRYPTO/EUROCRYPT/ASIACRYPT、PQCrypto、COSADE、HOST 等扩展来源仍待系统补齐。',
      '- 标题/摘要筛查、正式条目、版本归并与前后向引用追踪尚未完成。',
      '- 当前统计只针对已收集目录；未取得的目录、没有摘要的条目和日期不明记录均不视为完成。'])
    (root/'COVERAGE.md').write_text('\n'.join(lines)+'\n')
    write_json(root/'coverage.json',{'cutoff':'2026-11-12','rolling_window_start':'2021-11-12',
               'total_catalog_records':len(catalogs),'priority_counts':dict(Counter(r['priority'] for r in queue)),
               'core_cells':cells,'goal_complete':False})
    print(json.dumps({'catalog_records':len(catalogs),'pqc_queue':len(pqcqueue),
                      'abstracts_local':len(abstracts),'parsed_cells':sum(c['catalog_parsed'] for c in cells),
                      'completed_cells':0,'screened':len(decisions)},ensure_ascii=False))

if __name__=='__main__':main()
