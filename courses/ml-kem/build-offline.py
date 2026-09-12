"""Export the exact local course as one offline HTML file."""
from pathlib import Path
import base64
import re

root = Path(__file__).resolve().parent
html = (root / 'index.html').read_text(encoding='utf-8')
for name in ['style.css', 'extra.css']:
    css = (root / name).read_text(encoding='utf-8')
    html = html.replace(f'<link rel="stylesheet" href="./{name}">', '<style>\n' + css + '\n</style>')
license_data = base64.b64encode((root / 'third-party-licenses.txt').read_bytes()).decode('ascii')
for name in ['crypto-bundle.js', 'math.js', 'real-ntt.js', 'extra.js', 'app.js']:
    js = (root / name).read_text(encoding='utf-8')
    if '</script' in js.lower():
        raise ValueError('Unsafe inline script end in ' + name)
    js = js.replace('href="./third-party-licenses.txt"', 'download="third-party-licenses.txt" href="data:text/plain;base64,' + license_data + '"')
    js = js.replace('href="../../docs/', 'href="https://github.com/dikaerdun/sidechannel/blob/main/docs/')
    js = js.replace('href="./TEACHING_GUIDE.zh-CN.md"', 'href="https://github.com/dikaerdun/sidechannel/blob/main/courses/ml-kem/TEACHING_GUIDE.zh-CN.md"')
    html = html.replace(f'<script src="./{name}"></script>', '<script>\n' + js + '\n</script>')
assert not re.search(r'<script\s+src=', html)
assert '<link rel="stylesheet"' not in html
out = root / 'ML-KEM_Interactive_Offline.html'
out.write_text(html, encoding='utf-8')
print(out.name, out.stat().st_size, 'bytes')
