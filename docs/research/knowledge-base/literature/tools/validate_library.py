#!/usr/bin/env python3
"""Validate artifact consistency, not completeness of the research literature."""
from collections import Counter
import json
from pathlib import Path
import re
import unicodedata
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
allowed_reading={'abstract_and_bibliographic_metadata','selected_full_text_sections'}
assert all(p['reading_level'] in allowed_reading for p in papers)
assert all(p.get('reading_sections') and p.get('reading_source_ids') for p in papers if p['reading_level']=='selected_full_text_sections')
assert all('abstract' not in p for p in papers),'Do not mirror full abstracts'
assert len({d['id'] for d in decisions})==len(decisions)
assert all(d['id'] in ids for d in decisions)
titles=read_rows(ROOT/'screening/title-decisions.jsonl')
assert len({t['id'] for t in titles})==len(titles)
assert {t['id'] for t in titles}<={r['id'] for r in catalog},'Title decision without catalog identity'
# Saved title batches currently cover whole venue-year cells. This is an accounting
# invariant for those batches, not a claim that other cells have been screened.
for venue,year in {(t['venue'],t['venue_year']) for t in titles}:
    assert {t['id'] for t in titles if (t['venue'],t['venue_year'])==(venue,year)}=={r['id'] for r in catalog if (r['venue'],r['venue_year'])==(venue,year)},f'Incomplete saved title batch: {venue} {year}'
assert all(t['decision'] in {'candidate','adjacent','outside_title_scope','uncertain'} and t['final_scope_decision'] is False for t in titles)
assert coverage['title_screened_records']==len(titles)
assert coverage['abstract_screened_records']==len(decisions)
assert coverage['included_papers']==len(papers)
assert coverage['reading_level_counts']==dict(Counter(p['reading_level'] for p in papers))
assert coverage['core_catalog_records']==sum(c['catalog_records'] for c in coverage['core_cells'])
assert coverage['core_catalog_records']+coverage['citation_expansion_records']==len(catalog)
queue=read_rows(ROOT/'screening/reading-queue.jsonl')
assert {q['id'] for q in queue}==ids
assert all(q['automatically_excluded'] is False for q in queue)
for cell in coverage['core_cells']:
    assert cell['title_screened_records']==sum(t['venue']==cell['venue'] and t['venue_year']==cell['year'] for t in titles)
    assert cell['abstract_screened_records']==sum(q['venue']==cell['venue'] and q['venue_year']==cell['year'] and q['screening_status']!='pending' for q in queue)
citation_tasks=read_rows(ROOT/'citations/queue.jsonl')
assert all(t['seed_id'] in {p['id'] for p in papers} for t in citation_tasks)
assert len({(t['seed_id'],t['direction']) for t in citation_tasks})==len(citation_tasks)
sources={s.get('source_id',s.get('id')) for p in (ROOT/'provenance').glob('*.json') for s in json.loads(p.read_text()).get('sources',[])}
assert all(s in sources for r in catalog for s in r['source_ids']),'Missing source provenance'
assert all(s in sources for p in papers for s in p.get('reading_source_ids',[]))
catalog_map={r['id']:r for r in catalog}
toc_cells={}
normalize_title=lambda s: ''.join(c for c in unicodedata.normalize('NFKD',s).casefold() if c.isalnum())
for provenance in (ROOT/'provenance').glob('*.json'):
    data=json.loads(provenance.read_text())
    source_hashes={s.get('source_id',s.get('id')):s.get('sha256') for s in data.get('sources',[])}
    for check in data.get('core_cell_crosschecks',[]):
        key=(check['venue'],check['year'])
        assert key not in toc_cells
        toc_cells[key]=check
        inventory=read_rows(ROOT/check['inventory_file'])
        expected_ids={r['id'] for r in catalog if (r['venue'],r['venue_year'])==key}
        assert len(inventory)==len({r['catalog_id'] for r in inventory})==check['print_toc_records']
        assert {r['catalog_id'] for r in inventory}==expected_ids
        assert len(expected_ids)==check['accepted_records']
        assert check['missing_from_toc']==check['extra_in_toc']==0
        assert sum(r['start_page']=='N/A' for r in inventory)==check['unpaginated_records']
        exact=[r for r in inventory if r['match']=='normalized_title_exact']
        changed=[r for r in inventory if r['match'].startswith('title_changed;')]
        assert len(exact)==check['exact_normalized_title_matches']
        assert len(changed)==check['manually_matched_title_changes']
        assert len(exact)+len(changed)==len(inventory)
        assert all(normalize_title(r['title'])==normalize_title(catalog_map[r['catalog_id']]['title']) for r in exact)
        assert all(r['title']==catalog_map[r['catalog_id']]['published_title'] for r in changed)
        assert all(r['source_id'] in sources and r['source_sha256']==source_hashes[r['source_id']] for r in inventory)
        cell=next(c for c in coverage['core_cells'] if (c['venue'],c['year'])==key)
        assert cell['independent_toc_crosscheck']==check['status']
        assert cell['toc_crosscheck_provenance']==str(provenance.relative_to(ROOT))
assert all((c['venue'],c['year']) in toc_cells or c['independent_toc_crosscheck']=='pending' for c in coverage['core_cells'])
edges=read_rows(ROOT/'citations/edges.jsonl')
assert len({(e['from'],e['to'],e['type']) for e in edges})==len(edges)
assert all(e['to'] in ids for e in edges)
cites=[e for e in edges if e['type']=='cites']
assert all(e['from'] in ids and e['source_id'] in sources and len(e['source_sha256'])==64 for e in cites)
assert len({(e['from'],e['reference_number']) for e in cites})==len(cites)
gofetch_refs=read_rows(ROOT/'citations/gofetch-reference-screen.jsonl')
assert len(gofetch_refs)==98 and {r['reference_number'] for r in gofetch_refs}==set(range(1,99))
scheduled_refs=read_rows(ROOT/'citations/scheduled-disclosure-reference-screen.jsonl')
assert len(scheduled_refs)==79 and {r['reference_number'] for r in scheduled_refs}==set(range(1,80))
refs=[r for p in (ROOT/'citations').glob('*reference-screen.jsonl') for r in read_rows(p)]
assert len({(r['seed_id'],r['reference_number']) for r in refs})==len(refs)
assert all(r['seed_id'] in ids and r['source_id'] in sources for r in refs)
assert all(r['final_scope_decision'] is False for r in refs)
inventory_sources={r['source_id'] for r in refs}
assert {(r['seed_id'],r['reference_number'],r['target_id']) for r in refs if r['status']=='linked_catalog'}=={(e['from'],e['reference_number'],e['to']) for e in cites if e['source_id'] in inventory_sources}
discoveries=read_rows(ROOT/'citations/discoveries.jsonl')
assert len({d['discovery_id'] for d in discoveries})==len(discoveries)
pending_discoveries=[d for d in discoveries if d['status'].startswith('pending_')]
resolved_discoveries=[d for d in discoveries if d['status']=='resolved_identity_and_scope']
assert len(pending_discoveries)+len(resolved_discoveries)==len(discoveries),'Unknown discovery state'
assert {(r['seed_id'],r['reference_number']) for r in refs if r['status']=='discovery_queued'}=={(d['seed_id'],d['reference_number']) for d in pending_discoveries}
decision_map={d['id']:d for d in decisions}
for d in resolved_discoveries:
    assert d['target_id'] in ids and d['target_id'] in decision_map
    assert d['scope_decision']==decision_map[d['target_id']]['decision']
    assert any(e['from']==d['seed_id'] and e['to']==d['target_id'] and e['reference_number']==d['reference_number'] for e in cites)
assert coverage['citation_progress']['unresolved_discoveries']==len(pending_discoveries)
assert coverage['citation_progress']['resolved_discoveries']==len(resolved_discoveries)
assert coverage['citation_progress']['verified_citation_edges']==len(cites)
versions=[e for e in edges if e['type']!='cites']
inferred_versions=[e for e in versions if e.get('relation_confidence')=='primary_source_inference']
assert coverage['citation_progress']['verified_version_edges']==len(versions)-len(inferred_versions)
assert coverage['citation_progress']['inferred_version_edges']==len(inferred_versions)
assert coverage['citation_progress']['task_status_counts']==dict(Counter(t['status'] for t in citation_tasks))
excluded=[r for p in (ROOT/'catalog-exclusions').glob('*.jsonl') for r in read_rows(p)]
assert all(r.get('reason') and r.get('source_ids') for r in excluded)
for year in range(2021,2027):
    prov=json.loads((ROOT/f'provenance/usenix-{year}.json').read_text())
    assert prov['matched_nodes']==prov['parsed_records']+prov['nonpaper_entries'],f'Unaccounted USENIX schedule nodes in {year}'
    assert prov['retained_total']==counts[('USENIX',year)]
assert not ({r.get('id') for r in excluded if r.get('id')} & ids),'Excluded schedule entry retained as a paper'
broken=[];links=0
docs=list(ROOT.rglob('*.md'))+[ROOT.parent/'README.md',ROOT.parent/'SOURCE_INDEX.md',ROOT.parent/'NEXT_ACTION.md',*ROOT.parent.joinpath('records').glob('*literature*.md')]
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
                  'title_screened':len(titles),'abstract_or_above_decisions':len(decisions),'included_papers':len(papers),
                  'citation_task_status_counts':dict(Counter(t['status'] for t in citation_tasks)),
                  'citation_edges':len(cites),'version_edges':len(versions),'inferred_version_edges':len(inferred_versions),
                  'resolved_discoveries':len(resolved_discoveries),'pending_discoveries':len(pending_discoveries),
                  'relative_links_checked':links,'artifact_checks':'passed','literature_goal_complete':False}))
