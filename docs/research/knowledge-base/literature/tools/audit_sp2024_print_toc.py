#!/usr/bin/env python3
"""Recheck 257 extracted and four visually transcribed SP 2024 TOC rows.

Requires PyMuPDF and the exact externally stored source PDF. The four rows on
PDF page 3 were visually read during curation because its font encoding is
damaged. This tool preserves that transcription; it does not revalidate it by
OCR or claim an independent second visual reading.
"""
import argparse
import hashlib
import json
from pathlib import Path

import fitz
from audit_sp2025_print_toc import extract


VISUAL_PAGE_3 = [
    ('On SMS Phishing Tactics and Infrastructure', '1'),
    ('Conning the Crypto Conman: End-to-End Analysis of Cryptocurrency-based Technical Support Scams', '17'),
    ('From Chatbots to Phishbots?: Phishing Scam Generation in Commercial Large Language Models', '36'),
    ('A Representative Study on Human Detection of Artificially Generated Media Across Countries', '55'),
]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pdf', type=Path, required=True)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    provenance = json.loads((args.root / 'provenance/sp2024-print-toc-crosscheck-20261113.json').read_text())
    source = next(s for s in provenance['sources'] if s['source_id'] == 'sp2024-print-toc')
    raw = args.pdf.read_bytes()
    if hashlib.sha256(raw).hexdigest() != source['sha256']:
        raise ValueError('Source PDF changed; perform a fresh audit instead of reusing this inventory')
    with fitz.open(stream=raw, filetype='pdf') as pdf:
        pdf.delete_pages(0, 2)
        extracted = extract(pdf)
    for row in extracted:
        row['toc_pdf_page'] += 3
    if len(extracted) != 257:
        raise ValueError('Expected 257 text-extracted rows')
    visual = [{'title': title, 'start_page': page, 'toc_pdf_page': 3}
              for title, page in VISUAL_PAGE_3]
    actual = visual + extracted
    expected = [json.loads(line) for line in (args.root / 'toc-crosschecks/sp-2024.jsonl').read_text().splitlines() if line]
    projection = [{key: row[key] for key in ('title', 'start_page', 'toc_pdf_page')} for row in expected]
    if actual != projection:
        raise ValueError('TOC extraction/transcription differs from saved inventory')
    print(json.dumps({'source_hash_matched': True, 'text_extracted_rows_verified': len(extracted),
                      'previous_visual_transcriptions_preserved': len(visual),
                      'saved_rows_matched': len(actual),
                      'scope': 'frozen extraction plus saved visual transcription; run validate_library.py for catalog mapping'}))


if __name__ == '__main__':
    main()
