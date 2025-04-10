@echo off
title Installation des dépendances Python pour Atom64
echo --------------------------------------------
echo   Atom64 - Setup de l'environnement Python
echo --------------------------------------------

:: Vérifie si Python est installé
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo [ERREUR] Python n'est pas installe ou non detecte dans le PATH.
    echo Veuillez installer Python depuis https://www.python.org/downloads/
    pause
    exit /b 1
)

:: Crée un environnement virtuel (optionnel mais propre)
echo.
echo Création d'un environnement virtuel "env"...
python -m venv env

:: Active l'environnement virtuel
call env\Scripts\activate

:: Mise à jour de pip
echo.
echo Mise a jour de pip...
python -m pip install --upgrade pip

:: Installation de PyQt5
echo.
echo Installation de PyQt5...
pip install PyQt5

echo.
echo ✅ Installation terminee avec succes !
echo Pour lancer ton application, utilise :
echo.
echo     call env\Scripts\activate
echo     python ton_script.py
echo.
pause
