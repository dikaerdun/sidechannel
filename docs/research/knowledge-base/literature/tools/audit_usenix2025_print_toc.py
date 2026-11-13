#!/usr/bin/env python3
"""Read-only source audit of the frozen USENIX 2025 printed TOC.

Checks title/page extraction and published inventory; not scientific scope or
the unexplained 407+32 versus 438 discrepancy in the chairs' message.
Requires PyMuPDF; the PDF stays outside the repository.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import unicodedata

import fitz

SHA256 = '1802c2a8963a239e27f199d881713ab3ced63b4d983c4dd49fd55113ce8ebefa'


def normalized(text):
    return ''.join(c for c in unicodedata.normalize('NFKD', text).casefold() if c.isalnum())


def extract(pdf):
    assert hashlib.sha256(pdf.read_bytes()).hexdigest() == SHA256, 'Unexpected source PDF'
    pending, rows = '', []
    with fitz.open(pdf) as doc:
        for page_no, page in enumerate(doc, 1):
            for block in page.get_text('dict')['blocks']:
                for line in block.get('lines', []):
                    if not any('Bold' in s['font'] and s['size'] < 11 for s in line['spans']):
                        continue
                    pending += ' ' + ''.join(s['text'] for s in line['spans']).strip()
                    end = re.search(r'\.(?:\s*\.)*\s+(\d+)\s*$', pending)
                    if end:
                        rows.append({'title': pending[:end.start()].strip().rstrip('. '),
                                     'start_page': end[1], 'toc_pdf_page': page_no})
                        pending = ''
    assert not pending.strip()
    assert len(rows) == len({normalized(r['title']) for r in rows}) == 438
    assert len({r['start_page'] for r in rows}) == 438
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--pdf', type=Path, required=True)
    args = ap.parse_args()
    root = Path(__file__).resolve().parents[1]
    source_rows = extract(args.pdf)
    saved = [json.loads(s) for s in (root / 'toc-crosschecks/usenix-2025.jsonl').read_text().splitlines()]
    projected = [{k: r[k] for k in ['title', 'start_page', 'toc_pdf_page']} for r in saved]
    assert source_rows == projected, 'Published inventory differs from source extraction'
    print(json.dumps({'source_sha256': SHA256, 'source_records': len(source_rows),
                      'exact_inventory_match': True, 'scientific_validation': False}))


if __name__ == '__main__':
    main()
