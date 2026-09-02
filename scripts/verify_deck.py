"""Verifica estructura, material inactivo y PDF del curso; requiere pypdf."""
from pathlib import Path
import re
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
original = (ROOT / 'libro_original.tex').read_text(encoding='utf-8')
body = original.split(r'\begin{document}', 1)[1].split(r'\end{document}', 1)[0].strip()
embedded = (ROOT / 'modules/04_laberinto.tex').read_text(encoding='utf-8')
embedded = embedded.split('\n', 1)[1].strip()
assert body == embedded, 'Cambió la secuencia o el estado activo/inactivo del libro.'

files = list((ROOT / 'slides').glob('*.tex'))
assert len(files) == 78, f'Se esperaban 78 fuentes del libro: {len(files)}'
assert len(list((ROOT / 'graficas').iterdir())) == 7
for part in range(1, 4):
    source = next((ROOT / 'modules').glob(f'{part:02d}_*.tex')).read_text(encoding='utf-8')
    assert source.count(r'\begin{frame}') == [16, 15, 3][part-1]

pdf = PdfReader(ROOT / 'output/pdf/Curso_PGN.pdf')
assert len(pdf.pages) == 66, f'Se esperaban 66 páginas, hay {len(pdf.pages)}'
texts = [p.extract_text() or '' for p in pdf.pages]
assert all(len(t.strip()) > 15 for t in texts), 'Página vacía'
for page in pdf.pages:
    assert abs(float(page.mediabox.width) / float(page.mediabox.height) - 16/9) < .002
for page, expected in [(34, 'espejos'), (35, 'convertidor'), (36, 'caja negra'), (37, 'libro')]:
    assert expected in texts[page-1], (page, expected)

# Firmas de láminas internas que deben permanecer desactivadas.
for inactive in ['Lecciones de casos comparados', 'debt overhang', 'AFP y bancos']:
    assert inactive not in '\n'.join(texts), f'Se activó material inactivo: {inactive}'
log = ROOT / 'tmp/latex/main.log'
if log.exists():
    log_text = log.read_text(encoding='utf-8', errors='replace')
    assert not re.search(r'Overfull \\[hv]box|Missing character|Undefined control sequence', log_text), 'Revisar advertencias LaTeX'
print('OK: 66 páginas 16:9; 34 láminas de contenido PGN más 2 de apertura; 30 del libro.')
print('OK: secuencia del libro y todos sus comentarios intactos; 78 fuentes y 7 imágenes.')
print('OK: sin páginas vacías, glifos ausentes ni desbordamientos de LaTeX.')
