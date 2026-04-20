# ============================================
# Author: Wasifa Hossain
# Vulnerability: Server Information Disclosure
# Target: api.0x10.cloud
# ============================================

import urllib.request
import time

url = "http://api.0x10.cloud"

try:
    response = urllib.request.urlopen(url)
    headers = dict(response.getheaders())

    print("Checking server information...\n")

    if "Server" in headers:
        print(f"[!] VULNERABILITY: Server information exposed → {headers['Server']}")
        print("    → Attackers can use this info to find known vulnerabilities")
    else:
        print("[+] Server header not found")

    if "X-Powered-By" in headers:
        print(f"[!] VULNERABILITY: Technology disclosed → {headers['X-Powered-By']}")
        print("    → Reveals backend technology (security risk)")
    else:
        print("[+] X-Powered-By header not found")

    time.sleep(0.15)

except Exception as e:
    print("Error:", e)