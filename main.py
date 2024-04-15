#!/usr/bin/python3

import subprocess



# ANSI color codes
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE ="\033[34m"
RESET = "\033[0m"


def welcome():
    print(
 f"""
 {GREEN}
   ██╗  ██╗ █████╗  ██████╗ ███╗   ███╗ ██╗██╗  ██╗
   ██║ ██╔╝██╔══██╗ ██╔══██╗████╗ ████║ ██║██║ ██╔╝
   █████╔╝ ███████║ ██████╔╝██╔████╔██║ ██║█████╔╝
   ██╔═██╗ ██╔══██║ ██╔══██╗██║╚██╔╝██║ ██║██╔═██╗
   ██║  ██╗██║  ██║ ██║  ██║██║ ╚═╝ ██║ ██║██║  ██╗
   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═╝  ╚═╝╚═╝     ╚═╝ ╚═╝╚═╝  ╚═╝ v1.0
                 {RED} BY BHAVYA NEGI        {RESET}                             
   {RESET}
    """)
def menu():
    print(f"{BLUE}       WELCOME TO MAIN MENU!\n {RESET}"
          f"  {YELLOW}         [1]MAC CHANGER\n {RESET}"
          f"  {YELLOW}         [2]NETWORK SCANNER\n {RESET}"
          f"  {YELLOW}         [3]ARP SPOOFER\n {RESET}"
          f"  {YELLOW}         [4]WEB CRAWLER\n {RESET}")
    user_input= input(f'       {RED}ENTER YOUR CHOICE : {RESET} ')
    return user_input


def main():
 while True:
    try:
        welcome()
        choice = menu()

        if choice == '1':
            from mac_changer import main_func
            main_func()  # This function needs to be called to execute its functionality.

        elif choice == "2":
            from network_scanner import main
            main()  # This function needs to be called to execute its functionality.

        elif choice == "3":
            from arp_spoof import main
            main()
        elif choice == "4":
            from website_crawler import main
            main()
    except KeyboardInterrupt:
        print("[!] ERROR: Keyboard Interruption!")
        exit()
main()

