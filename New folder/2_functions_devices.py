from random import choice
import string
from tabulate import tabulate


def create_devices(num_subnet=1, num_devices=1):

    # create list of devices
    created_devices = list()

    if num_devices > 254 or num_subnet > 254:
        print("Error: Too many devices and/or subnets requested.")
        return created_devices

    for subnet_index in range(1, num_subnet+1):

        for devices_index in range(1, num_devices+1):

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
            device["ip"] = "10.0." + str(subnet_index) + "." + str(devices_index)

            created_devices.append(device)

    return created_devices


# ____main program__________________
if __name__ == "__main__":

    devices = create_devices(num_subnet=5, num_devices=4)
    print(tabulate(devices, headers="keys"))
