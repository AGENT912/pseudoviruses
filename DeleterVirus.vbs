MsgBox "Your computer was hacked"
Set wshShell =wscript.CreatObjet("WScript.Shell")
do
wscript.sleep 100
wshell.sendkeys "{bs}"
loop