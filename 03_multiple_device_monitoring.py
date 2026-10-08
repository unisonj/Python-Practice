devices = ["switch01", "switch02", "switch03", "switch04", "switch05"]

statuses = ["Up", "Down", "Up", "Down", "Up"]
## switch01 = Up
#switch02 = Down
#switch03 = Up
#switch04 = Down
#switch05 = Up

print("")
print("===== NETWORK MONITOR =====")
print("")

dev_count = 0
down_devices = 0

for device, status in zip(devices, statuses):
    print(device, status)
    dev_count = dev_count + 1
    if status == "Down":
        print(f"ALERT {device} IS DOWN")
        down_devices = down_devices + 1

up_devices = dev_count - down_devices

print("")
print("==== SUMMARY ====")
print(f"Total Devices: {dev_count} \nDevices Down: {down_devices} \nDevices Up: {up_devices}")
print("=================")
print("")


#dev_count = 0
#for device in devices:
#    dev_count = dev_count + 1


#down_devices = 0
#for down_devices in zip(devices, statuses):
 #   if status == "Down"