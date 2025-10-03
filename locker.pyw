#proto_agent
import pyautogui as py
import datetime, os

__version__ = "1.0.0"

with open("./secured.txt", "r") as r:
    x = int(r.read())
locked = False
if x > 0:
    x -= 1
    locked = True
with open("./secured.txt", "w") as r:
    r.write(str(x))

#Protokoll
with open("./proto.txt", "a") as p:
    p.write(str(datetime.datetime.today()))
    p.write("\n"+str(locked)+";"+str(x)+"\n")

#Locker
if locked:
    os.system('shutdown /s /t 10 /c "Die Benutzeroberfläche wurde gesperrt. Sie haben keine Zugriffsberechtigung."')
    with open("./password.txt", "r", encoding="utf-8") as f:
        pwd = f.read()
    if py.password("Rettungscode", "!!!") == pwd:
        os.system("shutdown /a")
        py.alert("Verificated.")
else:
    py.alert("Not locked.")
