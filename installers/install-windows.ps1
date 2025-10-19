# EASY Language Installer for Windows
# Requires PowerShell 5.0 or higher

$ErrorActionPreference = "Stop"

Write-Host "╔════════════════════════════════════╗" -ForegroundColor Blue
Write-Host "║  EASY Language Installer v1.0      ║" -ForegroundColor Blue
Write-Host "╚════════════════════════════════════╝" -ForegroundColor Blue
Write-Host ""

# Check Python installation
try {
    $pythonVersion = & python --version 2>&1
    Write-Host "✓ Found $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Python 3 is required but not found." -ForegroundColor Red
    Write-Host "Please install Python from https://www.python.org/downloads/" -ForegroundColor Yellow
    Write-Host "Make sure to check 'Add Python to PATH' during installation!" -ForegroundColor Yellow
    pause
    exit 1
}

# Installation directory
$installDir = "$env:LOCALAPPDATA\EasyLang"
$scriptsDir = "$env:LOCALAPPDATA\Microsoft\WindowsApps"

Write-Host ""
Write-Host "Installing to: $installDir" -ForegroundColor Cyan

# Create installation directory
New-Item -ItemType Directory -Force -Path $installDir | Out-Null

# Copy interpreter files
Write-Host "Copying EASY interpreter files..." -ForegroundColor Cyan
Copy-Item -Path "easy\*" -Destination $installDir -Recurse -Force

# Create easy.cmd wrapper
$easyCmdContent = @"
@echo off
python "$installDir\easy.py" %*
"@

$easyCmdContent | Out-File -FilePath "$scriptsDir\easy.cmd" -Encoding ASCII

# Create easy-shell.cmd wrapper
$easyShellContent = @"
@echo off
set PYTHONPATH=$installDir;%PYTHONPATH%
python "$installDir\..\misc\shell.py"
"@

# Copy shell.py to installation directory
Copy-Item -Path "misc\shell.py" -Destination $installDir -Force

$easyShellContent | Out-File -FilePath "$scriptsDir\easy-shell.cmd" -Encoding ASCII

Write-Host ""
Write-Host "╔════════════════════════════════════╗" -ForegroundColor Green
Write-Host "║  Installation Complete!            ║" -ForegroundColor Green
Write-Host "╚════════════════════════════════════╝" -ForegroundColor Green
Write-Host ""
Write-Host "EASY has been installed successfully!" -ForegroundColor Green
Write-Host ""
Write-Host "Commands available:" -ForegroundColor Cyan
Write-Host "  easy       - Run EASY programs" -ForegroundColor White
Write-Host "  easy-shell - Interactive EASY shell" -ForegroundColor White
Write-Host ""
Write-Host "Try it out:" -ForegroundColor Yellow
Write-Host '  echo say("Hello, EASY!") > test.esy' -ForegroundColor White
Write-Host "  easy test.esy" -ForegroundColor White
Write-Host ""
pause
