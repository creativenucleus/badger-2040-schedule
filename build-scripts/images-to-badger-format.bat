:: Converts a folder of images into Badger .bin format. Outputs into another folder
:: Arguments [src-folder] [dest-folder] [convert-script-folder]

@echo off
setlocal enabledelayedexpansion

set srcfolder=%1
set destfolder=%2
set codefolder=%3

echo *START* [Images to Badger format]
echo = From folder '%srcfolder%' to folder '%destfolder%'

@for %%f in (%srcfolder%\*) do @(
    set srcfile=%%~f
    @echo Convert: !srcfile! into folder %destfolder%
    python3 %codefolder%\convert.py --binary !srcfile! --out_dir %destfolder%
)

echo *COMPLETE* [Images to Badger format]

@echo on
