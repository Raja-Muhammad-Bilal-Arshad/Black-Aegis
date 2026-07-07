# T1021.006 - WinRM Hunting Guide

## Log Artifacts

| Event ID | Source | Description |
|----------|--------|-------------|
| **4624** | Security | Successful Logon. Look for **Logon Type 3** (Network) using Auth Package `Kerberos` or `Negotiate`. |
| **6** | Microsoft-Windows-WinRM/Operational | "Creating WS-Man Session". |
| **91** | Microsoft-Windows-WinRM/Operational | "Creating Shell". |

## Indicators
- `wsmprovhost.exe` process (host process for WinRM).
- Unexpected PowerShell execution from Network logon sessions.
