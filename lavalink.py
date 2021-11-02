from os import getenv, system
#from subprocess import Popen
from urllib.request import urlretrieve
from re import sub

print("[INFO] Changing the port ...")
try:
    temp = open('application.yml', 'r').read()
    temp = sub('REPLACEPORT', getenv('PORT'), temp)
    temp = sub('REPLACEPASSWORD', getenv('PASSWORD'), temp)
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
    system('java -jar Lavalink.jar -Xmx250m -Xms250m -XX:+UseContainerSupport -XX:CICompilerCount=4 -Dfile.encoding=UTF-8 -XX:+AggressiveOpts')
except:
    print(f"[ERROR] Failed to start Lavalink server... Info: {exc}")
