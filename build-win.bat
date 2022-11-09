@echo off

echo *START* [Building Assets for Badger]

:: Set up a clean deploy folder and temporary directories
rmdir .\_deploy /s /Q
mkdir .\_deploy
mkdir .\_deploy\schedule
mkdir .\_deploy\schedule\images
mkdir .\_temp

call build-scripts\crop-images.bat .\config\images _temp
call build-scripts\images-to-badger-format.bat .\_temp .\_deploy\schedule\images .\external-code
call build-scripts\collect-config-for-deploy.bat .\config .\_deploy\schedule

:: Clean away the temporary directory
rmdir .\_temp /s /Q

echo *COMPLETE* [Building Assets for Badger]

@echo on