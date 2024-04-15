import subprocess
import re

import scapy.all as scapy
import subprocess as sub
def user_input():
    print("[!]USE THE NETWORK SCANNER ONLY AS ROOT!")
    range = input("[+]ENTER A YOUR NETWORK RANGE : ")
    return range

def network(range):
    try:
      sub.call(f"sudo netdiscover -r {range}" , shell=True)
    except subprocess.CalledProcessError as e :
        print(f"[!]ERROR OCCURED : {e}")
    except Exception :
        print("[!]ENTER CORRECT NETWORK RANGE !")
    return range

def main():
    range = user_input()
    network(range)

if __name__ == '__main__':
    main()