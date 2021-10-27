from os import getenv, system


class lavalinkserver:
    def __init__(self):
        self.download_command = "wget -qi https://github.com/freyacodes/Lavalink/releases/download/3.4/Lavalink.jar"
        self.change_port = 'sed -i "s|DYNAMICPORT|{}|" application.yml'.format(getenv('PORT'))
        #self.change_password = 'sed -i "s|DYNAMICPASSWORD||" application.yml'
        #self.no_password = 'sed -i "s|DYNAMICPASSWORD|youshallnotpass|" application.yml'
        #self.additional = environ.get("ADDITIONAL_JAVA_OPTIONS")
        self.run_command = "java -jar Lavalink.jar"

    def password_and_port(self):
        print("[INFO] Changing the port ...")
        try:
            system(self.change_port)
        except BaseException as exc:
            print(f"[ERROR] Error changing port ... Info: {exc}")
        else:
            print("[INFO] Successfully changed Port and Password...")

    def download(self):
        print("[INFO] Downloading Latest Lavalink ...")
        try:
            system(self.download_command)
        except BaseException as exc:
            print(f"[ERROR] Error downloading Lavalink... Info: {exc}")
        else:
            print("[INFO] Success in downloading Lavalink...")
    
    def run(self):
        self.download()
        self.password_and_port()
        print("[INFO] Starting lavalink.")
        try:
            system(self.run_command)
        except BaseException as exc:
            print(f"[ERROR] Failed to start Lavalink server... Info: {exc}")

if __name__ == "__main__":
   lavalinkserver().run()

