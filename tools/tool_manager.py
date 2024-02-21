# coding=utf-8
import os
from time import sleep

from core import KryptonHub
from core import HackingToolsCollection


class UpdateTool(KryptonHub):
    TITLE = "Update Tool or System"
    DESCRIPTION = "Update Tool or System"

    def __init__(self):
        super(UpdateTool, self).__init__([
            ("Update System", self.update_sys),
            ("Update KryptonHub", self.update_kh)
        ], installable = False, runnable = False)

    @staticmethod
    def update_sys(self):
        os.system("sudo apt update && sudo apt full-upgrade -y")
        os.system(
            "sudo apt-get install tor openssl curl && sudo apt-get update tor openssl curl")
        os.system("sudo apt-get install python3-pip")

    @staticmethod
    def update_kh(self):
        os.system("sudo chmod +x /etc/;"
                  "sudo chmod +x /usr/share/doc;"
                  "sudo rm -rf /usr/share/doc/krypton-hub/;"
                  "cd /etc/;"
                  "sudo rm -rf /etc/krypton-hub/;"
                  "mkdir krypton-hub;"
                  "cd krypton-hub;"
                  "git clone https://github.com/attilapeterszucs/krypton-hub.git;"
                  "cd krypton-hub;"
                  "sudo chmod +x install.sh;"
                  "bash install.sh")


class UninstallTool(KryptonHub):
    TITLE = "Uninstall Krypton-Hub"
    DESCRIPTION = "Uninstall Krypton-Hub"

    def __init__(self):
        super(UninstallTool, self).__init__([
            ('Uninstall', self.uninstall)
        ], installable = False, runnable = False)

    def uninstall(self):
        print("Krypton-Hub started to uninstall..\n")
        sleep(1)
        os.system("sudo chmod +x /etc/;"
                  "sudo chmod +x /usr/share/doc;"
                  "sudo rm -rf /usr/share/doc/krypton-hub/;"
                  "cd /etc/;"
                  "sudo rm -rf /etc/krypton-hub/;")
        print("\nKrypton-Hub Successfully Uninstalled..")
        print("Happy Hacking..!!")
        sleep(1)


class ToolManager(HackingToolsCollection):
    TITLE = "Update or Uninstall | Krypton-Hub"
    TOOLS = [
        UpdateTool(),
        UninstallTool()
    ]
