from pprint import pprint

device={
    "name":"Mobile",
    "os":"OSX",
    "version":"1.1",
}
for key, values in device.items():
    print(f"{key:>7s} : {values}")

pprint(device, width=1);
