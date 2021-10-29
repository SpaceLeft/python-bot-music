from os import getenv
from subprocess import Popen
from urllib.request import urlretrieve
from re import sub

print("[INFO] Changing the port ...")
try:
    temp = open('application.yml', 'r').read()
    temp = sub('DYNAMICPORT', getenv('PORT'), temp)
    open('application.yml', 'w').write(temp)
except BaseException as exc:
    print(f"[ERROR] Error changing port ... Info: {exc}")
else:
    print("[INFO] Successfully changed Port and Password...")

print("[INFO] Downloading Latest Lavalink ...")
try:
    urlretrieve("https://github.com/freyacodes/Lavalink/releases/download/3.4/Lavalink.jar", filename='Lavalink.jar')
except BaseException as exc:
    print(f"[ERROR] Error downloading Lavalink... Info: {exc}")
else:
    print("[INFO] Success in downloading Lavalink...")
    
try:
    Popen('java -jar Lavalink.jar', shell=True)
except:
    print(f"[ERROR] Failed to start Lavalink server... Info: {exc}")
