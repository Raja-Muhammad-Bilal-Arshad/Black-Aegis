# T1570 - Lateral Tool Transfer Hunting Guide

## Log Artifacts

| Event ID | Source | Description |
|----------|--------|-------------|
| **11** | Sysmon | FileCreate. Look for executable files dropped in `C:\Users\Public`, `C:\Temp`, or `C:\ProgramData`. |
| **4663** | Security | File object access (Write data). |
| **5145** | Security | Detailed Share Access. Look for Access Mask `0x2` (WriteData) on a network share. |

## Indicators
- Usage of `certutil.exe`, `bitsadmin.exe`, or `curl.exe` to download files.
- SMB copy of `.exe` or `.dll` files to administrative shares.
