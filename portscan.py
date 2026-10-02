#!/user/bin/env python3
# portscan.py v2 -TCP scanner with service name, banner grab, and report
# usage: python3 portscan.py <target> [start] [end]
# Example; python3 portscan.py scanme.nmap.org 1 1024


import socket
import sys
from datetime import datetime

# common port _> service name
SERVICES = {
    21: "FTH", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
    80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS", 445: "SMB",
    3306: "MySQL", 3389: "RDP", 8080: "HTTP-proxy",
}

target = sys.argv[1]

#port range from args, else default 1-1024
if len(sys.argv) >=4:
   start = int(sys.argv[2])
   end = int(sys.argv[3])
else:
    start, end = 1, 1024

print(f"scanning {target} ports {start}-{end} ...")
print("")

open_ports = []
report_lines = []

for port in range(start, end + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target, port))
    if result == 0:
        name =SERVICES.get(port, "unknown")
        banner = ""
        try:
            banner = s.recv(1024).decode().strip()
        except Exception:
            banner = ""
        line = f"[+] Port {port}: OPEN ({name})"
        if banner:
            line += f" banner: {banner}"
        print(line)
        open_ports.append(port)
        report_lines.append(line)
    s.close()

print("")
print(f"Scan complete. {len(open_ports)} open ports(s): {open_ports}")

# save the report
with open("scan_report.txt", "w") as f:
    f.write(f"port scan of {target} ({start}-{end}) at {datetime.now()}\n")
    for line in report_lines:
        f.write(line + "\n")
print("Report saved to scan_report.txt")
