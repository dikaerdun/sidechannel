#!/usr/bin/env python3
"""Build coverage and reading queues. Keyword hits NEVER decide inclusion/exclusion."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
from lxml import html
from harvest_catalogs import clean, write_json, write_jsonl

CORE_VENUES={'TCHES','SP','USENIX','CCS','NDSS'}

PQC=re.compile(r'\b(?:kyber|dilithium|falcon|sphincs\+?|mceliece|bike|hqc|ntru|nttru|saber|frodokem|sike|sidh|sqisign|haetae|picnic\d*|hawk|uov|rainbow|rollo|scabbard|raccoon|mayo|mqom|faest|perk|sdith|mirith|mpcith|voleith|ctidh|dctidh|csidh|xmss)\b|(?-i:\bCROSS\b|\bLESS\b)|MPC[- ]in[- ]the[- ]head|ML[- ]?(?:KEM|DSA)|SLH[- ]?DSA|post[- ]quantum|lattice[- ]based|\bNTT\b|number[- ]theoretic|isogen|\bLWE\b|\bRLWE\b|\bMLWE\b',re.I)
SCA=re.compile(r'side[- ]?channels?|leakage|\bmask(?:ed|ing)\b|probing|constant[- ]time|timing|power analysis|electromagnetic|\bSASCA\b|\bDPA\b|\bCPA\b|\bSIFA\b|hamming|cache|speculat|transient execution|cold boot|rowhammer|microarchitectur|shuffling|plaintext[- ]checking|template attack',re.I)

def md(s): return str(s).replace('|','\\|').replace('\n',' ')

def render_papers(root):
    papers=[json.loads(x) for x in (root/'papers.jsonl').read_text().splitlines() if x]
    lines=['# 已阅读论文卡片','','状态：持续整理，尚未覆盖全部相关论文。按每篇实际阅读层级报告；作者报告不等于本地复现。','',
           f'当前 {len(papers)} 篇；按 DOI 或官方页面关联目录，边界论文继续保留。','']
    for p in sorted(papers,key=lambda x:(x['venue_year'],x['venue'],x['title'])):
        lines += ['## '+p['title'],'',f"- 来源：[{p['venue']} {p['venue_year']}]({p['url']})；时间标记：{p['rolling_window_status']}。",
          '- 作者：'+('; '.join(p['authors']) if p.get('authors') else p.get('authors_display','未知')),
          '- 对象：'+', '.join(p['algorithms'])+'；类型：'+p['contribution_type']+'。',
          '- 核心想法：'+p['summary_zh'],'- 作者报告：'+p['author_report_zh'],
          '- 限制与下一步：'+p['limits_zh'],
          '- 阅读层级：'+p['reading_level']+'；来源：'+p['reading_source']+'。']
        if p.get('reading_sections'):lines.append('- 已读章节：'+p['reading_sections'])
        if p.get('detailed_note'):lines.append(f"- [详细阅读记录]({p['detailed_note']})")
        lines += ['- 代码/数据核查：'+p['code_artifact_status']+'；引用追踪：'+p['citation_chasing_status']+'。','']
    (root/'PAPER_NOTES.md').write_text('\n'.join(lines).rstrip()+'\n')
    topics={}
    for p in papers:
        for tag in p['algorithms']:topics.setdefault(tag,[]).append(p)
    tlines=['# 已纳入论文的对象索引','','只索引已经阅读并纳入的条目；同一论文可以列在多个标签下，标签数不可相加当作论文数。历史算法名与最终标准名不自动视为实现等价。',
            '[阅读卡片与限制](PAPER_NOTES.md) · [尚待阅读的 PQC 候选](PQC_QUEUE.md)','']
    for tag,group in sorted(topics.items(),key=lambda x:x[0].casefold()):
        tlines+=['## '+tag,'']
        for p in sorted(group,key=lambda p:(p['venue_year'],p['title'])):
            tlines.append(f"- {p['venue_year']} {p['venue']} · [{md(p['title'])}]({p['url']}) · {p['contribution_type']} · {p['reading_level']}")
        tlines.append('')
    (root/'TOPIC_INDEX.md').write_text('\n'.join(tlines))
    ylines=['# 已纳入论文的年度索引','','按会议/卷年分组；发表日期与预印本日期请查论文卡片。仅含已阅读纳入条目，不是该年全部相关研究。','']
    for year in sorted({p['venue_year'] for p in papers},reverse=True):
        ylines+=['## '+str(year),'','| 来源 | 论文 | 阅读层级 |','|---|---|---|']
        for p in sorted((p for p in papers if p['venue_year']==year),key=lambda p:(p['venue'],p['title'])):
            ylines.append(f"| {p['venue']} | [{md(p['title'])}]({p['url']}) | {p['reading_level']} |")
        ylines.append('')
    (root/'YEAR_INDEX.md').write_text('\n'.join(ylines))
    return papers

def render_citations(root,catalogs):
    catalog={r['id']:r for r in catalogs}
    edges=[json.loads(x) for x in (root/'citations/edges.jsonl').read_text().splitlines() if x]
    tasks=[json.loads(x) for x in (root/'citations/queue.jsonl').read_text().splitlines() if x]
    discoveries=[json.loads(x) for x in (root/'citations/discoveries.jsonl').read_text().splitlines() if x]
    citations=[e for e in edges if e['type']=='cites'];versions=[e for e in edges if e['type'] in {'preprint_of','version_of','author_revision_of'}]
    lines=['# 引用与版本追踪进度','',
      f'已核对 {len(citations)} 条引用关系、{len(versions)} 条版本关系；它们不等于被引论文已全部读完。',
      f'追踪任务共 {len(tasks)} 项：'+', '.join(f'{k}={v}' for k,v in sorted(Counter(t['status'] for t in tasks).items()))+'。',
      f'另有 {len(discoveries)} 条引用发现等待原始来源身份/范围核查。','',
      '本批逐条阅读 GoFetch 参考文献 [1]–[98]，其中已解析关系见下表。其余条目分为新发现、基础研究或实现背景；这不代表前后向追踪已经完成。',
      '[98 条参考文献初筛](citations/gofetch-reference-screen.jsonl) · [待核查发现](citations/discoveries.jsonl) · [全部任务](citations/queue.jsonl)','',
      '| 引用论文 | 引用号 | 已核对目标 | 目标阅读状态 |','|---|---:|---|---|']
    papers={p['id']:p for p in (json.loads(x) for x in (root/'papers.jsonl').read_text().splitlines())}
    for e in sorted(citations,key=lambda x:(x['from'],x['reference_number'])):
        r=catalog[e['to']]
        seed=catalog[e['from']]
        lines.append(f"| [{md(seed['title'])}]({seed['url']}) | {e['reference_number']} | [{md(r['title'])}]({r['url']}) | {papers.get(r['id'],{}).get('reading_level','catalog only; abstract pending')} |")
    lines+=['','## 版本关系','','| 电子稿 | 目录中的正式记录 | 关系与边界 |','|---|---|---|']
    for e in versions:
        r=catalog[e['to']]
        lines.append(f"| [来源]({e['from']}) | [{md(r['title'])}]({r['url']}) | {e['type']}; {md(e['status'])} |")
    lines+=['','## 本批纠正与未完成项','',
      '- GoFetch [89] 指向 S&P 2023 的 DVFS 论文：主列表漏列、另一官方日程有收录。已补条目并保留来源差异；独立论文集全量核对仍未完成。',
      '- GoFetch [58] 对应 SAC 2022 论文，但正式章节 2024 年上线；ePrint 与正式版作者顺序不同。书目关系已确认，全文差异未核对。',
      '- GoFetch [61] 的 Raccoon 是 TLS-DH(E) 攻击，不是同名后量子签名。',
      '- HOST 2021 采样论文的 ePrint 上传于 2022 年；会议年、出版日期和预印本日期分别保留。',
      '- 前向关系只记录当前实际看到的引用，不等于枚举了所有后续论文。扩展会议的系统目录、未解析引用及基础文献筛查继续进行。','']
    (root/'CITATION_PROGRESS.md').write_text('\n'.join(lines))
    return {'verified_citation_edges':len(citations),'verified_version_edges':len(versions),
            'task_status_counts':dict(Counter(t['status'] for t in tasks)),'unresolved_discoveries':len(discoveries)}

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
    abstracts={k:v for k,v in abstracts.items() if v.strip().lower() not in {'','not available','n/a','none','no abstract available'}}
    decisions_path=root/'screening/decisions.jsonl'
    decisions={r['id']:r for r in (json.loads(x) for x in decisions_path.read_text().splitlines())} if decisions_path.exists() else {}
    title_path=root/'screening/title-decisions.jsonl'
    titles={r['id']:r for r in map(json.loads,title_path.read_text().splitlines())} if title_path.exists() else {}
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
                      'title_screening_status':titles.get(record['id'],{}).get('decision','pending'),
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
       '| 会议/卷 | 年份 | 已提取记录 | 交叉核对 | 标题初筛 | 摘要及以上判定 | 来源与数量证据 |','|---|---:|---:|---|---|---|---|']
    for venue in ['TCHES','SP','USENIX','CCS','NDSS']:
        for year in range(2021,2027):
            n=counts.get((venue,year),0)
            filename='tches' if venue=='TCHES' else venue.lower()+'-'+str(year)
            provpath=root/'provenance'/f'{filename}.json'
            prov=json.loads(provpath.read_text()) if provpath.exists() else {}
            reviewed=sum(1 for r in queue if r['venue']==venue and r['venue_year']==year and r['screening_status']!='pending')
            title_reviewed=sum(1 for r in queue if r['venue']==venue and r['venue_year']==year and r['title_screening_status']!='pending')
            cell={'venue':venue,'year':year,'catalog_records':n,'catalog_parsed':n>0,
                  'provenance_file':f'provenance/{filename}.json' if prov else None,
                  'independent_toc_crosscheck':'pending','screened_records':reviewed,
                  'title_screened_records':title_reviewed,'abstract_screened_records':reviewed,
                  'citation_chasing':'pending','complete':False}
            cells.append(cell)
            link=f'[记录](provenance/{filename}.json)' if prov else '待取得'
            lines.append(f'| {venue} | {year} | {n if n else "待补齐"} | 待核对 | {title_reviewed}/{n} | {reviewed}/{n} | {link} |')
    lines.extend(['','## 当前已知缺口','',
      '- 全部核心目录仍需与独立出版目录/正式论文集核对；同一个来源的 JSON 与 HTML 不算独立证据。',
      '- IEEE S&P 2026 页面标题与目录年度为 2026，但有一个 cycle 小标题写 2025，保留为需复核的页面不一致。',
      '- IEEE S&P 2023 主列表漏列 DVFS Frequently Leaks Secrets；GoFetch 引用与另一官方日程促成补录。两份官方页面的对照不替代独立论文集全量审计。',
      '- CCS 2026 为截至截点的官方录用目录；会议尚未举行，不能统一标为已正式发表。',
      '- Crossref 的 ISBN 查询只返回 CCS 论文集容器，不能用于证明其中没有论文；已改用官方网站目录。',
      '- TCHES 按卷年与出版日期分别处理，回看 2020 年元数据以补齐 2021 卷首期。Crossref 未提交引用列表不等于没有引用。',
      '- TCHES 已逐题初筛完整标题及可用副标题；标题暂判不是最终纳入/排除。卷首前言另存于 catalog-exclusions/tches.jsonl。',
      '- 摘要占位文本 Not Available 不计为可读摘要；标题层的相邻/范围外条目仍可被后续摘要或引用证据修订。',
      '- CRYPTO/EUROCRYPT/ASIACRYPT、PQCrypto、COSADE、HOST 等扩展来源仍待系统补齐；引用扩展取得少量条目不等于补齐会议年度目录。',
      '- 标题/摘要筛查、正式条目、版本归并与前后向引用追踪尚未完成。',
      '- 当前统计只针对已收集目录；未取得的目录、没有摘要的条目和日期不明记录均不视为完成。'])
    (root/'COVERAGE.md').write_text('\n'.join(lines)+'\n')
    papers=render_papers(root)
    citation_progress=render_citations(root,catalogs)
    extended=[r for r in catalogs if r['venue'] not in CORE_VENUES]
    elines=['# 引用扩展来源','','这里只统计引用追踪实际取得的条目，**不是扩展会议的完整目录**。它们与核心会议共用 papers.jsonl、阅读队列和引用关系。','',
            '| 会议/来源 | 年份 | 已取得条目 | 完整目录与独立核对 |','|---|---:|---:|---|']
    for (v,y),n in sorted(Counter((r['venue'],r['venue_year']) for r in extended).items()):
        elines.append(f'| {v} | {y} | {n} | 未完成；仅引用扩展 |')
    elines+=['','SAC 2022 的会议年与 2024 年上线日期分别记录；ICCD 2021-10 论文作为年度边界补充保留。未取得的扩展会议（包括 CRYPTO、EUROCRYPT、ASIACRYPT、COSADE）仍有系统收集任务。',
             '[元数据](catalogs/citation-expansion.jsonl) · [来源与哈希](provenance/citation-expansion.json) · [未解析引用发现](citations/discoveries.jsonl)','']
    (root/'EXTENDED_SOURCES.md').write_text('\n'.join(elines))
    title_lines=['# 标题与副标题初筛','','这是一轮人工阅读后的 Codex 判定，不是关键词自动分类。全部判定均为标题层暂判；后续摘要判定见 decisions.jsonl。','',
                 f'当前 {len(titles)} 条：'+', '.join(f'{k}={v}' for k,v in sorted(Counter(r['decision'] for r in titles.values()).items()))+'。',
                 'candidate=侧信道候选；adjacent=相邻主题；outside_title_scope=标题层范围外暂判；uncertain=标题不足以判定。没有因此删除任何研究论文目录条目。','',
                 '| 年/会议 | 论文 | 暂判 | 主题提示 |','|---|---|---|---|']
    urls={r['id']:r['url'] for r in catalogs}
    for r in sorted(titles.values(),key=lambda x:(x['venue_year'],x['venue'],x['title'])):
        title_lines.append(f"| {r['venue_year']} {r['venue']} | [{md(r['title'])}]({urls[r['id']]}) | {r['decision']} | {r['topic_hint']} |")
    title_lines += ['','逐条依据、阅读来源与是否独立复核见 [title-decisions.jsonl](screening/title-decisions.jsonl)。','']
    (root/'TITLE_SCREENING.md').write_text('\n'.join(title_lines))
    write_json(root/'coverage.json',{'cutoff':'2026-11-12','rolling_window_start':'2021-11-12',
               'total_catalog_records':len(catalogs),'priority_counts':dict(Counter(r['priority'] for r in queue)),
               'core_catalog_records':sum(counts[c['venue'],c['year']] for c in cells),'citation_expansion_records':len(extended),
               'title_screened_records':len(titles),'abstract_screened_records':len(decisions),
               'included_papers':len(papers),'reading_level_counts':dict(Counter(p['reading_level'] for p in papers)),
               'citation_progress':citation_progress,'core_cells':cells,'goal_complete':False})
    print(json.dumps({'catalog_records':len(catalogs),'pqc_queue':len(pqcqueue),
                      'abstracts_local':len(abstracts),'parsed_cells':sum(c['catalog_parsed'] for c in cells),
                      'completed_cells':0,'title_screened':len(titles),'screened':len(decisions),'included_papers':len(papers)},ensure_ascii=False))

if __name__=='__main__':main()
