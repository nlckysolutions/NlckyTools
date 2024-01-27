import pywifi
from pywifi import const

def create_multiple_open_wifi_networks(ssid, num_networks):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.disconnect()
    iface.remove_all_network_profiles()

    for i in range(num_networks):
        profile = pywifi.Profile()
        profile.ssid = ssid
        profile.auth = const.AUTH_OPEN

        iface.connect(iface.add_network_profile(profile))
        print(f"Successfully created open WiFi network {i+1} with SSID: {ssid}")

if __name__ == "__main__":
    ssid = input("Enter the desired SSID for the WiFi networks: ")
    num_networks = int(input("Enter the number of WiFi networks to create: "))
    create_multiple_open_wifi_networks(ssid, num_networks)
