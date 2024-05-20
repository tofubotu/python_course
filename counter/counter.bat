@echo off
setlocal enabledelayedexpansion

set counter=1

:loop
echo !counter!
set /a counter+=1
timeout /t 1 >nul
goto loop