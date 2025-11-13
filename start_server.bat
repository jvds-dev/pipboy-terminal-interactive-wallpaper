@echo off
title Lively Server
color 0A
cd /d "%~dp0"
echo ===============================
echo Iniciando servidor Lively...
echo ===============================
call venv\Scripts\activate
python server.py
echo.
echo Servidor encerrado.
pause
