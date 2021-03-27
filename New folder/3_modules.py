from tabulate import tabulate
from util.create_utils import create_devices


if __name__ == "__main__":
    devices = create_devices(num_subnet=4, num_devices=5)
    print(tabulate(devices,headers="keys"))