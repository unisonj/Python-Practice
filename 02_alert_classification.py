hostname = input("Hostname: ")
ip = input("IP address: ")
status = input("Status: ")
severity = input("Severity: ")
building = input("Building: ")

print("======= Network Device Report ======")
print(f"Hostname: {hostname}\nStatus: {status}\nSeverity: {severity}\nBuilding: {building}")
print("====================================")

if status == "Down" and severity == "Critical":
    print("ESCALATE IMMEDIATELY")

elif status == "Down" and severity == "Warning":
    print("REVIEW REQUIRED")

elif status == "Up":
    print("DEVICE HEALTHY")   

elif status == "Down":
    print("ESCALATE")

else: 
    print("INPUT INVALID")


