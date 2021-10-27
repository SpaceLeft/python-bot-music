from os import getenv, system
import urllib.request
import re


print("[INFO] Changing the port ...")
try:
    temp = open('application.yml', 'r').read()
    temp = re.sub('DYNAMICPORT', getenv('PORT'), temp)
    open('application.yml', 'w').write(temp)
except BaseException as exc:
    print(f"[ERROR] Error changing port ... Info: {exc}")
else:
    print("[INFO] Successfully changed Port and Password...")

print("[INFO] Downloading Latest Lavalink ...")
try:
    urllib.request.retrieve("https://github.com/freyacodes/Lavalink/releases/download/3.4/Lavalink.jar", filename='Lavalink.jar')
except BaseException as exc:
    print(f"[ERROR] Error downloading Lavalink... Info: {exc}")
else:
    print("[INFO] Success in downloading Lavalink...")
    
try:
    system('java -jar Lavalink.jar')
except:
    print(f"[ERROR] Failed to start Lavalink server... Info: {exc}")
