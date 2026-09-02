param([string]$Tectonic = 'tectonic')
$ErrorActionPreference = 'Stop'
Push-Location $PSScriptRoot
try {
    New-Item -ItemType Directory -Force -Path 'tmp/latex', 'output/pdf' | Out-Null
    & $Tectonic --keep-logs --keep-intermediates --outdir 'tmp/latex' 'main.tex'
    if ($LASTEXITCODE -ne 0) { throw 'La compilación de LaTeX falló.' }
    Copy-Item -LiteralPath 'tmp/latex/main.pdf' -Destination 'output/pdf/Curso_PGN.pdf' -Force
    Write-Output (Join-Path $PSScriptRoot 'output/pdf/Curso_PGN.pdf')
} finally { Pop-Location }
