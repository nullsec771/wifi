import os
import sys
import ctypes
import xml.etree.ElementTree as ET
import subprocess

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def import_wifi_profile():
    with open(os.devnull, 'w') as devnull:
        subprocess.Popen('netsh wlan export profile folder=C:\ key=clear', shell=True, stdout=devnull, stderr=devnull)
    wifi_name = input("Enter your WiFi name: ")
    xml_file = f"C:\\Wi-Fi-{wifi_name}.xml"

    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        name = root.find('.//{http://www.microsoft.com/networking/WLAN/profile/v1}name').text
        password = root.find('.//{http://www.microsoft.com/networking/WLAN/profile/v1}keyMaterial').text
        print(f"Your WiFi Name: {name}")
        print(f"Your Password: {password}")
    except FileNotFoundError:
        print("WiFi profile not found.")

def main():
    if is_admin():
        import_wifi_profile()
        input("Press enter to exit...")
    else:
        print("This script requires administrator privileges to run.")
        run_as_admin()

def run_as_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

if __name__ == "__main__":
    main()
