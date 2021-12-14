import platform
import os
import webbrowser
from platform import system
from time import sleep

from core import HackingToolsCollection
from tools.anonsurf import AnonSurfTools
from tools.ddos import DDOSTools
from tools.exploit_frameworks import ExploitFrameworkTools
from tools.forensic_tools import ForensicTools
from tools.information_gathering_tools import InformationGatheringTools
from tools.other_tools import OtherTools
from tools.payload_creator import PayloadCreatorTools
from tools.phising_attack import PhishingAttackTools
from tools.post_exploitation import PostExploitationTools
from tools.remote_administration import RemoteAdministrationTools
from tools.reverse_engineering import ReverseEngineeringTools
from tools.sql_tools import SqlInjectionTools
from tools.steganography import SteganographyTools
from tools.tool_manager import ToolManager
from tools.webattack import WebAttackTools
from tools.wireless_attack_tools import WirelessAttackTools
from tools.wordlist_generator import WordlistGeneratorTools
from tools.xss_attack import XSSAttackTools

all_tools = [
    AnonSurfTools(),
    InformationGatheringTools(),
    WordlistGeneratorTools(),
    WirelessAttackTools(),
    SqlInjectionTools(),
    PhishingAttackTools(),
    WebAttackTools(),
    PostExploitationTools(),
    ForensicTools(),
    PayloadCreatorTools(),
    ExploitFrameworkTools(),
    ReverseEngineeringTools(),
    DDOSTools(),
    RemoteAdministrationTools(),
    XSSAttackTools(),
    SteganographyTools(),
    OtherTools(),
    ToolManager()
]


logo = """\033[33m
     _   __                 _                _   _       _     
    | | / /                | |              | | | |     | |    
    | |/ / _ __ _   _ _ __ | |_ ___  _ __   | |_| |_   _| |__  
    |    \| '__| | | | '_ \| __/ _ \| '_ \  |  _  | | | | '_ \ 
    | |\  \ |  | |_| | |_) | || (_) | | | | | | | | |_| | |_) |
    \_| \_/_|   \__, | .__/ \__\___/|_| |_| \_| |_/\__,_|_.__/ 
                 __/ | |                                       
                |___/|_|                                       
\033[97m """


class AllTools(HackingToolsCollection):
    TITLE = "All tools"
    TOOLS = all_tools

    def show_info(self):
        print(logo + '\033[0m \033[97m')

# --------------------------------------------------------------------------------------
if __name__ == "__main__":
    try:
        if system() == 'Linux':
            fpath = "/home/kryptonhubpath.txt"
            if not os.path.exists(fpath):
                os.system('clear')
                # run.menu()
                print("""
                        [@] Set Path (All your tools will be installed in that directory)
                        [1] Manual 
                        [2] Default
                """)
                choice = input("Krypton >> ")

                if choice == "1":
                    inpath = input("Enter Path (with Directory Name) >> ")
                    with open(fpath, "w") as f:
                        f.write(inpath)
                    print(f"Successfully Set Path to: {inpath}")
                elif choice == "2":
                    autopath = "/home/kryptonhub/"
                    with open(fpath, "w") as f:
                        f.write(autopath)
                    print(f"Your Default Path Is: {autopath}")
                    sleep(3)
                else:
                    print("Try Again..!!")
                    exit(0)

            with open(fpath) as f:
                archive = f.readline()
                if not os.path.exists(archive):
                    os.mkdir(archive)
                os.chdir(archive)
                all_tools = AllTools()
                all_tools.show_options()

        elif system() == "Windows":
            print(
                "\033[91m Please Run This Tool On A Debian System For Best Results " "\e[00m")
            sleep(2)

        else:
            print("Please Check Your System!")

    except KeyboardInterrupt:
        print("\nExiting ..!!!")
        sleep(2)

# --------------------------------------------------------------------------------------


def main_menu():
    os.system("clear")
    logo()
    print("\n")
    print("        \033[34m[✔]                 Version 1.1.0                [✔]")
    print("        \033[91m[X]     Please Don't Use For illegal Activity     [X]")
    print("        \033[91m[X]  I'm not responsible for any damage you make! [X]\033[97m")
    print("\n\n-------------------------------------------")
    print("| Show IP address (0)                     |")
    print("| Show Wireless Network Devices (1)       |")
    print("| Ping Attack (2)                         |")
    print("| Tools (10)                              |")
    print("-------------------------------------------")
    print("| Exit (99)                               |")
    print("-------------------------------------------")
    command = int(input("Command: "))
    if command == 0:
        os.system("clear")
        os.system("ifconfig")
        back_to_main()
    elif command == 1:
        os.system("clear")
        os.system("iwconfig")
        back_to_main()
    elif command == 2:
        print("Sorry, Currently now available!")
        back_to_main()
    elif command == 10:
        tools()
    elif command == 99:
        print("\nExiting...")
        sleep(1)
        os.system("clear")
        exit()
    else:
        wrong_choice()


def tools():
    os.system("clear")
    logo()
    print("\n\n-------------------------------------------")
    print("| (0) Information Gathering")
    print("| (1) Wireless attacks")
    print("| (2) SQL Injection tools")
    print("| (3) DDOS tools")
    print("-------------------------------------------")
    print("| (99) Back To Main Menu")
    print("-------------------------------------------")
    command = int(input("Command: "))
    if command == 99:
        main_menu()


def ping_attack():
    os.system("clear")
    logo()
    print("\n")
    ipaddr = input("\nTarget Url/Ip: ")
    os.system("clear")
    logo()
    print("\n")
    time = input("\nSet Amount: ")
    os.system("clear")
    logo()
    print("\n")
    count = input("\nSet Count: ")
    os.system("clear")
    logo()
    print("\n")
    print("-------------------------------------------")
    print("| Target: {}".format(ipaddr))
    print("| Amount: {}".format(time))
    print("| Count: {}".format(count))
    print("-------------------------------------------")
    print("\n")
    question_for_attack()


def begin_attack():
    os.system("clear")
    logo()
    print("\n")
    print("Begin Attack...")
    sleep(1)
    os.system("clear")
    logo()
    print("\n")
    # os.system("ping  {}  ".format())


def question_for_attack():
    start_ping = input("Do you want to begin the attack? (y/n): ")
    if start_ping != "":
        if start_ping == "y" or start_ping == "Y":
            begin_attack()
        elif start_ping == "n" or start_ping == "N":
            main_menu()
    else:
        print("\nWrong choice!")
        question_for_attack()


def back_to_main():
    back = input("\nDo you want to go back? (y/n): ")
    if back != "":
        if back == "y" or back == "Y":
            main_menu()
        if back == "n" or back == "N":
            print("\nExiting...")
            sleep(1)
            exit()
    else:
        wrong_choice()


def wrong_choice():
    print("\nWrong choice!")
    sleep(2)
    main_menu()


def diagnostic():
    sysOS = platform.system()

    if sysOS == "Linux":
        os.system("clear")
    if sysOS == "Windows":
        os.system("cls")

    logo()
    print("\n")
    print("\nDetecting System...")
    sleep(1)
    print("System detected: ", sysOS)
    sleep(1)

    if sysOS == "Linux":
        main_menu()
    else:
        print("\n           \033[91m[X] Your system is not Linux, You may not be able to run this script in some systems [X]\033[97m")


def tool_install_run():
    logo()
    print("\n\n-------------------------------------------")
    print("| (0) Install")
    print("| (1) Run")
    print("-------------------------------------------")
    print("| (99) Back")
    print("-------------------------------------------")
    command = int(input("Command: "))
    if command == 99:
        tools()
