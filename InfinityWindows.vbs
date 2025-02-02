do
Set wshshell = wscript.CreateObject("WScript.Shell")
Wshshell.run "Notepad"
wscript.sleep 100
wshshell.sendkeys "V"
wscript.sleep 100
wshshell.sendkeys "I"
wscript.sleep 100
wshshell.sendkkeys "R"
wscript.sleep 100
wshshell.sendkeys "U"
wscript.sleep 100
wshshell.sendkeys "S"
wscript.sleep 100
wshshell.sendkeys "!"
loop