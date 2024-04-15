

import re
import subprocess
def user_input():
 print("\n[!]USE THE MAC CHANGER AS ROOT USER!")
 interface = input("[+]ENTER YOUR INTERFACE TO CHANGE MAC ADDRESS: ")
 mac= input("[+]ENTER YOUR CUSTOM MAC ADDRESS: ")


 return interface , mac

def mac_checker(mac):
    if re.match("^00([-:][0-9a-fA-F]{2}){5}$", mac):
        return True
    else:
        print("[!]ERROR ! : (ENTER A MAC THAT STARTS WITH 00 AND HEXADECIMAL DIGITS!) ")


def mac_changer(interface,mac):
    try:
       subprocess.check_call(f"sudo ip link set dev {interface} down " , shell=True )
       subprocess.check_call(f"sudo ip link set dev {interface} address {mac} " , shell=True )
       subprocess.check_call(f"sudo ip link set dev {interface} up" , shell = True)
       print("[+]MAC ADDRESS CHANGED SUCCESSFULLY!")

    except subprocess.CalledProcessError as e:
        print(f"[-]AN ERROR OCCURED : {e}")

    except Exception as e:
        print(f"[-]AN UNEXPECTED ERROR OCCURED : {e}")

def main_func():
    interface , mac = user_input()
    if mac_checker(mac):
     mac_changer(interface, mac)

main_func()
