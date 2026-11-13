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
    pending_discoveries=[d for d in discoveries if d['status'].startswith('pending_')]
    resolved_discoveries=[d for d in discoveries if d['status']=='resolved_identity_and_scope']
    decisions={d['id']:d for d in (json.loads(x) for x in (root/'screening/decisions.jsonl').read_text().splitlines())}
    citations=[e for e in edges if e['type']=='cites'];versions=[e for e in edges if e['type'] in {'preprint_of','version_of','author_revision_of'}]
    inferred_versions=[e for e in versions if e.get('relation_confidence')=='primary_source_inference']
    lines=['# 引用与版本追踪进度','',
      f'已核对 {len(citations)} 条引用条目；版本关系共 {len(versions)} 条，其中 {len(versions)-len(inferred_versions)} 条书目核实、{len(inferred_versions)} 条为原始来源推定。它们不等于被引论文已全部读完。',
      f'追踪任务共 {len(tasks)} 项：'+', '.join(f'{k}={v}' for k,v in sorted(Counter(t['status'] for t in tasks).items()))+'。',
      f'已登记发现中，{len(resolved_discoveries)} 条完成身份与范围判定，{len(pending_discoveries)} 条仍待核查；已解析记录继续保留历史。','',
      'GoFetch 参考文献 [1]–[98] 与 Scheduled Disclosure [1]–[79] 已逐条初筛；OpenTitan、Peek-a-Walk、EasyCrypt、Episode V 及 S&P 2023 的指定引用继续保留。追加 GLP 期刊、Protecting Dilithium、3D-Shield 合计九条选读；所有选读均不构成完整参考文献筛查。',
      'SDitH 的 27 条、CiC FAEST 攻击的 38 条和 HQC 有效密文攻击的 30 条参考列表已逐条初筛，共 36 条对应、23 条新发现待核查、36 条暂列背景。背景条目未经原文最终排除，全部列表也不构成递归引用闭合。',
      '[SDitH 引用清单](citations/sdith2026-reference-screen.jsonl) · [CiC FAEST 引用清单](citations/faest-cic2026-reference-screen.jsonl) · [HQC 引用清单](citations/hqc-valid2025-reference-screen.jsonl) · [修订与证据范围](notes/mpcith-revisions-and-evidence-20261113.md)','',
      '[GoFetch 的 98 条初筛](citations/gofetch-reference-screen.jsonl) · [Scheduled Disclosure 的 79 条初筛](citations/scheduled-disclosure-reference-screen.jsonl) · [OpenTitan 单条选读](citations/opentitan-selected-reference-screen.jsonl) · [Peek-a-Walk 两条选读](citations/peek-walk-selected-reference-screen.jsonl) · [四篇 Kyber 来源](provenance/kyber-four-reference-followup-20261113.json) · [发现与解析历史](citations/discoveries.jsonl) · [全部任务](citations/queue.jsonl)','',
      '| 引用论文 | 引用号 | 已核对目标 | 目标阅读状态 |','|---|---:|---|---|']
    papers={p['id']:p for p in (json.loads(x) for x in (root/'papers.jsonl').read_text().splitlines())}
    for e in sorted(citations,key=lambda x:(x['from'],x['reference_number'])):
        r=catalog[e['to']]
        seed=catalog[e['from']]
        reading=papers.get(r['id'],{}).get('reading_level')
        if reading is None:
            decision=decisions.get(r['id'],{})
            reading=('abstract read; '+decision['decision']+' (see ADJACENT_NOTES)') if decision else 'catalog only; abstract pending'
        version=f"; actual cited version: [preprint]({e['cited_version_url']})" if e.get('cited_version_url') else ''
        if e.get('evidence_level')=='publisher_deposited_reference':
            reading += '; citation DOI from publisher metadata; full-text bibliography unread'
        lines.append(f"| [{md(seed['title'])}]({seed['url']}) | {e['reference_number']} | [{md(r['title'])}]({r['url']}) | {reading}{version} |")
    lines+=['','## 版本关系','','| 版本来源 | 目录中的关联记录 | 关系与边界 |','|---|---|---|']
    for e in versions:
        r=catalog[e['to']]
        lines.append(f"| [来源]({e['from']}) | [{md(r['title'])}]({r['url']}) | {e['type']}; {md(e['status'])} |")
    lines+=['','## 累积纠正与未完成项','',
      '- GoFetch [89] 指向 S&P 2023 的 DVFS 论文：主列表漏列、另一官方日程有收录。已补条目并保留来源差异；此前独立印刷目录 196 条对应也确认包含该篇。',
      '- GoFetch [58] 对应 SAC 2022 论文，但正式章节 2024 年上线；ePrint 与正式版作者顺序不同。书目关系已确认，全文差异未核对。',
      '- GoFetch [61] 的 Raccoon 是 TLS-DH(E) 攻击，不是同名后量子签名。',
      '- HOST 2021 采样论文的 ePrint 上传于 2022 年；会议年、出版日期和预印本日期分别保留。',
      '- GoFetch [26] 实际引用 2023 年 XPT/PrefetchX 预印本；与 HPCA 2024 条目的研究版本关联由相同作者及机制推定，仍待显式版本链接/全文对照。标题及定量结果不同，不声称全文等价。',
      '- GoFetch [71] 的 Flatter 已读摘要并归为格约简方法背景，见 [相邻主题记录](ADJACENT_NOTES.md)；未计作独立侧信道攻击。',
      '- Scheduled Disclosure 的密码实验对象为 SIKE-751；15 条引用已与目录对应，ASIACCS/DIMVA/ASPLOS 三条发现已读并解析。OpenTitan 的 Share-slicing 引用已补读摘要与讨论，作为窗口外基础文献保留；完整追踪仍未完成。',
      '- Peek-a-Walk 标题无 PQC 名称，正文包含参考 Dilithium-2 的 nonce 泄漏与格后处理；已对应 GoFetch 与 Too Many Hints 两条引用，其余参考文献尚待逐条筛查。',
      '- EasyCrypt S&P 2025 的 [11]、[12] 已对应 Episode IV、Episode V；后者补读恒时证明范围及 [八条选读引用](citations/kyber-v-selected-reference-screen.jsonl)，新增 CRYPTO 2020 与 CHES 2017 两篇窗口外基础卡片。ePrint 2025/1607 的 minor revision 与 2024/843 的 major revision 均有显式书目关系，全文差异尚未核对。见 [Episode V 范围记录](notes/kyber-verification-episode-v-20261113.md)。',
      '- S&P 2023 的 Raccoon 五条与 selSLH 四条选读均已对应，GLP、Protecting、3D-Shield 的九条选读继续保留。打乱论文全部 17 条引用现已对应并作范围判定，七条发现已解析；NIST 错误 DOI 已纠正。JCEN 后续两条实际引用及局部掩码的出版商提交引用分别记录，见 [完整种子引用清单](citations/kyber-shuffle-selected-reference-screen.jsonl)、[后续选读](citations/kyber-hardware-followup-selected-reference-screen.jsonl)与 [证据范围](notes/kyber-shuffle-followups-and-evidence-20261113.md)。这些关系不构成递归引用闭合。',
      '- 前向关系只记录当前实际看到的引用，不等于枚举了所有后续论文。扩展会议的系统目录、未解析引用及基础文献筛查继续进行。',
      '- FAEST 2025/1261 当前版撤回掩码实现，旧题名保留为被引版本；不能把 CiC 攻击自动认定为撤回原因。Godard 的预印本到 PQCrypto 关系仅为原始来源推定；CARDIS 2017/2018 与 Picnic 2021-07 的时间边界分开记录。','']
    (root/'CITATION_PROGRESS.md').write_text('\n'.join(lines))
    return {'verified_citation_edges':len(citations),'verified_version_edges':len(versions)-len(inferred_versions),'inferred_version_edges':len(inferred_versions),
            'task_status_counts':dict(Counter(t['status'] for t in tasks)),
            'unresolved_discoveries':len(pending_discoveries),'resolved_discoveries':len(resolved_discoveries)}

def render_adjacent(root,catalogs,decisions):
    catalog={r['id']:r for r in catalogs}
    adjacent=[d for d in decisions.values() if d['decision']=='adjacent']
    lines=['# 已阅读的相邻主题与方法背景','',
           f'当前 {len(adjacent)} 条；保留在目录与引用图中，不计入侧信道纳入论文数量。后续全文证据可以修订范围判定。','']
    for d in sorted(adjacent,key=lambda d:(catalog[d['id']]['venue_year'],catalog[d['id']]['title'])):
        r=catalog[d['id']]
        lines+=['## '+r['title'],'',f"- 来源：[{r['venue']} {r['venue_year']}]({r['url']})。",
                '- 判定依据：'+d['reason_zh'],
                '- 阅读来源：'+d.get('reading_source','publisher-deposited Crossref abstract')+'。',
                '- 核查日期：'+d['reviewed_on']+'；没有独立第二审读或本地复现。','']
    (root/'ADJACENT_NOTES.md').write_text('\n'.join(lines))

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
    review_date=max((r['reviewed_on'] for r in decisions.values()),default='2026-11-12')
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
    toc_checks={}
    for path in sorted((root/'provenance').glob('*.json')):
        for check in json.loads(path.read_text()).get('core_cell_crosschecks',[]):
            key=(check['venue'],check['year'])
            if key in toc_checks:raise ValueError('Multiple active TOC crosschecks: '+str(key))
            toc_checks[key]=dict(check,provenance_file=str(path.relative_to(root)))
    cells=[];lines=['# 目录覆盖与未完成工作','',f'阅读判定更新：{review_date}；目录截点仍为 2026-11-12。目录记录数不是相关论文数，也不是版本去重后的论文数。',
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
            toc=toc_checks.get((venue,year))
            cell={'venue':venue,'year':year,'catalog_records':n,'catalog_parsed':n>0,
                  'provenance_file':f'provenance/{filename}.json' if prov else None,
                  'independent_toc_crosscheck':toc['status'] if toc else 'pending','screened_records':reviewed,
                  'title_screened_records':title_reviewed,'abstract_screened_records':reviewed,
                  'citation_chasing':'pending','complete':False}
            if toc:cell['toc_crosscheck_provenance']=toc['provenance_file']
            cells.append(cell)
            link=f'[记录](provenance/{filename}.json)' if prov else '待取得'
            toc_caveat=f"；含 {toc['unpaginated_records']} 条无页码记录" if toc and toc['unpaginated_records'] else ''
            toc_label=f"[{toc['print_toc_records']} 条对应{toc_caveat}]({toc['provenance_file']})" if toc else '待核对'
            lines.append(f'| {venue} | {year} | {n if n else "待补齐"} | {toc_label} | {title_reviewed}/{n} | {reviewed}/{n} | {link} |')
    lines.extend(['','## 当前已知缺口','',
      '- S&P 2022、2023、2024、2025 已与另一来源取得的 IEEE 印刷论文集目录逐项对应；USENIX 2026 已与单独取得的官方论文集 PDF 目录对应。其余 25 个单元仍待独立核对；同一个 HTML 的两种导出不算独立证据，官方 PDF 也不是独立科学审查。',
      '- USENIX 2026 的 381 个议程节点已分为 362 篇论文和 19 条其他活动；2016 论文的回顾讨论不计作 2026 新论文。362 个标题已读、76 篇有摘要及以上判定，286 篇摘要仍待复核。五条 SDitH 发现已解析，后续 CiC/HQC 又登记 23 条待核查引用；目录一处 L∞/L_infinity 仅为数学记号差异。',
      '- S&P 2022 全部 147 条标题已读，49 个候选/不确定项有摘要判定，其余 98 条待复核。独立印刷目录 140 条规范化题名相同、7 条改题名；146 个可用出版起始页匹配，MSR Templating 的 Crossref 页码缺失。三处作者尾部字符已按印刷目录更正，其他名字形式及录用/出版差异保留。',
      '- IEEE S&P 2026 页面标题与目录年度为 2026，但有一个 cycle 小标题写 2025，保留为需复核的页面不一致。',
      '- IEEE S&P 2023 主列表漏列 DVFS Frequently Leaks Secrets；GoFetch 引用与另一官方日程促成补录，独立印刷目录现已确认全部 196 条。194 条规范化题名相同、2 条改题名；三个 N/A、两组重复 DOI 和五条作者字段差异保留待查。该年标题候选/不确定项共 48 条均有摘要判定，其余 148 条仍待摘要复核。',
      '- CCS 2026 为截至截点的官方录用目录；会议尚未举行，不能统一标为已正式发表。',
      '- Crossref 的 ISBN 查询只返回 CCS 论文集容器，不能用于证明其中没有论文；已改用官方网站目录。',
      '- TCHES 按卷年与出版日期分别处理，回看 2020 年元数据以补齐 2021 卷首期。Crossref 未提交引用列表不等于没有引用。',
      '- TCHES 已逐题初筛完整标题及可用副标题；标题暂判不是最终纳入/排除。卷首前言另存于 catalog-exclusions/tches.jsonl。',
      '- S&P 2025 的 255 条标题已初筛；印刷目录也有 255 条，254 条规范化题名相同、1 条经作者与主题核对为改题名。另有 1 条页码为 N/A，其最终出版状态待查；目录对应不等于全部摘要已读。',
      '- S&P 2024 的 261 条标题已初筛，42 个候选/不确定项已有摘要判定；独立印刷目录 259 条规范化题名相同、2 条改题名，四条需渲染页转录。出版元数据另保留五处题名变化与九条作者字段差异。S&P 2024、2025 各有 219 条仍待摘要复核，不能视为最终排除。',
      '- EasyCrypt S&P 2025 论文在录用/印刷目录与 IEEE 出版页间改题名；已按 DOI 合并身份并保留别名。ePrint 作者修订关系已核实，全文差异尚未逐项核对。',
      '- 摘要占位文本 Not Available 不计为可读摘要；标题层的相邻/范围外条目仍可被后续摘要或引用证据修订。',
      '- CRYPTO/EUROCRYPT/ASIACRYPT、PQCrypto、COSADE、HOST 等扩展来源仍待系统补齐；引用扩展取得少量条目不等于补齐会议年度目录。',
      '- 标题/摘要筛查、正式条目、版本归并与前后向引用追踪尚未完成。',
      '- 当前统计只针对已收集目录；未取得的目录、没有摘要的条目和日期不明记录均不视为完成。'])
    (root/'COVERAGE.md').write_text('\n'.join(lines)+'\n')
    papers=render_papers(root)
    render_adjacent(root,catalogs,decisions)
    citation_progress=render_citations(root,catalogs)
    extended=[r for r in catalogs if r['venue'] not in CORE_VENUES or not 2021<=r['venue_year']<=2026]
    elines=['# 引用与检索扩展来源','','这里只统计引用、检索和版本追踪实际取得的条目，**不是扩展会议的完整目录**。它们与核心会议共用 papers.jsonl、阅读队列和引用关系；版本记录不能直接相加为独立研究数量。','',
            '| 会议/来源 | 年份 | 已取得条目 | 完整目录与独立核对 |','|---|---:|---:|---|']
    for (v,y),n in sorted(Counter((r['venue'],r['venue_year']) for r in extended).items()):
        elines.append(f'| {v} | {y} | {n} | 未完成；引用/检索/版本扩展 |')
    elines+=['','SAC 2022 的会议年与 2024 年上线日期分别记录；ICCD 2021-10、ISCA 2021-06 和 ASIACCS 2021-05 论文作为窗口前边界引用保留。TCHES 2020 卷的 Share-slicing 于 2019-11 发表；CRYPTO 2020 的 FO 时序与 CHES 2017 的单轨迹论文也作为窗口外基础引用，不计入 2021–2026 核心单元。CRYPTO、EUROCRYPT、ASIACRYPT、COSADE 等扩展会议仍有系统目录收集任务；已有个别记录不等于完整覆盖。',
             '另保留 GLP 2018、CARDIS 2019（2020 上线）的 qTESLA、ACNS 2019 Dilithium、PLDI/S&P 2020 与 CCS 2017 基础文献。GLP 期刊版在线于 2023 年、卷年 2024；2022 Leveling 固定稿与 2023 Protecting 修正版分列。3D-Shield 仅核定 arXiv 记录，其作者声明的会议身份仍待独立核对。',
             'MPCitH/FAEST/HQC 引用补入 16 条记录；Picnic DPA 于 2021-07 上线，在滚动窗口前；CARDIS 2017 检测论文于 2018 上线。CCS 2016/2020、Keccak、TVLA、Private Circuits 与 DPA 等基础来源单列，FAEST 当前掩码实现撤回状态保留在卡片与笔记。',
             '[元数据](catalogs/citation-expansion.jsonl) · [首批来源与哈希](provenance/citation-expansion.json) · [此前来源](provenance/citation-followup-20261113.json) · [掩码与硬件补读来源](provenance/sp2023-reference-followup-20261113.json) · [四篇 Kyber 来源](provenance/kyber-four-reference-followup-20261113.json) · [MPCitH 后续来源](provenance/mpcith-followup-20261113.json) · [发现与解析历史](citations/discoveries.jsonl)','']
    (root/'EXTENDED_SOURCES.md').write_text('\n'.join(elines))
    title_lines=['# 标题与副标题初筛','','这是一轮人工阅读后的 Codex 判定，不是关键词自动分类。全部判定均为标题层暂判；后续摘要判定见 decisions.jsonl。','',
                 f'当前 {len(titles)} 条：'+', '.join(f'{k}={v}' for k,v in sorted(Counter(r['decision'] for r in titles.values()).items()))+'。',
                 '按来源计：'+', '.join(f'{v}={n}' for v,n in sorted(Counter(r['venue'] for r in titles.values()).items()))+'。未列来源仍待逐题筛查。',
                 'candidate=侧信道候选；adjacent=相邻主题；outside_title_scope=标题层范围外暂判；uncertain=标题不足以判定。没有因此删除任何研究论文目录条目。','',
                 '| 年/会议 | 论文 | 暂判 | 主题提示 |','|---|---|---|---|']
    urls={r['id']:r['url'] for r in catalogs}
    for r in sorted(titles.values(),key=lambda x:(x['venue_year'],x['venue'],x['title'])):
        title_lines.append(f"| {r['venue_year']} {r['venue']} | [{md(r['title'])}]({urls[r['id']]}) | {r['decision']} | {r['topic_hint']} |")
    title_lines += ['','逐条依据、阅读来源与是否独立复核见 [title-decisions.jsonl](screening/title-decisions.jsonl)。','']
    (root/'TITLE_SCREENING.md').write_text('\n'.join(title_lines))
    write_json(root/'coverage.json',{'cutoff':'2026-11-12','rolling_window_start':'2021-11-12','reading_updated_on':review_date,
               'total_catalog_records':len(catalogs),'priority_counts':dict(Counter(r['priority'] for r in queue)),
               'core_catalog_records':sum(counts[c['venue'],c['year']] for c in cells),'citation_expansion_records':len(extended),
               'title_screened_records':len(titles),'abstract_screened_records':len(decisions),
               'included_papers':len(papers),'reading_level_counts':dict(Counter(p['reading_level'] for p in papers)),
               'citation_progress':citation_progress,'core_cells':cells,'goal_complete':False})
    print(json.dumps({'catalog_records':len(catalogs),'pqc_queue':len(pqcqueue),
                      'abstracts_local':len(abstracts),'parsed_cells':sum(c['catalog_parsed'] for c in cells),
                      'completed_cells':0,'title_screened':len(titles),'screened':len(decisions),'included_papers':len(papers)},ensure_ascii=False))

if __name__=='__main__':main()
