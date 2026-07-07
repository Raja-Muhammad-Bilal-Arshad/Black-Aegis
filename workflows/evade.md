---
description: Bypass EDR/AV/Firewalls
---

# Evasion Workflow

## 1. Static Evasion (Disk)
1.  **Obfuscate**: Encrypt strings, randomize function names.
2.  **Certify**: Sign binary with a (stolen or self-signed) code signing cert.
3.  **Pack**: Use custom packers (avoid UPX).

## 2. Dynamic Evasion (Runtime)
1.  **Unhook**: Detect hooks in `ntdll.dll` and overwrite with clean syscalls.
2.  **Sleep**: Long sleeps hide from Sandbox analysis (execution timeout).
3.  **Spoof**: Fake Parent Process ID (PPID) to look like `svchost.exe`.

## 3. Network Evasion
1.  **Jitter**: Randomize C2 check-in times (10% - 30%).
2.  **Domain Fronting**: Use CDN (Cloudflare/Azure) to hide destination IP.
