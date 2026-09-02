# Curso de Presupuesto General de la Nación

Oliver Pardo · Septiembre de 2026 · Dos sesiones de tres horas.

La presentación editable está en `main.tex`. El PDF se publica en `output/pdf/Curso_PGN.pdf`.

El PDF contiene **66 diapositivas**: sesión 1, páginas 1–36; sesión 2, páginas 37–66. Los tres diagramas solicitados están en las páginas 34–36.

## Contenido

1. Ingresos, gastos y financiamiento: adaptación del curso FPC, con sus ejemplos de crédito, amortización, intereses, hipoteca y venta de activos.
2. Apropiaciones, compromisos, obligaciones y pagos: adaptación de FPC, complementada con CDP, RP, PAC, reservas, cuentas por pagar y un ejercicio resuelto.
3. Tres láminas consecutivas con idéntica estructura: espejo entre contabilidad presupuestal y fiscal; convertidor; convertidor como caja negra.
4. Presentación completa de *El laberinto fiscal de Colombia*: las 30 diapositivas activas de la versión independiente, en su orden original.

## Material inactivo del libro

Se incluyen los 78 archivos de `FiscalBookPresentation/slides`, sus imágenes y una copia exacta de su entrada original (`libro_original.tex`). `modules/04_laberinto.tex` reproduce el cuerpo de esa entrada, incluidos sus `input` comentados. Los bloques `comment` internos también siguen inactivos. No se descomentó ninguna diapositiva. Solo se ajustó el tamaño de la tabla de transferencias (`DesTrans.tex`) y del gráfico de depósitos (`depositos2.tex`) para evitar desbordamientos, sin cambiar texto ni cifras.

Las presentaciones originales de FPC y del libro no se modificaron. Se mantiene el diseño Beamer Singapore/orchid y la relación 16:9. Las series del libro se preservan tal como estaban en la versión fuente; esta integración no constituye una actualización de sus datos.

## Distribución sugerida del tiempo

Los tiempos son una guía para el docente, no aparecen en la proyección.

| Sesión 1 | Minutos |
| --- | ---: |
| Apertura y preguntas iniciales | 10 |
| Ingresos, gastos y financiamiento; discusión de ejemplos | 65 |
| Pausa | 10 |
| Etapas de ejecución, cierre y ejercicio numérico | 70 |
| Espejo, convertidor y discusión sobre conciliación | 25 |
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

## Otras diapositivas de FPC recomendadas

No se activaron bloques adicionales, para mantener la selección solicitada y dejar tiempo para discusión. En orden de prioridad:

1. **Cobertura institucional: PGN, GNC y gobierno general.** Una lámina antes del convertidor aclararía por qué no se pueden comparar directamente sus totales.
2. **Los dos cuadros comparativos de balance fiscal 2026–2027.** Un caso práctico para identificar versiones, supuestos y reclasificaciones; 2026 y 2027 deben señalarse como proyecciones. Se necesitaría explicar la versión y el origen de cada columna, no tratarlas como cifras observadas.
3. **Dinámica de la deuda y regla fiscal.** Tres o cuatro láminas antes del libro para explicar la necesidad de balance primario y cómo se restringe el espacio presupuestal.

Si se incorporan, conviene sustituir parte de la exposición por el ejercicio con los cuadros, no simplemente aumentar el número de láminas.

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

Compilación local con Tectonic 0.16.9, sin desbordamientos ni caracteres ausentes. Se renderizaron y revisaron las 66 páginas. El texto de las 30 páginas del libro coincide con el PDF independiente original, excluida la numeración. Los dos cambios de maquetación no alteran sus cifras.

La verificación automatizada de estructura, PDF y material inactivo está en `scripts/verify_deck.py` (requiere Python y `pypdf`):

```powershell
python scripts/verify_deck.py
```
