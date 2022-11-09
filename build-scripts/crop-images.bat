:: Crops/converts a folder of images. Outputs into another folder
:: Arguments [src-folder] [dest-folder]

@echo off
setlocal enabledelayedexpansion

set srcfolder=%1
set destfolder=%2

echo *START* [Cropping images]
echo = From folder '%srcfolder%' to folder '%destfolder%'

@for %%f in (%srcfolder%\*) do @(
    set srcfile=%%~f
    set destfile=%destfolder%\%%~nf.jpg
    @echo Crop: !srcfile! !destfile!
    magick !srcfile! -resize 96x96^ -gravity center -extent 96x96 !destfile!
)

echo *COMPLETE* [Cropping images]

@echo on