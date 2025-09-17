@echo off
set TARGET_DIR=DIRECTORY_WHERE_SCRIPT_IS
set START_ENV_CMD=call .\venv\Scripts\Activate
set RUN_CMD=python .\cppserver_killer.py
start cmd /c "cd /d %TARGET_DIR% && %START_ENV_CMD% && %RUN_CMD% && pause"