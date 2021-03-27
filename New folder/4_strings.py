from pprint import pprint

device1_str = "  r3-L-n7, cisco, catalyst 2960, ios  "

print("String split, strip, replace")
# Split
device1 = device1_str.split(",")
print("Device1 using split")
print("    ", device1)

# strip
device1 = device1_str.strip().split(",")
print("Device1 using strip and split")
print("    ", device1)

# replace to remove blanks
device1 = device1_str.replace(" ", "").split(",")
print("device1 using replace and split")
print("    ", device1)

# replace to remove and replace blanks with colon
device1 = device1_str.replace(" ", "").replace(",", ":")
print("device1 with balcks removed with colon")
print("    ", device1)

# loop with split and strip
device1 = list()
for items in device1_str.split(","):
    device1.append(items.strip())
print("device1 using strip and loop")
print("    ", device1)

# strip and split, single line using list comprehension
device1 = [items.strip() for items in device1_str.split(",")]
print("device1 using list comprehension")
print("    ", device1)

# ignoring case
print("\n\nIgnoring case")
model = "CSR1000V"
if model == "csr1000v":
    print(f"Model matched: {model}")
else:
    print(f"Model mismatched: {model}")

# going again using lowercase
if model.lower() == "csR1000v".lower():
    print(f"Model matched: {model}")
else:
    print(f"Model mismatched: {model}")

# Finding substrings
print("\n\n____Finding Substrings____")
version = "Virtual XE Software, Version 16.11.1a, Release Software fc1"
expected_version = "Version 16.11.1a"
index = version.find(expected_version)
if index>=0:
    print(f"Found Version: {expected_version} at index {index}")
else:
    print(f"Not found: {expected_version}")

# separating string in parts
print("\n\n____Separating version string components___")
version_info = version.split(",")
for part_no, version_info_part in enumerate(version_info):
    print(f"Version info part {part_no}: {version_info_part}")

show_interface_stats = """
GigabitEthernet1
          Switching path    Pkts In   Chars In   Pkts Out  Chars Out
               Processor      25376    1529598       8242     494554
             Route cache          0          0          0          0
       Distributed cache     496298   60647894     673003  218461079
                   Total     521674   62177492     681245  218955633
GigabitEthernet2
          Switching path    Pkts In   Chars In   Pkts Out  Chars Out
               Processor         19       1140          0          0
             Route cache          0          0          0          0
       Distributed cache       6077     663304          0          0
                   Total       6096     664444          0          0
Interface GigabitEthernet3 is disabled
Loopback21
          Switching path    Pkts In   Chars In   Pkts Out  Chars Out
               Processor          0          0          0          0
             Route cache          0          0          0          0
       Distributed cache          0          0          0          0
                   Total          0          0          0          0
Loopback55
          Switching path    Pkts In   Chars In   Pkts Out  Chars Out
               Processor          0          0          3        241
             Route cache          0          0          0          0
       Distributed cache          0          0          0          0
                   Total          0          0          3        241
Loopback100
          Switching path    Pkts In   Chars In   Pkts Out  Chars Out
               Processor          0          0         43       2806
             Route cache          0          0          0          0
       Distributed cache          0          0          0          0
                   Total          0          0         43       2806
"""

interface_counters = dict()
show_interface_stats_lines = show_interface_stats.splitlines()
for index,stats_line in enumerate(show_interface_stats_lines):
    if stats_line.find("GigabitEthernet", 0) == 0:

        totals_line = show_interface_stats_lines[index+5]
        interface_counters[stats_line] = totals_line.split()[1:]

print("\n\n__________Interface Counters______")
pprint(interface_counters)