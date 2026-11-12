#!/usr/bin/env python3
"""Validate artifact consistency, not completeness of the research literature."""
from collections import Counter
import json
from pathlib import Path
import re
from urllib.parse import unquote

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[3]

def read_rows(path):
    return [json.loads(x) for x in path.read_text().splitlines() if x]

catalog=[r for p in (ROOT/'catalogs').glob('*.jsonl') for r in read_rows(p)]
ids={r['id'] for r in catalog}
assert len(ids)==len(catalog),'Duplicate catalog identity'
assert all(r.get('title') and r.get('url') and r.get('source_ids') for r in catalog)
assert all(r.get('authors') or r.get('authors_display') for r in catalog),'Unresolved author field requires review'
coverage=json.loads((ROOT/'coverage.json').read_text())
counts=Counter((r['venue'],r['venue_year']) for r in catalog)
assert coverage['total_catalog_records']==len(catalog)
assert len(coverage['core_cells'])==30
for cell in coverage['core_cells']:
    assert cell['catalog_records']==counts[(cell['venue'],cell['year'])]
    assert cell['catalog_records']>0
    assert cell['complete'] is False,'This initial batch cannot claim completed screening'
papers=read_rows(ROOT/'papers.jsonl')
decisions=read_rows(ROOT/'screening/decisions.jsonl')
assert len({p['id'] for p in papers})==len(papers)
assert all(p['id'] in ids for p in papers)
assert {p['id'] for p in papers}=={d['id'] for d in decisions if d['decision']=='include'}
assert all(p['reading_level']=='abstract_and_bibliographic_metadata' for p in papers)
assert all('abstract' not in p for p in papers),'Do not mirror full abstracts'
queue=read_rows(ROOT/'screening/reading-queue.jsonl')
assert {q['id'] for q in queue}==ids
assert all(q['automatically_excluded'] is False for q in queue)
citation_tasks=read_rows(ROOT/'citations/queue.jsonl')
assert all(t['seed_id'] in {p['id'] for p in papers} for t in citation_tasks)
assert len({(t['seed_id'],t['direction']) for t in citation_tasks})==len(citation_tasks)
sources={s.get('source_id',s.get('id')) for p in (ROOT/'provenance').glob('*.json') for s in json.loads(p.read_text()).get('sources',[])}
assert all(s in sources for r in catalog for s in r['source_ids']),'Missing source provenance'
excluded=[r for p in (ROOT/'catalog-exclusions').glob('*.jsonl') for r in read_rows(p)]
assert all(r.get('reason') and r.get('source_ids') for r in excluded)
broken=[];links=0
docs=list(ROOT.rglob('*.md'))+[ROOT.parent/'README.md',ROOT.parent/'SOURCE_INDEX.md',ROOT.parent/'NEXT_ACTION.md',ROOT.parent/'records/2026-11-12-literature-catalog-batch.md']
for p in docs:
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',p.read_text()):
        if re.match(r'^(?:https?://|mailto:|#)',target):continue
        links+=1
        resolved=(p.parent/unquote(target.split('#')[0])).resolve()
        if not resolved.exists():broken.append((str(p.relative_to(REPO)),target))
assert not broken,broken
for p in ROOT.rglob('*'):
    if not p.is_file() or '__pycache__' in p.parts:continue
    assert p.suffix not in ['.pdf','.raw','.zip','.mat','.npy','.pyc']
    text=p.read_text()
    assert not re.search(r'/(?:Users|home)/[A-Za-z0-9][^\s/]*|AKIA[0-9A-Z]{16}|gh[pousr]_[A-Za-z0-9]{30,}',text)
print(json.dumps({'catalog_records':len(catalog),'core_cells':30,'nonpaper_entries':len(excluded),
                  'reviewed_abstracts':len(papers),'citation_tasks_pending':len(citation_tasks),
                  'relative_links_checked':links,'artifact_checks':'passed','literature_goal_complete':False}))
