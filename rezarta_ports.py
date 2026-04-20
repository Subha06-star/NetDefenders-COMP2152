# ============================================
# Author: Rezarta Marku
# Vulnerability: Open Port Exposure
# Target: api.0x10.cloud
# ============================================

import socket
import time

target = "api.0x10.cloud"
ports = [21, 22, 23, 80, 443, 6379]

for port in ports:
   try:
     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     sock.settimeout(2)

     result = sock.connect_ex((target, port))

     if result == 0:
       print(f"[!] Port {port} is OPEN")

       if port == 23: 
         print("   → Telnet is insecure (plaintext communication)")
       elif port == 21:
         print("   → FTP may allow anonymous login")
       elif port == 6379:
         print("   → Redis may be exposed without authentication")
       else:
         print("   → Service is exposed")

     else:
       print(f"[+] Port {port} is closed")

     sock.close()
     time.sleep(0.15)

   except Exception as e:
     print(f"Error: {e}")