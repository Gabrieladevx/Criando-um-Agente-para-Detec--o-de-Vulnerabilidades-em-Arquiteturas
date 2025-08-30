# start_all.ps1
# Inicia as apps vulneráveis em background usando o python do venv.
# Uso: execute na raiz do repositório: .\start_all.ps1

$python = Join-Path $PSScriptRoot ".\.venv\Scripts\python.exe"
if (-not (Test-Path $python)) {
    Write-Error "python do venv não encontrado em $python. Ative o venv ou crie-o com: python -m venv .venv"
    exit 1
}

$apps = @(
    @{ Name='sql_injection'; Script='app_vulneravel/sql_injection/app.py'; Port=5001 },
    @{ Name='xss'; Script='app_vulneravel/xss/app.py'; Port=5002 },
    @{ Name='auth_fraca'; Script='app_vulneravel/auth_fraca/app.py'; Port=5003 },
    @{ Name='config_insegura'; Script='app_vulneravel/config_insegura/app.py'; Port=5004 }
)

$log = Join-Path $PSScriptRoot "start_all.log"
"=== start_all.ps1 log - $(Get-Date -Format o) ===" | Out-File $log -Encoding utf8

foreach ($app in $apps) {
    $scriptPath = Join-Path $PSScriptRoot $app.Script
    if (-not (Test-Path $scriptPath)) {
        "[ERROR] Script não encontrado: $scriptPath" | Add-Content $log
        continue
    }
    # checar porta
    $conn = Get-NetTCPConnection -LocalPort $app.Port -ErrorAction SilentlyContinue
    if ($conn) {
        "[SKIP] Porta $($app.Port) já em uso. Pulando $($app.Name)." | Add-Content $log
        continue
    }
    try {
        $proc = Start-Process -FilePath $python -ArgumentList $scriptPath -PassThru -WindowStyle Minimized
        "[STARTED] $($app.Name) (PID $($proc.Id)) -> $scriptPath" | Add-Content $log
        Start-Sleep -Milliseconds 500
    } catch {
        "[ERROR] Falha ao iniciar $($app.Name): $_" | Add-Content $log
    }
}

"=== done at $(Get-Date -Format o) ===" | Add-Content $log
Write-Output "Done. See $log for details."
