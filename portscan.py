#!/usr/bin/env python3
# portscan.py v2 - TCP scanner with threading, banner grab, and report
# Usage: python3 portscan.py <target> [start_port] [end_port]
# Example: python3 portscan.py scanme.nmap.org 1 1024

import socket
import sys
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# --- SECTION 1: Known services ---
# Maps port numbers to service names so the report is readable
SERVICES = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
    80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS", 445: "SMB",
    3306: "MySQL", 3389: "RDP", 8080: "HTTP-Proxy",
}

# --- SECTION 2: Check arguments ---
# Make sure the user gave at least a target IP/hostname
if len(sys.argv) < 2:
    print("Usage: python3 portscan.py <target> [start] [end]")
    print("Example: python3 portscan.py scanme.nmap.org 1 1024")
    sys.exit(1)

target = sys.argv[1]

# If user gave start and end ports, use them. Otherwise default 1-1024
if len(sys.argv) >= 4:
    start = int(sys.argv[2])
    end = int(sys.argv[3])
else:
    start, end = 1, 1024

# --- SECTION 3: The scanning function ---
# This function scans ONE port. We will run it 50 times in parallel.
def scan_port(port):
    # Create a socket (think of it as a virtual phone)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)  # Don't wait more than 0.5 seconds per port

    # Try to connect. connect_ex returns 0 if successful, error code if not
    result = s.connect_ex((target, port))

    if result == 0:
        # Port is OPEN! Now grab the banner
        name = SERVICES.get(port, "unknown")
        banner = ""
        try:
            # Send an HTTP request to trigger a response from the server
            s.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
            # Read whatever the server sends back
            raw = s.recv(1024).decode(errors='ignore').strip()
            # Take only the first line (the most useful part)
            banner = raw.split('\n')[0] if raw else ""
        except Exception:
            banner = ""

        s.close()

        # Build the result line
        line = f"[+] Port {port}: OPEN ({name})"
        if banner:
            line += f" | Banner: {banner}"
        return (port, line)

    s.close()
    return None  # Port is closed, return nothing

# --- SECTION 4: Run the scan ---
print(f"\nScanning {target} ports {start}-{end}...")
print(f"Started at {datetime.now().strftime('%H:%M:%S')}\n")

open_ports = []
report_lines = []

# ThreadPoolExecutor runs 50 scan_port() calls at the same time
# Without this, scanning 1024 ports would take ~8 minutes
# With 50 threads, it takes ~10 seconds
with ThreadPoolExecutor(max_workers=50) as executor:
    # Submit all ports to the thread pool
    futures = [executor.submit(scan_port, p) for p in range(start, end + 1)]

    # Collect results as they finish
    for future in futures:
        result = future.result()
        if result:
            port, line = result
            print(line)
            open_ports.append(port)
            report_lines.append(line)

# --- SECTION 5: Summary and report ---
print(f"\nScan complete at {datetime.now().strftime('%H:%M:%S')}")
print(f"Found {len(open_ports)} open port(s): {sorted(open_ports)}")

# Save results to a file
with open("scan_report.txt", "w") as f:
    f.write(f"Port scan of {target} ({start}-{end})\n")
    f.write(f"Date: {datetime.now()}\n\n")
    for line in report_lines:
        f.write(line + "\n")

print("Report saved to scan_report.txt")
