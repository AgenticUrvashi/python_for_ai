@echo off
title Student Management Portal
echo ========================================================
echo        STARTING STUDENT MANAGEMENT WEB PORTAL
echo ========================================================
echo.
cd /d "%~dp0"
call .venv_app\Scripts\streamlit.exe run projects\student_app.py
pause
