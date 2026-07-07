# T1550.002 - Pass the Hash Hunting Guide

## Log Artifacts

| Event ID | Source | Description |
|----------|--------|-------------|
| **4624** | Security | Successful Logon. **Logon Type 3** (Network) using NTLM. Key: **Key Length is 0**. |
| **4624** | Security | **Logon Process Name** is `seclogon` (if using Mimikatz `sekurlsa::pth` which injects into a process). |

## Patterns
- High volume of Admin logins (Type 3) to different hosts using NTLM, often with the same Logon ID.
- Access to `ADMIN$` shares using NTLM instead of Kerberos.
