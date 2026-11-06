# 유튜브 자막 수집 (sources.txt에 적은 영상·재생목록·채널)
# 실행: powershell -ExecutionPolicy Bypass -File .\run_subs.ps1
$ErrorActionPreference = "Continue"
Set-Location $PSScriptRoot
New-Item -ItemType Directory -Force -Path ".\subs" | Out-Null
Write-Host "새 채널 영상들의 자막을 받는 중입니다 (5~10분)... 화면이 멈춰 보여도 정상입니다."
.\yt-dlp.exe --skip-download --no-simulate --write-auto-subs --write-subs `
    --sub-langs "ko,ko-orig" --sub-format vtt `
    --ignore-errors --no-warnings --quiet --sleep-requests 1 --sleep-subtitles 2 `
    --playlist-end 30 `
    --print-to-file "%(id)s`t%(upload_date)s`t%(duration)s`t%(channel)s`t%(title)s" "list.tsv" `
    -o "subs/%(id)s.%(ext)s" -a sources.txt
$n = (Get-Content ".\list.tsv" -ErrorAction SilentlyContinue).Count
Write-Host ""
Write-Host "완료: 영상 $n 편을 처리했습니다. Claude에게 알려 주세요."
Read-Host "엔터를 누르면 창이 닫힙니다"
