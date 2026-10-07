import socket
import sys
from datetime import datetime

# Define the target (You can use a safe testing site or localhost)
target_host = "scanme.nmap.org" 

print("-" * 50)
print(f"Scanning target: {target_host}")
print(f"Time started: {str(datetime.now())}")
print("-" * 50)

# List of common ports to check
ports_to_scan = [21, 22, 23, 80, 443, 8080]

try:
    for port in ports_to_scan:
        # Set up a standard internet socket connection
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0) # Don't wait forever if the port is closed
        
        # Attempt to connect to the port
        result = s.connect_ex((target_host, port))
        
        if result == 0:
            print(f" Port {port}: OPEN ✅")
        else:
            print(f" Port {port}: Closed ❌")
        s.close()

except KeyboardInterrupt:
    print("\nExiting script.")
    sys.exit()

except socket.gaierror:
    print("\nHostname could not be resolved.")
    sys.exit()
