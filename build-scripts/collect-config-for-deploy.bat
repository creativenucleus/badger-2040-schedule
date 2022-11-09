:: Crops/converts a folder of images. Outputs into another folder
:: Arguments [src-folder] [dest-folder]

@echo off
setlocal enabledelayedexpansion

set srcfolder=%1
set destfolder=%2

echo *START* [Collect config for deploy]
echo = From folder '%srcfolder%' to folder '%destfolder%'

copy %srcfolder%\config.py %destfolder%\config.py

echo *COMPLETE* [Collect config for deploy]

@echo on
