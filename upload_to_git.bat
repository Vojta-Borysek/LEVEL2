@echo off
REM ------------------------------
REM Upload celého projektu na GitHub s vlastním commitem
REM ------------------------------

REM Nastav GitHub repozitář
SET REPO_URL=https://github.com/Vojta-Borysek/LEVEL2.git

REM Inicializace git repozitáře, pokud ještě není
IF NOT EXIST ".git" (
    git init
)

REM Přidání všech souborů
git add .

REM Zeptáme se uživatele na commit zprávu
set /p COMMIT_MSG=Zadej commit zpravu:

REM Commit s vlastní zprávou
git commit -m "%COMMIT_MSG%" 2>nul

REM Přepnutí/pojmenování hlavní větve
git branch -M main

REM Přidání remote (přepíše existující origin, pokud je)
git remote remove origin 2>nul
git remote add origin %REPO_URL%

REM Push na GitHub
git push -u origin main

echo.
echo --------------------------------
echo Upload dokoncen s commit zpravou: %COMMIT_MSG%
echo --------------------------------
pause
