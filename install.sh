#!/bin/bash
clear

BLACK='\e[30m'
RED='\e[31m'
GREEN='\e[92m'
YELLOW='\e[33m'
ORANGE='\e[93m'
BLUE='\e[34m'
PURPLE='\e[35m'
CYAN='\e[36m'
WHITE='\e[37m'
NC='\e[0m'
purple='\033[35m'

echo " _   __                 _                _   _       _     "
echo "| | / /                | |              | | | |     | |    "
echo "| |/ / _ __ _   _ _ __ | |_ ___  _ __   | |_| |_   _| |__  "
echo "|    \| '__| | | | '_ \| __/ _ \| '_ \  |  _  | | | | '_ \ "
echo "| |\  \ |  | |_| | |_) | || (_) | | | | | | | | |_| | |_) |"
echo "\_| \_/_|   \__, | .__/ \__\___/|_| |_| \_| |_/\__,_|_.__/ "
echo "             __/ | |                                       "
echo "            |___/|_|                                       "
echo ""
echo -e "${RED}[!] You Have to Run This Tool As Root [!]${NC}"
echo ""
echo -e ${CYAN}"Select Operating System: "
echo ""
echo -e "${WHITE}        [1] Kali Linux / Parrot-Os "
echo -e "${WHITE}        [0] Exit "
echo ""
echo -n -e "Krypton >> "
read choice

INSTALL_DIR="/usr/share/doc/krypton-hub"
BIN_DIR="/usr/bin/"
if [ $choice == 1 ]; then 
	echo "[*] Checking Internet Connection .."
	wget -q --tries=10 --timeout=20 --spider https://google.com
	if [[ $? -eq 0 ]]; then
	    echo -e ${BLUE}"[✔] Loading ... "
	    sudo apt-get update && apt-get upgrade 
	    sudo apt-get install python-pip
	    echo "[✔] Checking directories..."
	    if [ -d "$INSTALL_DIR" ]; then
	        echo "[!] A Directory krypton-hub Was Found.. Do You Want To Replace It ? [y/n]:" ;
	        read input
	        if [ "$input" = "y" ]; then
	            rm -R "$INSTALL_DIR"
	        else
	            exit
	        fi
	    fi
    		echo "[✔] Installing ...";
		echo "";
		git clone https://github.com/JustKKrypton/krypton-hub.git "$INSTALL_DIR";
		echo "#!/bin/bash
		python3 $INSTALL_DIR/Krypton-Hub.py" '${1+"$@"}' > kryptonhub;
		sudo chmod +x hackingtool;
		sudo cp hackingtool /usr/bin/;
		rm krypton-hub;
		echo ""; 
		echo "[✔] Trying to installing Requirements ..."
		sudo pip3 install lolcat
		sudo apt-get install -y figlet
		sudo pip3 install boxes
		sudo apt-get install boxes
		sudo pip3 install flask
		sudo pip3 install requests
	else 
		echo -e $RED "Please Check Your Internet Connection ..!!"
	fi

    if [ -d "$INSTALL_DIR" ]; then
        echo "";
        echo "[✔] Successfully Installed !!! ";
        echo "";
        echo "";
        echo -e $ORANGE "		[+]+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[+]"
        echo 		"		[+]						      		[+]"
        echo -e $ORANGE  "		[+]     ✔✔✔ Now Just Type In Terminal (kryptonhub) ✔✔✔ 	[+]"
        echo 		"		[+]						      		[+]"
        echo -e $ORANGE "		[+]+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[+]"
    else
        echo "[✘] Installation Failed !!! [✘]";
        exit
    fi
elif [ $choice -eq 0 ];
then
    echo -e $RED "[✘] Thank You !! [✘] "
    exit
else 
    echo -e $RED "[!] Select Valid Option [!]"
fi