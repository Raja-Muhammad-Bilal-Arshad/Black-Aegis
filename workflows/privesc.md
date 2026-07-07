---
description: Elevate to System/Root/Admin
---

# Privilege Escalation Workflow

## 1. Windows Privesc
1.  **Kernel Exploits**: Suggester checks (Watson/Sherlock). Only use if necessary (unstable).
2.  **Misconfigurations**:
    - Unquoted Service Paths.
    - Writable Service Binaries.
    - AlwaysInstallElevated.
3.  **Credentials**: Memory dumping (LSASS), cached GPP passwords, SAM hive.

## 2. Linux Privesc
1.  **Sudo Rights**: `sudo -l`. (GTFOBins).
2.  **SUID Binaries**: `find / -perm -u=s -type f 2>/dev/null`.
3.  **Kernel**: DirtyCow, PwnKit (if applicable).
