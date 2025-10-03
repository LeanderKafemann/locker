print("Herzlich Willkommen beim Locker-Installer!")
__version__ = "1.0.0"

name = input("Dein Windows-Nutzername: ")
pwd = input("Passwort eingeben: ")
pwd2 = input("Passwort wiederholen: ")
while pwd != pwd2:
    print("Falsche Eingabe.")
    pwd2 = input("Passwort wiederholen: ")

with open("./script_template.bat", "r", encoding="utf-8") as f:
    script = f.read()
with open(f"C:\\Users\\{name}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\openPythonLocker.bat", "w", encoding="utf-8") as g:
    g.write(script.format(name))

with open("./password.txt", "w", encoding="utf-8") as f:
    f.write(pwd)
with open("./secured.txt", "w", encoding="utf-8") as f:
    f.write("0")

print("\nProgramm erfolgreich installiert.")
input()