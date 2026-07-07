---
description: Internal discovery & mapping
---

# Enumeration Workflow

## 1. Host Enumeration
1.  **Whoami**: `whoami /all`, `ipconfig /all`.
2.  **Defenses**: `sc query windefend`, `tasklist | findstr /i "cb carbon"`.
3.  **Files**: Search for `passwords.txt`, `config.xml`.

## 2. Network Enumeration
1.  **Scanning**: `arp -a`, `netstat -ano`.
2.  **Neighbors**: Identify DCs, File Servers, DBs.

## 3. AD Enumeration
1.  **Domain**: `net domain`, `Get-NetDomain` (PowerView).
2.  **Users/Groups**: `Get-NetUser | select name, lastlogon`, `Get-NetGroup "Domain Admins"`.
3.  **Shares**: `Find-DomainShare`.
