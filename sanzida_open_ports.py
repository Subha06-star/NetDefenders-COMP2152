# ============================================
# Author: Sanzida Islam
# Vulnerability: Open Ports Detection
# Target: api.0x10.cloud
# ============================================

import socket
import time

target = "api.0x10.cloud"

# Common + non-standard ports
ports = [21, 22, 80, 443, 2121, 2323, 2525, 6379]

for port in ports:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"\n[!] VULNERABILITY: Port {port} is OPEN on {target}")

            if port == 21 or port == 2121:
                print("    → FTP may allow anonymous login (data exposure risk)")
            elif port == 22:
                print("    → SSH exposed (possible brute-force target)")
            elif port == 2323:
                print("    → Telnet sends data in cleartext (HIGH RISK)")
            elif port == 2525:
                print("    → SMTP may allow spam or abuse")
            elif port == 6379:
                print("    → Redis often runs without authentication (CRITICAL)")
            else:
                print("    → Service exposed on this port")

        else:
            print(f"[+] Port {port} is closed")

        sock.close()
        time.sleep(0.15)

    except Exception as e:
        print(f"Error scanning port {port}: {e}")