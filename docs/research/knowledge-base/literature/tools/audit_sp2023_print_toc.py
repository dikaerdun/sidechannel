#!/usr/bin/env python3
"""Re-extract the frozen SP 2023 print TOC using a visually calibrated glyph map.

The embedded fonts lack usable Unicode mappings. The map was calibrated against
rendered PDF pages 3, 5, 7, 8, 11, 13, 20, 28, not from catalog titles. Unknown
glyphs fail closed. This is a source-specific extraction check, not a new visual
review, final-publication check, or proof of subject coverage.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re

import fitz

SPECIAL = {32: ' ', 561: ' ', 497: ':', 556: '-', 495: '.', 550: '/',
           507: '(', 508: ')', 496: ',', 519: '’', 520: '"', 501: '?',
           503: '!', 515: '“', 516: '”', 558: '–', 440: '+', 514: '’', 493: '&'}


def decode(text):
    result = []
    for char in text:
        code = ord(char)
        if 3 <= code <= 28:
            result.append(chr(code + 62))
        elif 138 <= code <= 163:
            result.append(chr(code - 41))
        elif 342 <= code <= 351:
            result.append(chr(code - 294))
        elif code in SPECIAL:
            result.append(SPECIAL[code])
        else:
            raise ValueError('Unknown source glyph code: ' + str(code))
    return ''.join(result)


def extract(pdf):
    rows, title, first_page = [], [], None
    for index in range(2, len(pdf)):
        for block in pdf[index].get_text('dict')['blocks']:
            for line in block.get('lines', []):
                spans = line['spans']
                if not spans or not all(s['font'] in {'PalatinoLinotype-Roman', 'PalatinoLinotype'} for s in spans):
                    continue
                if not all(abs(s['size'] - (6.541 if index == 27 else 10)) < .01 for s in spans):
                    continue
                text = decode(''.join(s['text'] for s in spans)).strip()
                if not text:
                    continue
                inline = re.fullmatch(r'(.*?)\s{2,}(\d+|N/A)', text)
                if inline:
                    first_page = first_page or index + 1
                    title.append(inline.group(1))
                    text = inline.group(2)
                if re.fullmatch(r'\d+|N/A', text):
                    if not title:
                        raise ValueError('Page number without title')
                    rows.append({'title': ' '.join(title), 'start_page': text, 'toc_pdf_page': first_page})
                    title, first_page = [], None
                else:
                    first_page = first_page or index + 1
                    title.append(text)
    if title:
        raise ValueError('Unterminated title')
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pdf', type=Path, required=True)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    provenance = json.loads((args.root / 'provenance/sp2023-print-toc-crosscheck-20261113.json').read_text())
    source = next(s for s in provenance['sources'] if s['source_id'] == 'sp2023-print-toc')
    raw = args.pdf.read_bytes()
    if hashlib.sha256(raw).hexdigest() != source['sha256']:
        raise ValueError('Source PDF changed; perform a fresh visual calibration and audit')
    with fitz.open(stream=raw, filetype='pdf') as pdf:
        actual = extract(pdf)
    expected = [json.loads(line) for line in (args.root / 'toc-crosschecks/sp-2023.jsonl').read_text().splitlines() if line]
    projection = [{key: row[key] for key in ('title', 'start_page', 'toc_pdf_page')} for row in expected]
    if actual != projection:
        raise ValueError('Extracted TOC differs from saved inventory')
    print(json.dumps({'source_hash_matched': True, 'glyph_decoded_rows_verified': len(actual),
                      'unpaginated_rows': sum(r['start_page'] == 'N/A' for r in actual),
                      'scope': 'frozen glyph-decoded extraction; run validate_library.py for catalog mapping'}))


if __name__ == '__main__':
    main()
