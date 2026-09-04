# Curso de Presupuesto General de la Nación

Oliver Pardo · Septiembre de 2026 · Dos sesiones de tres horas.

La presentación editable está en `main.tex`. El PDF se publica en `output/pdf/Curso_PGN.pdf`.

El PDF contiene **78 diapositivas**: sesión 1, páginas 1–48; sesión 2, páginas 49–78. La distinción entre PGN, GNC y gobierno general está en la página 34; los diagramas del espejo y convertidor, en 35–37; los dos cuadros de los anexos, en 38–39; el comparativo Petro–Abelardo, en 40; y el ejercicio de conciliación con su solución, en 41–42. Las láminas originales de clasificación de FPC están en 43–44 y el bloque de deuda y regla fiscal, en 45–48, antes del libro.

## Contenido

1. Ingresos, gastos y financiamiento: adaptación del curso FPC, con sus ejemplos de crédito, amortización, intereses, hipoteca y venta de activos.
2. Apropiaciones, compromisos, obligaciones y pagos: adaptación de FPC, complementada con CDP, RP, PAC, reservas, cuentas por pagar y un ejercicio resuelto.
3. Una lámina distingue PGN, GNC y gobierno general. Le siguen tres láminas consecutivas con idéntica estructura: espejo entre contabilidad presupuestal y fiscal; convertidor; convertidor como caja negra.
4. Dos cuadros de los anexos presidenciales, como caso para discutir el convertidor: proyecciones del plan financiero para 2026–2027 y comparación del balance fiscal 2027 entre MFMP, PGN y actualización. Se reproducen las imágenes originales, con sus cifras, unidades, fuente y condición de proyecciones. Se mantiene la advertencia de FPC sobre los porcentajes inconsistentes de gasto y balances de la columna «PGN Petro».
5. Cuadro comparativo de los proyectos del PGN 2027 de Petro (julio de 2026) y Abelardo (agosto de 2026): funcionamiento, inversión y servicio de la deuda, separado en amortizaciones (principal), intereses, comisiones y otros gastos, y Fondo de Contingencias. Incluye el total y las diferencias Abelardo menos Petro, en billones de pesos corrientes. Son proyecciones, no ejecución.
6. Ejercicio y solución de conciliación: reconstruir balances primario y total de los cuadros, descomponer la revisión de 2027 en ingresos y gastos, y explicar por qué no basta con restar el principal del PGN para llegar al gasto fiscal del GNC. No se duplican las imágenes originales.
7. Dos láminas copiadas textualmente de FPC, antes del bloque de deuda y del libro: «Desagregación del Sector Público Consolidado» y «Balance fiscal del Sector Público No Financiero, 2025». Se conservan sus textos, cifras, clasificación y código LaTeX; solo se omiten las repeticiones idénticas del esquema.
8. Cuatro láminas de deuda y regla fiscal, seleccionadas y sintetizadas de FPC: ecuación exacta y superávit estabilizador, ejemplo numérico paso a paso, definición y cálculo del BPNE, y fórmula ordinaria con ejemplo de cumplimiento y distinción de la cláusula de escape. Se conservan los supuestos y resultados de los ejemplos originales.
9. Presentación completa de *El laberinto fiscal de Colombia*: las 30 diapositivas activas de la versión independiente, en su orden original.

## Fuentes y comparabilidad del PGN 2027

El comparativo toma las columnas **Proyecto 2027** de los cuadros 1.6.1 y 1.6.6 del MHCP–DGPPN:

- Anexo al mensaje presidencial, julio de 2026: páginas impresas 37 y 53 (páginas PDF 58 y 74). Fuente local: `C:/Users/olive/Downloads/2.Anexo Mensaje PGN 2027.pdf`.
- Anexo al mensaje presidencial reformulado, agosto de 2026: páginas impresas 45 y 61 (páginas PDF 58 y 74). Fuente local: `C:/Users/olive/Downloads/2. Anexo al Mensaje.pdf`.

La transcripción en la unidad original (miles de millones de pesos) está en `data/comparativo_pgn_2027.csv`. La presentación divide entre 1.000 para expresar billones. Los totales del PGN son 575,699 y 634,952 billones; la diferencia es 59,253 billones. Se comparan presupuestos completos de la misma vigencia, no los balances fiscales del GNC de las dos imágenes precedentes.

Se preservan dos precisiones de las fuentes: el principal incluye Acuerdos Marco de Retribución (0,490 y 0,990 billones, respectivamente); y en ambos proyectos la suma de los cuatro componentes de deuda excede el total publicado en 0,001 billones. No se modificaron los totales para forzar su coincidencia. El título del cuadro 1.6.6 dice «2025–2026» en ambos documentos, pero las columnas identifican 2026 y Proyecto 2027; se usa la segunda. El párrafo de agosto bajo el cuadro 1.6.1 agrupa incorrectamente intereses y otros rubros: se da prioridad a las cifras coincidentes de ambos cuadros.

## Material inactivo del libro

Se incluyen los 78 archivos de `FiscalBookPresentation/slides`, sus imágenes y una copia exacta de su entrada original (`libro_original.tex`). `modules/04_laberinto.tex` reproduce el cuerpo de esa entrada, incluidos sus `input` comentados. Los bloques `comment` internos también siguen inactivos. No se descomentó ninguna diapositiva. Solo se ajustó el tamaño de la tabla de transferencias (`DesTrans.tex`) y del gráfico de depósitos (`depositos2.tex`) para evitar desbordamientos, sin cambiar texto ni cifras.

Las presentaciones originales de FPC y del libro no se modificaron. Se mantiene el diseño Beamer Singapore/orchid y la relación 16:9. Las series del libro se preservan tal como estaban en la versión fuente; esta integración no constituye una actualización de sus datos.

## Distribución sugerida del tiempo

Los tiempos son una guía para el docente, no aparecen en la proyección.

| Sesión 1 | Minutos |
| --- | ---: |
| Apertura y preguntas iniciales | 5 |
| Ingresos, gastos y financiamiento; discusión de ejemplos | 35 |
| Pausa | 10 |
| Etapas de ejecución, cierre y ejercicio numérico | 45 |
| Cobertura institucional, espejo y convertidor | 20 |
| Plan Financiero 2027, anexos, comparación Petro–Abelardo y conciliación | 35 |
| Clasificación y desagregación del sector público | 5 |
| Dinámica de deuda y regla fiscal | 25 |
| **Total** | **180** |

| Sesión 2 | Minutos |
| --- | ---: |
| Presentación del libro y profundidad del ajuste | 25 |
| Ingresos, recaudo y brecha tributaria | 45 |
| Pausa | 10 |
| Gasto, transferencias y presiones de mediano plazo | 60 |
| Viabilidad política, liquidez y discusión de cierre | 40 |
| **Total** | **180** |

## Precisiones al adaptar FPC

- Se distingue el gasto que reduce patrimonio de la inversión neta en activos no financieros; ambos intervienen en el cálculo del préstamo neto/endeudamiento neto. El balance fiscal no es simplemente el cambio total del patrimonio.
- Se distingue la venta de activos financieros de la de activos no financieros. El caso ISA plantea la clasificación y cobertura sin reproducir las dos afirmaciones contradictorias de FPC sobre su registro histórico.
- Se elimina la afirmación de que únicamente el Congreso puede modificar apropiaciones: el EOP prevé facultades del Gobierno, entre ellas reducir o aplazar bajo condiciones legales.
- Las obligaciones presupuestales no se equiparan automáticamente al gasto fiscal: se explica caja, devengo y caja modificada.
- Los ejemplos nuevos usan cifras hipotéticas, no proyecciones oficiales.

Fuentes de las precisiones: Decreto 111 de 1996 (EOP), MEFP 2014 del FMI y documentación metodológica del MHCP. Las referencias se incluyen en notas `\note{[Sources] ...}` de los archivos LaTeX.

## Adiciones de FPC incorporadas

Las recomendaciones ya están activas: cobertura institucional (`modules/02b_cobertura.tex`), ejercicio de conciliación (`modules/03d_ejercicio_conciliacion.tex`) y cuatro láminas de deuda y regla fiscal (`modules/03e_deuda_regla.tex`). Las fuentes docentes de este último bloque son `FPC_repo/slides/DeudaDinamica.tex` y `FPC_repo/slides/ReglaFiscalPedagogica.tex`; no se modifican los archivos de FPC.

Se acorta el bloque original de once láminas a cuatro, manteniendo las ecuaciones y los ejemplos: deuda inicial 60%, interés nominal 8%, crecimiento nominal 6% y superávit primario 1%; BPNE de -0,5% en el ejemplo de ajustes; meta ordinaria de 0,70% con deuda neta previa de 60%. Los ejemplos se identifican como hipotéticos. La meta ordinaria no se presenta como meta oficial de 2027: se distingue la cláusula de escape y el retorno previsto en el MFMP 2026 a la fórmula desde 2028. Fuentes normativas y metodológicas verificadas: Ley 2155 de 2021, CARF y MHCP, citadas en las notas de cada lámina.

El ejercicio recalcula los balances con los montos originales. Los resultados que difieren en 0,001 billones de la cifra publicada se advierten expresamente; no se alteran las imágenes ni se usan los porcentajes inconsistentes de «PGN Petro». La diferencia del balance total entre las dos versiones de 2027 se descompone en -40,965 billones de ingresos y +63,888 billones de gasto. La resta PGN menos principal (576,680 billones) no se identifica con el gasto fiscal del GNC (529,175): el anexo de agosto, sección 2.4, documenta los ajustes adicionales.

Se redistribuyen los tiempos sugeridos de la primera sesión, manteniendo 180 minutos y el libro completo en la segunda sesión de 180 minutos.

## Compilación

Con Tectonic instalado:

```powershell
./build.ps1
```

O indicando una ruta al ejecutable:

```powershell
./build.ps1 -Tectonic 'C:/ruta/a/tectonic.exe'
```

También se puede abrir `main.tex` en Overleaf y compilar con XeLaTeX. La primera compilación con Tectonic puede necesitar descargar paquetes. Los archivos temporales no se versionan.

## Verificación

Compilación local con Tectonic 0.16.9, sin desbordamientos ni caracteres ausentes. El PDF tiene 78 páginas. Las dos imágenes de los anexos se verifican por SHA-256 y aparecen en 38–39. El comparativo de la página 40 se coteja contra las ocho filas del CSV y sus diferencias calculadas; se comprueban los cálculos de la solución y de los ejemplos de deuda y regla fiscal. También se verifica la identidad textual de las dos láminas de clasificación copiadas de FPC y su presencia en 43–44. El texto de las 30 páginas del libro coincide con el PDF independiente original, excluida la numeración. Los dos cambios de maquetación del libro no alteran sus cifras.

Las siete láminas nuevas se revisaron visualmente a 144 dpi. La comparación de texto e imágenes confirma que las 71 diapositivas anteriores conservan su contenido y diseño; solo cambia su numeración.

La verificación automatizada de estructura, PDF y material inactivo está en `scripts/verify_deck.py` (requiere Python y `pypdf`):

```powershell
python scripts/verify_deck.py
```
