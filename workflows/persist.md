---
description: Install backdoors/implants
---

# Persistence Workflow

## 1. User Land
1.  **Registry Run Keys**: `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`.
2.  **Startup Folder**: `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup`.
3.  **Scheduled Tasks**: `schtasks /create /tn "Updater" /tr "cmd.exe /c payload.exe" /sc daily /st 12:00`.

## 2. Admin Land
1.  **Services**: Create a new service (or modify existing, stopped one).
2.  **WMI Subscriptions**: Event-triggered execution (e.g., on system uptime).
3.  **DLL Hijacking**: Place malicious DLL next to a trusted binary.

## 3. AD Persistence
1.  **Golden Ticket**: Create TGT valid for 10 years.
2.  **Anomalous ACLs**: Grant "Full Control" to a low-priv user on the Admin group object.
