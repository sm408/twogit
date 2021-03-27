from util.create_utils import create_devices
from pprint import pprint
from tabulate import tabulate

devices = create_devices(num_subnet=2, num_devices=10)

print("\n    Name    Vendor : OS      IP Address    Version")
print("   ______   _______  _____   ___________  ________")
for device in devices:
    print(f'{device["name"]:>9}  {device["vendor"]:>8} : {device["os"]:<5}   {device["ip"]:<9}   {device["version"]}')

print("\n\n_______Only Cisco devices_______")
print("\n    Name    Vendor : OS      IP Address    Version")
print("   ______   _______  _____   ___________  ________")
for device in devices:
    if device["vendor"].lower() == "cisco":
        print(
            f'{device["name"]:>9}  {device["vendor"]:>8} : {device["os"]:<5}   {device["ip"]:<9}   {device["version"]}')

print("\n\n_____Finding duplicate values_______")
flag = 0
for index, device_a in enumerate(devices):
    for device_b in devices[index+1:]:
        if device_a["name"] == device_b["name"]:
            flag +=1
            print(
                f"\nMatch Found:  {device_a['name']} found at both {device_a['ip']} and {device_b['ip']}"
            )
if flag == 0:
    print("\n_________No match found!!!______")
print("\n_____Comparison Complete_______")

