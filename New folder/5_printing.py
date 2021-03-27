from util.create_utils import create_devices
from pprint import pprint
from datetime import datetime
from time import sleep
from operator import itemgetter
from tabulate import tabulate
from random import choice

devices = create_devices(num_subnet=4, num_devices=3)

pprint(devices)

print("Using loops")
for device in devices:
    sleep(0.1)
    device["Last heard"] = str(datetime.now())
    pprint(device)

print("\n___________Using Tabulate_______")
print(
    tabulate(sorted(devices,key=itemgetter("vendor","os","version")),headers="keys")
)

print("\n\n___________Multiple print statements in same line________")
print("Testing hardware")
for device in devices:
    print(f"---- Testing device {device['name']} ....", end="")
    sleep(choice([0.1,0.3,0.4,0.5]))
    print("Done")
