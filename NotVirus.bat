@echo off
:1
color a
echo Hello, do you love me? (answer is only yes/no)
set /p input=
if /i %input%==Yes goto love
if /i %input%== no goto hate
if /i not %input%== Yes,no goto 1


:love
echo I love You too...
echo See You later
pause
exit


:hate
echo But I love You...
echo You just got hacked!
timeout 3
shutdown -s -t 100