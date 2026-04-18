# COMP2152 — Term Project: CTF Bug Bounty

## Team Name
NetDefenders-COMP2152

## Team Members
Sanzida Islam - 101564719 (https://github.com/Subha06-star/NetDefenders-COMP2152)
Rezarta Marku - 101402390 (https://github.com/rezarta5/NetDefenders-COMP2152)
Wasifa Hossain - 101594842 (https://github.com/wasifahs/NetDefenders-COMP2152)

| Member | Vulnerability Found | Branch Name |
|--------|-------------------|-------------|
| Sanzida Islam | No HTTPS on api.0x10.cloud| sanzida-feature |
| Rezarta Marku | Open Port Exposure on api.0x10.cloud | rezarta-feature |
| Wasifa Hossain | Server Information Disclosure on api.0x10.cloud | wasifa-feature |

## Videos

Each team member records a short video (max 3 minutes) explaining their vulnerability. Add your YouTube links below:

- Member 1: https://youtube.com/watch?v=_______
- Member 2: https://youtube.com/watch?v=_______
- Member 3: https://youtube.com/watch?v=_______

## Vulnerability Report (Sanzida Islam)

### Title:
No HTTPS on api.0x10.cloud

### Description:
The website allows communication over HTTP instead of HTTPS. This means data transmitted between the user and the server is not encrypted. An attacker can intercept sensitive information such as login credentials using a man-in-the-middle (MITM) attack.

### Proof:
Scanning target: api.0x10.cloud
Port 80 (HTTP) is OPEN
Port 443 (HTTPS) is OPEN (but HTTPS is not enforced)
HTTP request test:
http://api.0x10.cloud → 200 OK (No redirect to HTTPS)

Observation:
- Connection is established over unencrypted HTTP (port 80)
- No forced redirect from HTTP → HTTPS
- Data transmitted over port 80 is not encrypted

  
## Vulnerability Report (Rezarta Marku)

### Title:

Open Port Exposure on api.0x10.cloud

### Description:

Ports such as Telnet (23), FTP (21), or Redis (6379) may be open on the target server. These services are often insecure or misconfigured. For example, Telnet sends data in plaintext, and Redis may allow unauthorized access if not secured. Open ports increase the attack surface and can be exploited by attackers.

### Proof:
1. A Python script was used to scan common ports on the target server api.0x10.cloud using the socket library.

2. The script attempted connections to ports: 21, 22, 23, 80, 443, and 6379.

3. The scan result showed that ports 80 (HTTP) and 443 (HTTPS) are open, while the others are closed.

4. Port 80 allows unencrypted communication, which can expose data to interception, even though HTTPS is available on port 443.

Output:
[+] Port 21 is closed
[+] Port 22 is closed
[+] Port 23 is closed
[!] Port 80 is OPEN
    → HTTP is insecure (no encryption)
[!] Port 443 is OPEN
    → HTTPS is secure but HTTP should be redirected
[+] Port 6379 is closed

## Vulnerability Report (Wasifa Hossain)

### Title:
Server Information Disclosure on api.0x10.cloud

### Description:
The target web application exposes server-related information through HTTP response headers such as "Server" and "X-Powered-By".

This is a security vulnerability because it reveals details about the server software and technologies used. Attackers can use this information to identify known vulnerabilities associated with specific versions and launch targeted attacks.

Therefore, exposing server information increases the risk of exploitation.

### Proof:
1. A Python script was used to send a request to the target server.
2. The response headers were analyzed.
3. The "Server" or "X-Powered-By" header was found.

Output:
VULNERABILITY: Server information exposed → nginx/1.18.0


## Target

- Server: `0x10.cloud` and its subdomains
- Submission: http://submit.0x10.cloud
- Leaderboard: http://ranking.0x10.cloud

## Important: Rate Limit

The server allows **10 requests per second** per IP address. If you send requests too fast, you will get blocked (HTTP 429). Add a small delay between requests:

```python
import time
time.sleep(0.15)  # wait 150ms between requests
```
