# T1563.002 - RDP Hijacking Hunting Guide

## Log Artifacts

| Event ID | Source | Description |
|----------|--------|-------------|
| **4778** | Security | A session was reconnected to a Window Station. |
| **4624** | Security | Logon (Type 10). |

## Behavior
- Execution of `tscon.exe` or `rwinsta.exe`.
- Event 4778 where `Account Name` changes or is unexpected for that Session ID.
- Service creation executing `cmd /k tscon ...` (a common technique to get SYSTEM context).
