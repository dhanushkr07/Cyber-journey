#!/user/bin/env python3
# portscan.py - a simple TCP port scanner
# usage: python3 portscan.py <target>


import socket
import sys

target = sys.argv[1]

ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3306, 3389, 8080]

print(f"scanning {target} ...")
print("")

for port in ports:
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     s.settimeout(1)
     result = s.connect_ex((target, port))
     if result == 0:
        print(f"[+] port {port}: OPEN")
     s.close()


print("")
print("scan complete.")
