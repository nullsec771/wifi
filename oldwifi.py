import xml.etree.ElementTree as ET
import os
os.system('netsh wlan export profile folder=C:\ key=clear')
test = input("enter ur wifi name : ")
y= "C:\\Wi-Fi-" + test + ".xml"
tree = ET.parse(y)
root = tree.getroot()
name = root.find('.//{http://www.microsoft.com/networking/WLAN/profile/v1}name').text
password = root.find('.//{http://www.microsoft.com/networking/WLAN/profile/v1}keyMaterial').text
print(f"ur wifi Name: {name}")
print(f"ur password: {password}")