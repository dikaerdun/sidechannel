#!/usr/bin/env python3
"""Re-extract the frozen SP 2022 print TOC; not a new visual or completeness review."""
from pathlib import Path
import argparse,hashlib,fitz,json,re
def decode(s):
 out=[]
 for ch in s:
  c=ord(ch)
  if c==32:out.append(' ')
  elif 3<=c<=93:out.append(chr(c+29))
  elif c in {519,522,523,918}:out.append({519:'’',522:'“',523:'”',918:'I'}[c])
  else:raise ValueError(('unknown',c,s))
 return ''.join(out)
def extract(pdf):
 out=[];title=[];first=None
 for i in range(2,len(pdf)):
  for b in pdf[i].get_text('dict')['blocks']:
   for line in b.get('lines',[]):
    spans=line['spans']
    if not spans or not all(s['font']=='OpenSans-Regular' and abs(s['size']-10)<.01 for s in spans):continue
    s=decode(''.join(x['text'] for x in spans)).strip()
    if not s:continue
    inline=re.fullmatch(r'(.*?)\s+(\d+|N/A)',s)
    if inline:
     title.append(inline.group(1));first=first or i+1;s=inline.group(2)
    if re.fullmatch(r'\d+|N/A',s):
     assert title,('missing title',i,s)
     out.append(dict(title=' '.join(title),start_page=s,toc_pdf_page=first));title=[];first=None
    else:title.append(s);first=first or i+1
 assert not title,title
 return out

def main():
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--pdf',type=Path,required=True)
 parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
 args=parser.parse_args()
 provenance=json.loads((args.root/'provenance/sp2022-print-toc-crosscheck-20261113.json').read_text())
 source=next(s for s in provenance['sources'] if s['source_id']=='sp22-print-toc')
 raw=args.pdf.read_bytes()
 if hashlib.sha256(raw).hexdigest()!=source['sha256']:raise ValueError('Source changed; repeat visual calibration and audit')
 with fitz.open(stream=raw,filetype='pdf') as pdf:actual=extract(pdf)
 expected=[json.loads(l) for l in (args.root/'toc-crosschecks/sp-2022.jsonl').read_text().splitlines() if l]
 projection=[{k:r[k] for k in ['title','start_page','toc_pdf_page']} for r in expected]
 if actual!=projection:raise ValueError('Extracted TOC differs from saved inventory')
 print(json.dumps({'source_hash_matched':True,'glyph_decoded_rows_verified':len(actual),'scope':'source-specific extraction only; catalog mapping checked by validate_library.py'}))
if __name__=='__main__':main()
