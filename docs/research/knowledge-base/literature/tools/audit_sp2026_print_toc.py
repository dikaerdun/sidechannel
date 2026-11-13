#!/usr/bin/env python3
"""Re-extract the frozen SP 2026 print TOC; check membership with validate_library.py.

Requires PyMuPDF and the externally stored PDF. Cover/copyright pages are
excluded. The printed pagination differs from publisher metadata; neither
source is silently used to repair the other.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re

import fitz


def extract(pdf):
    out=[]; pending=[]; start=None
    for pno,page in enumerate(pdf,1):
        if pno<3:
            continue
        for block in page.get_text('dict')['blocks']:
            for line in block.get('lines',[]):
                spans=line['spans']
                if not spans or not all(s['font']=='Times-Roman' and abs(s['size']-10)<.1 for s in spans):
                    continue
                text=''.join(s['text'] for s in spans).strip()
                if not text:
                    continue
                match=re.search(r'\.{2,}\s*(\d+|N/A)\s*$',text)
                start=start or pno
                if match:
                    pending.append(text[:match.start()].strip())
                    out.append({'title':' '.join(pending),'start_page':match[1],'toc_pdf_page':start})
                    pending=[]; start=None
                else:
                    pending.append(text)
    if pending:
        raise ValueError('Unparsed trailing title text')
    return out


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pdf',type=Path,required=True)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    args=parser.parse_args()
    provenance=json.loads((args.root/'provenance/sp2026-print-toc-crosscheck-20261114.json').read_text())
    source=next(s for s in provenance['sources'] if s['source_id']=='sp26-print-toc')
    raw=args.pdf.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=source['sha256']:
        raise ValueError('Source changed; a fresh audit is required')
    with fitz.open(stream=raw,filetype='pdf') as pdf:
        actual=extract(pdf)
    saved=[json.loads(s) for s in (args.root/'toc-crosschecks/sp-2026.jsonl').read_text().splitlines() if s]
    expected=[{k:r[k] for k in ('title','start_page','toc_pdf_page')} for r in saved]
    if actual!=expected or len(actual)!=252:
        raise ValueError('Expected all 252 frozen TOC rows to match')
    print(json.dumps({'source_hash_matched':True,'saved_rows_matched':len(actual),
                      'scope':'extraction consistency; two missing catalog entries remain unresolved'}))


if __name__=='__main__':
    main()
