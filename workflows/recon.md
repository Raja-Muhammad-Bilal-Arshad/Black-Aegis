---
description: Passive/Active Intel Gathering
---

# Reconnaissance Workflow

## 1. Passive Recon (No Touching)
1.  **Scope Validation**: Confirm targets in `scope.txt`.
2.  **OSINT**:
    - `theHarvester -d target.com -b google,linkedin`
    - Check BGP ASN for IP ranges.
3.  **Breach Check**: Search DeHashed/HIBP for `@target.com`.

## 2. Active Recon (Touching)
1.  **Subdomain Enumeration**:
    - `subfinder -d target.com`
    - `amass enum -d target.com`
2.  **Port Scanning**:
    - `masscan -p1-65535 --rate=1000` (Fast)
    - `nmap -sV -sC -p <ports>` (Detailed)
3.  **Service ID**: Screenshot HTTP services (`aquatone` / `gowitness`).
