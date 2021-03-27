from random import choice
import string
from tabulate import tabulate
from operator import itemgetter
from pprint import pprint

devices = list()

# for loop to create a large number of devices
for index in range(1, 10):
    # create device dictionary
    device = dict()

    # random device name
    device["name"] = (
            choice(["r2", "r3", "r4", "r6", "r10"])
            + choice(["L", "U"])
            + choice(string.ascii_letters)
    )

    # random vendors from choice of cisco, juniper, arista
    device["vendor"] = choice(["cisco", "juniper", "arista"])
    if device["vendor"] == "cisco":
        device["os"] = choice(["ios", "iosxe", "iosxr", "nexus"])
        device["version"] = choice(["12.1T 04", "14.8Y", "13.T6.78"])
    elif device["vendor"] == "juniper":
        device["os"] = "junos"
        device["version"] = choice(["J7.5.78", "A6.678.987", "Fg56.87.90"])
    elif device["vendor"] == "arista":
        device["os"] = "eos"
        device["version"] = choice(["34,.6", "67.87", "87.67.01"])
    device["ip"] = "10.0.0." + str(index)

    # nicely formatted print of this device
    print()
    for key, values in device.items():
        print(f"{key:>16s} : {values}")

    # adding those to list of devices
    devices.append(device)

print("\n__________A list of devices as dictionary______")
pprint(devices)

print("\n_______Devices in form of a table_________")
print(tabulate(sorted(devices, key=itemgetter("vendor", "os", "version")), headers="keys"))
