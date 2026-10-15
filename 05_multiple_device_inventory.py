devices = [
    {
        "hostname": "switch01",
        "ip": "192.168.1.10",
        "status": "Up",
        "severity": "Low",
        "building": "Library",
        "maintenance": False
    },
    {
        "hostname": "switch02",
        "ip": "192.168.1.11",
        "status": "Down",
        "severity": "Critical",
        "building": "Engineering",
        "maintenance": False
    },
    {
        "hostname": "switch03",
        "ip": "192.168.1.12",
        "status": "Down",
        "severity": "Warning",
        "building": "Student Union",
        "maintenance": True
    }
]

up_count = 0
down_count = 0
total_count = len(devices)
maint_count = 0
imed_escl_count = 0

#def checker(x):
#    down_count = down_count + 1
#    total_count = total_count + 1

print("==== NETWORK DEVICE INVENTORY ====")
print(" ")
for dev in (devices):
    print(f"{dev['hostname']} | {dev['status']} | {dev['building']} ")
    

    if dev['status'] == "Up" and dev['maintenance']:
            print("DEVICE HEALTHY")
            up_count = up_count + 1
            maint_count + 1

    elif dev['status'] == "Up":
        print("DEVICE HEALTHY")
        up_count = up_count + 1
        
        

    elif dev['maintenance']:
        print("MAINTENANCE")
        maint_count = maint_count + 1
        down_count = down_count + 1
        #checker
    elif dev['severity'] == "Critical":
        print("ESCALATE IMMEDIATELY")
        imed_escl_count = imed_escl_count + 1
        down_count = down_count + 1
        
        #checker



    elif dev['severity'] == "Warning":
        print("REVIEW REQUIRED")
        down_count =  down_count + 1
        
        
        #checker

    elif dev['status'] == "Down":
        print("ESCALATE")
        down_count = down_count + 1
        
        #checker

    print(" ")    
        
print("=====NETWORK SUMMARY====")

print(f"Total Devices: {total_count}")
print(f"Up Devices: {up_count}")
print(f"Down Devices: {down_count}")
print(f"Devices in Maintenance: {maint_count}")
print(f"Immediately Escalated Devices: {imed_escl_count}")
print("========================")


