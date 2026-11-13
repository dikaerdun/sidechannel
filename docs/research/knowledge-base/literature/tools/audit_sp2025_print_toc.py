#!/usr/bin/env python3
"""Recheck the frozen S&P 2025 print TOC against the saved row inventory.

Requires PyMuPDF. Reads an externally stored PDF; writes nothing and does not
establish final publication status, subject coverage, or scientific correctness.
The font/size rules are specific to the exact source hash recorded in provenance.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re

import fitz


def extract(pdf):
    records, title, first_page = [], [], None
    for page_number, page in enumerate(pdf, 1):
        for block in page.get_text('dict')['blocks']:
            for line in block.get('lines', []):
                spans = line['spans']
                if not spans or not all(
                    s['font'] == 'PalatinoLinotype-Roman'
                    and abs(s['size'] - 10) < 0.1 for s in spans
                ):
                    continue
                text = ''.join(s['text'] for s in spans).strip()
                # Two records put the title and page number in the same span.
                inline = re.fullmatch(r'(.*?)\s{2,}(\d+|N/A)', text)
                if inline:
                    first_page = first_page or page_number
                    title.append(inline.group(1))
                    text = inline.group(2)
                if re.fullmatch(r'\d+|N/A', text):
                    if not title:
                        raise ValueError('Page number without title')
                    records.append({'title': ' '.join(title), 'start_page': text,
                                    'toc_pdf_page': first_page})
                    title, first_page = [], None
                else:
                    first_page = first_page or page_number
                    title.append(text)
    if title:
        raise ValueError('Unterminated title: ' + ' '.join(title))
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pdf', type=Path, required=True)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    provenance = json.loads((args.root/'provenance/sp2025-print-toc-crosscheck-20261113.json').read_text())
    raw = args.pdf.read_bytes()
    source = provenance['sources'][0]
    if hashlib.sha256(raw).hexdigest() != source['sha256']:
        raise ValueError('Source PDF changed; perform a fresh audit instead of reusing this inventory')
    with fitz.open(stream=raw, filetype='pdf') as pdf:
        actual = extract(pdf)
    expected = [json.loads(line) for line in (args.root/'toc-crosschecks/sp-2025.jsonl').read_text().splitlines() if line]
    projection = [{key: row[key] for key in ('title', 'start_page', 'toc_pdf_page')} for row in expected]
    if actual != projection:
        raise ValueError('Extracted TOC differs from saved inventory')
    print(json.dumps({'source_hash_matched': True, 'print_toc_rows_verified': len(actual),
                      'unpaginated_rows': sum(r['start_page'] == 'N/A' for r in actual),
                      'scope': 'frozen PDF extraction only; run validate_library.py for catalog mapping'}))


if __name__ == '__main__':
    main()
