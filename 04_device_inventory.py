
device = {
    "hostname": "switch01",
    "ip": "192.168.1.10",
    "status": "Up",
    "building": "Library",
}

device["severity"] = "Critical"
device["status"] = "Down"
device["maintenance"] = True
#print(device)
#device["maintenance"] = False

print("====== DEVICE INVENTORY ======")
print(f"Hostname: {device['hostname']}")
print(f"Ip:  {device['ip']}")
print(f"Status: {device['status']}")
print(f"Severity: {device['severity']}")
print(f"Maintenance: {device['maintenance']}")
print(f"Building {device['building']}\n==============================")

if device['status'] == "Up":
        print("DEVICE HEALTHY")

elif device['maintenance']:
    print("MAINTENANCE - NO ESCALATION")


#elif not device['maintenance']:
 #   escalator(device)

    
#def escalator(dev):
           
elif device['status'] == "Down" and device['severity'] == "Critical": #and device['maintenance'] == False:
        print("ESCALATE IMMEDIATELY")

elif device['status'] == "Down" and device['severity'] == "Warning": #and device['maintenance'] == False:
        print("REVIEW REQUIRED")


elif device['status'] == "Down":
        print("ESCALATE")

    



