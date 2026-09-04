"""Verifica estructura, material inactivo y PDF del curso; requiere pypdf."""
from pathlib import Path
from hashlib import sha256
import csv
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

sector_source = (ROOT / 'modules/00_sector_publico.tex').read_text(encoding='utf-8')
assert sector_source.count(r'\begin{frame}') == 2
sector_frames = sector_source[sector_source.index(r'\begin{frame}'):].strip()
assert sha256(sector_frames.encode('utf-8')).hexdigest() == '93fb10f78aa9d1e8314bc0d69fa81ed825d5d9f5cebe5a31821db29f5ead0973', 'Se alteraron las dos láminas originales de FPC.'

annex_source = (ROOT / 'modules/03b_anexos_presidenciales.tex').read_text(encoding='utf-8')
assert annex_source.count(r'\begin{frame}') == 2
main = (ROOT / 'main.tex').read_text(encoding='utf-8')
input_order = ['modules/01_conceptos_fiscales', 'modules/02_ejecucion_presupuestal', 'modules/02b_cobertura',
               'modules/03_espejo_convertidor', 'modules/03b_anexos_presidenciales',
               'modules/03c_comparativo_pgn2027',
               'modules/03d_ejercicio_conciliacion', 'modules/00_sector_publico',
               'modules/03e_deuda_regla', 'modules/04_laberinto']
positions = [main.index(r'\input{' + name + '}') for name in input_order]
assert positions == sorted(positions), 'Cambió el orden solicitado: cobertura antes del convertidor; sector público, deuda y regla antes del libro.'
assert all(r'\input{slides/' + name + '}' not in main for name in ['pf2024', 'pf2025', 'pf2026']), 'Solo debe estar activo el bloque fiscal de 2027.'
assert not re.search(r'\\(?:input|begin\{frame\})', main[positions[-2] + len(r'\input{modules/03e_deuda_regla}'):positions[-1]])
for module, count in [('02b_cobertura', 1), ('03d_ejercicio_conciliacion', 2), ('03e_deuda_regla', 4)]:
    assert (ROOT / f'modules/{module}.tex').read_text(encoding='utf-8').count(r'\begin{frame}') == count

comparison = (ROOT / 'modules/03c_comparativo_pgn2027.tex').read_text(encoding='utf-8')
assert comparison.count(r'\begin{frame}') == 1
with (ROOT / 'data/comparativo_pgn_2027.csv').open(encoding='utf-8', newline='') as source:
    rows = list(csv.DictReader(source))
assert len(rows) == 8
assert len({row['concepto'] for row in rows}) == 8
expected_source = [(367698, 392560), (89960, 86960), (118041, 155432), (27604, 58272),
                   (87714, 94421), (295, 311), (2429, 2429), (575699, 634952)]
for row, expected_values in zip(rows, expected_source):
    petro, abelardo, difference = [int(row[key]) for key in ['petro_miles_millones', 'abelardo_miles_millones', 'diferencia_miles_millones']]
    assert (petro, abelardo) == expected_values, 'Las cifras difieren de los cuadros 1.6.1 y 1.6.6.'
    assert difference == abelardo - petro
    for value in [petro, abelardo, difference]:
        assert f'{value / 1000:.3f}'.replace('.', ',') in comparison.replace('{,}', ',')
for column in ['petro_miles_millones', 'abelardo_miles_millones']:
    amounts = [int(row[column]) for row in rows]
    assert amounts[0] + amounts[1] + amounts[2] == amounts[7]
    assert sum(amounts[3:7]) - amounts[2] == 1, 'Debe conservarse y advertirse la discrepancia de la fuente.'
assert '0,001 billones' in comparison and 'Cifras proyectadas' in comparison
for name, expected in {
    'balance_fiscal_pf_julio_2027.png': 'b99643c8a9f7c56d1a2925652d19e0bdcc920722858ce2f6fd3a9f2c9a360b97',
    'balance_fiscal_pgn2027_actualizado.png': '7d00122acfbe3f9630e3acd7ec0d394b71712985460705c55c060ba3abff7b2b',
}.items():
    assert sha256((ROOT / 'assets' / name).read_bytes()).hexdigest() == expected, f'Se alteró la imagen original: {name}'

pdf = PdfReader(ROOT / 'output/pdf/Curso_PGN.pdf')
assert len(pdf.pages) == 78, f'Se esperaban 78 páginas, hay {len(pdf.pages)}'
texts = [p.extract_text() or '' for p in pdf.pages]
assert all(len(t.strip()) > 15 for t in texts), 'Página vacía'
for page in pdf.pages:
    assert abs(float(page.mediabox.width) / float(page.mediabox.height) - 16/9) < .002
for page, expected in [(3, 'entendemos por ingresos y gastos'), (34, 'PGN, GNC y gobierno general'),
                       (35, 'espejos'), (36, 'convertidor'), (37, 'caja negra'),
                       (38, 'proyecciones 2026 y 2027'), (39, 'Balance fiscal 2027'),
                       (40, 'Petro frente a Abelardo'), (41, 'Ejercicio: reconstruir'),
                       (42, 'Solución: el balance'),
                       (43, 'Desagregación del Sector Público Consolidado'),
                       (44, 'Balance fiscal del Sector Público No Financiero, 2025'),
                       (45, 'balance primario determinan'), (46, 'paso a paso'),
                       (47, 'balance primario neto estructural'), (48, 'desvío es temporal'),
                       (49, 'libro')]:
    assert expected in ' '.join(texts[page-1].split()), (page, expected)
for page in [38, 39]:
    assert len(pdf.pages[page-1].images) == 1, f'Falta el cuadro en la página {page}'
assert 'no son consistentes' in ' '.join(texts[38].split()), 'Falta la advertencia sobre los porcentajes del cuadro original.'
comparison_text = ' '.join(texts[39].split())
for row in rows:
    assert row['concepto'] in comparison_text
    for key in ['petro_miles_millones', 'abelardo_miles_millones', 'diferencia_miles_millones']:
        value = int(row[key])
        # pypdf introduce espacios tras comas en algunas fuentes matemáticas.
        assert f'{abs(value) / 1000:.3f}'.replace('.', ',') in comparison_text.replace(' ', '')
assert 'Cifras proyectadas' in comparison_text and '0,001 billones' in comparison_text

# Ejercicio: resultados recalculados, no sustituciones silenciosas de las imágenes.
solution = texts[41].replace(' ', '').replace('\n', '')
incomes = [325281, 369731, 328766]
primary_spending = [366681, 381352, 424448]
total_spending = [431760, 465287, 529175]
for revenue, primary, total in zip(incomes, primary_spending, total_spending):
    for balance in [revenue - primary, revenue - total]:
        assert f'{abs(balance)/1000:.3f}'.replace('.', ',') in solution
assert (incomes[2] - incomes[1]) - (total_spending[2] - total_spending[1]) == -104853
assert 634952 - 58272 == 576680
assert all(value in solution for value in ['40,965', '63,888', '104,853', '576,680', '529,175', '0,001'])
debt_example = ' '.join(texts[45].split()).replace(' ', '')
assert round((1.08/1.06)*60-1, 2) == 60.13
assert round((.08-.06)/1.06*60, 2) == 1.13
assert all(value in debt_example for value in ['63,74', '60,13', '1,13'])
assert round(-1-(-.4)-(-.2)-.1, 2) == -.5
assert round(.2+.1*(60-55), 2) == .7
assert '0,5' in texts[46].replace(' ', '')
assert 'no es la meta oficial de 2027' in ' '.join(texts[47].split())
assert '2028' in texts[47] and '55%' in texts[46].replace(' ', '') and '71%' in texts[46].replace(' ', '')

# Firmas de láminas internas que deben permanecer desactivadas.
for inactive in ['Lecciones de casos comparados', 'debt overhang', 'AFP y bancos']:
    assert inactive not in '\n'.join(texts), f'Se activó material inactivo: {inactive}'
log = ROOT / 'tmp/latex/main.log'
if log.exists():
    log_text = log.read_text(encoding='utf-8', errors='replace')
    assert not re.search(r'Overfull \\[hv]box|Missing character|Undefined control sequence', log_text), 'Revisar advertencias LaTeX'
print('OK: 78 páginas 16:9; 48 en la sesión 1 y 30 del libro en la sesión 2.')
print('OK: cobertura PGN/GNC/GG en 34; bloque fiscal de 2027 en 38–42.')
print('OK: sector público original de FPC intacto en 43–44.')
print('OK: secuencia del libro y todos sus comentarios intactos; 78 fuentes y 7 imágenes.')
print('OK: los dos cuadros originales están en 38–39, sin duplicar ni alterar sus PNG.')
print('OK: Petro–Abelardo en 40; ejercicio y solución verificados en 41–42.')
print('OK: cuatro láminas de deuda y regla fiscal en 45–48, antes del libro; cálculos y salvedad de escape verificados.')
print('OK: sin páginas vacías, glifos ausentes ni desbordamientos de LaTeX.')
