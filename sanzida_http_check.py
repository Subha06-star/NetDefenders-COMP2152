# ============================================
# Author: Sanzida Islam
# Vulnerability: No HTTPS (HTTP usage)
# Target: api.0x10.cloud
# ============================================

import urllib.request

try:
    response = urllib.request.urlopen("http://api.0x10.cloud")
    
    print("Final URL:", response.url)

    if response.url.startswith("http://"):
        print("[!] VULNERABILITY: Site does NOT use HTTPS")
        print("    → Data can be intercepted (MITM attack)")
    else:
        print("[+] Redirects to HTTPS (Safe)")

except Exception as e:
    print("Error:", e)