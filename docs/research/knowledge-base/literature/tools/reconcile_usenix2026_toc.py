#!/usr/bin/env python3
"""Match the separately retrieved USENIX 2026 print TOC to the schedule catalog.

Requires PyMuPDF and cached usenix-2026-print-toc/chairs responses from Harvest.
This checks directory membership, not subject scope or scientific claims.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import unicodedata

import fitz
from harvest_catalogs import write_json, write_jsonl


def normalized(s):
    return ''.join(c for c in unicodedata.normalize('NFKD', s).casefold() if c.isalnum())


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--cache', type=Path, required=True)
    args = ap.parse_args()
    root = Path(__file__).resolve().parents[1]
    sources = []
    for key in ['usenix-2026-print-toc', 'usenix-2026-chairs']:
        meta = json.loads((args.cache / (key + '.meta.json')).read_text())
        raw = (args.cache / (key + '.raw')).read_bytes()
        assert meta['status'] == 200 and hashlib.sha256(raw).hexdigest() == meta['sha256']
        sources.append(meta)
    records = [json.loads(s) for s in (root / 'catalogs/usenix-2026.jsonl').read_text().splitlines()]
    by_title = {normalized(r['title']): r for r in records}
    assert len(by_title) == len(records)
    doc = fitz.open(args.cache / 'usenix-2026-print-toc.raw')
    toc, pending = [], ''
    for page_number, page in enumerate(doc, 1):
        for block in page.get_text('dict')['blocks']:
            for line in block.get('lines', []):
                # Keep mathematical spans in title lines, including the O(1)
                # set in a different font in Lighthouse's title.
                if not any('Bold' in s['font'] and s['size'] < 11 for s in line['spans']):
                    continue
                pending += ' ' + ''.join(s['text'] for s in line['spans']).strip()
                end = re.search(r'\.(?:\s*\.)*\s+(\d+)\s*$', pending)
                if not end:
                    continue
                title = pending[:end.start()].strip().rstrip('. ')
                key = normalized(title)
                match = 'normalized_title_exact'
                if key not in by_title and 'L∞ Distance' in title:
                    key = normalized(title.replace('L∞ Distance', 'L_infinity Distance'))
                    match = 'title_changed; mathematical notation L∞ versus L_infinity only; visually verified PDF page 13'
                assert key in by_title, title
                r = by_title[key]
                if match != 'normalized_title_exact':
                    r['published_title'] = title
                r['proceedings_start_page'] = end[1]
                r['source_ids'] = list(dict.fromkeys(r['source_ids'] + ['usenix-2026-print-toc']))
                toc.append({'catalog_id': r['id'], 'title': title, 'start_page': end[1],
                            'toc_pdf_page': page_number, 'match': match, 'checked_on': '2026-11-13',
                            'source_id': 'usenix-2026-print-toc', 'source_sha256': sources[0]['sha256']})
                pending = ''
    assert not pending.strip()
    assert len(toc) == len({r['catalog_id'] for r in toc}) == len(records) == 362
    assert {r['catalog_id'] for r in toc} == {r['id'] for r in records}
    assert len({r['start_page'] for r in toc}) == 362
    write_jsonl(root / 'catalogs/usenix-2026.jsonl', records)
    write_jsonl(root / 'toc-crosschecks/usenix-2026.jsonl', toc)
    exact = sum(r['match'] == 'normalized_title_exact' for r in toc)
    check = {'venue': 'USENIX', 'year': 2026, 'status': 'matched_print_toc',
             'inventory_file': 'toc-crosschecks/usenix-2026.jsonl', 'accepted_records': 362,
             'print_toc_records': 362, 'exact_normalized_title_matches': exact,
             'manually_matched_title_changes': 362 - exact, 'unpaginated_records': 0,
             'missing_from_toc': 0, 'extra_in_toc': 0,
             'scope': 'schedule versus separately retrieved publisher print TOC; same publishing organization, not an independent scientific review; mathematical spelling difference only'}
    write_json(root / 'provenance/usenix2026-print-toc-crosscheck-20261113.json', {
        'sources': sources, 'reviewed_on': '2026-11-13',
        'source_role': 'separate official proceedings PDF, independently retrieved from HTML schedule',
        'manual_checks': ['PDF title page and first TOC page', 'TOC page 13 L-infinity notation',
                          'program chairs PDF page 4: 166 + 196 = 362 accepted papers'],
        'core_cell_crosschecks': [check]})
    print(json.dumps(check))


if __name__ == '__main__':
    main()
