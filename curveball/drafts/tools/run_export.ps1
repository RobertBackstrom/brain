# run_export.ps1 - drive export_blueprints.py headless on forge (WP0.3).
# Usage (elevated not required):
#   powershell -File D:\Curveball\Tools\run_export.ps1 -Scope priority
#   powershell -File D:\Curveball\Tools\run_export.ps1 -Scope all -Fresh

param(
    [ValidateSet("priority", "all")] [string]$Scope = "priority",
    [string]$Engine  = "D:\UE\UnrealEngine",
    [string]$Project = "D:\Curveball\BBA\olle_dev\BladeBallArena.uproject",
    [string]$OutDir  = "D:\Curveball\BlueprintExports",
    [string]$Script  = "D:\Curveball\Tools\export_blueprints.py",
    [switch]$Fresh   # ignore existing exports instead of resuming
)

$ErrorActionPreference = "Stop"

$editor = Join-Path $Engine "Engine\Binaries\Win64\UnrealEditor-Cmd.exe"
foreach ($p in @($editor, $Project, $Script)) {
    if (-not (Test-Path $p)) { throw "missing: $p" }
}

$env:CVB_EXPORT_DIR = $OutDir
$env:CVB_SCOPE      = $Scope
$env:CVB_RESUME     = if ($Fresh) { "0" } else { "1" }

New-Item -ItemType Directory -Force -Path $OutDir | Out-Null
$log = Join-Path $OutDir ("_run_{0}.log" -f (Get-Date -Format "yyyyMMdd-HHmmss"))

Write-Host "editor : $editor"
Write-Host "project: $Project"
Write-Host "scope  : $Scope (resume=$($env:CVB_RESUME))"
Write-Host "log    : $log"

# -NoShaderCompile keeps a text export from burning an hour on shaders it will never use.
$args = @(
    "`"$Project`"",
    "-run=pythonscript",
    "-script=`"$Script`"",
    "-unattended", "-nosplash", "-nopause", "-NoShaderCompile",
    "-stdout", "-FullStdOutLogOutput"
)

$started = Get-Date
& $editor @args *>&1 | Tee-Object -FilePath $log
$code = $LASTEXITCODE

Write-Host ("exit={0} elapsed={1}" -f $code, ((Get-Date) - $started))
$summary = Join-Path $OutDir "_summary.json"
if (Test-Path $summary) { Get-Content $summary }
exit $code
