---
name: opsec-control
description: Log cleaning, time-stomp, proxy chains.
---

# OPSEC Control Protocol

## 1. Principles
- **Blend In**: Don't beacon every 5 seconds (jitter). Don't run commands at 3 AM local time.
- **Clean Up**: If you drop a file, delete it. If you create a user, remove it.
- **Proxy Everything**: Never expose the Teamserver IP. redirectors only.

## 2. Techniques
- **Time Stomping**: `(Get-Item file.exe).LastWriteTime = (Get-Date "01/01/2020")`.
- **Log Cleaning**: `wevtutil cl Security` (Alerts everyone!). Better: stop logging threads.
- **Redirectors**: Use multiple layers of Apache/Nginx reverse proxies to hide the C2.

## 3. Checklist
- [ ] C2 Profile has high jitter?
- [ ] User-Agent matches legitimate traffic?
- [ ] Redirectors are healthy?
- [ ] Cleanup script prepared?
