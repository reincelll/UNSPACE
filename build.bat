@echo off
python -m PyInstaller ^
  main.py ^
  --name UNSPACE ^
  --onefile ^
  --windowed ^
  --icon=icon.ico ^
  --collect-all raylibpy ^
  --add-data "assets;assets" ^
  --add-data "data;data"

pause