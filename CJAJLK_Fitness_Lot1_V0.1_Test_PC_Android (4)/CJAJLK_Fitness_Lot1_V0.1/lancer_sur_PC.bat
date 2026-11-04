@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo CJAJLK Fitness - Lot 1
where py >nul 2>nul
if %errorlevel%==0 (
  start "Serveur local CJAJLK Fitness" cmd /k "py -3 -m http.server 8080"
  timeout /t 2 /nobreak >nul
  start "" "http://localhost:8080"
  goto :eof
)
where python >nul 2>nul
if %errorlevel%==0 (
  start "Serveur local CJAJLK Fitness" cmd /k "python -m http.server 8080"
  timeout /t 2 /nobreak >nul
  start "" "http://localhost:8080"
  goto :eof
)
echo Python n'est pas installe. Installer Python ou publier l'application sur un hebergement HTTPS.
pause
