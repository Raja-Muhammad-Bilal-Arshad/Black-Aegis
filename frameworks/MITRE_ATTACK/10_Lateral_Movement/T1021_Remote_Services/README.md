# T1021 - Remote Services

## Description
Adversaries may use valid accounts to log into a service specifically designed to accept remote connections, such as SSH, RDP, or SMB/Windows Admin Shares.

## Sub-techniques
- **T1021.001**: Remote Desktop Protocol (RDP)
- **T1021.002**: SMB/Windows Admin Shares (PsExec)
- **T1021.006**: Windows Remote Management (WinRM)

## Analysis
- **PsExec**: The classic tool. Drops a service binary (PSEXESVC) on the target. Extremely noisy and flagged by EDR.
- **WinRM**: PowerShell Remoting. Uses ports 5985 (HTTP) and 5986 (HTTPS). Much stealthier if "Living off the Land".

## Best Practices
- **Defense**: Disable File and Printer Sharing (SMB) if not needed. Enforce Strong Passwords. Use Tiered Administration (Admins don't log into User workstations).
- **Log**: Event ID 4624 (Logon Type 3 - Network).

## References
- [MITRE T1021](https://attack.mitre.org/techniques/T1021/)
