# T1021.002 - SMB Hunting Guide

## Log Artifacts

| Event ID | Source | Description |
|----------|--------|-------------|
| **4624** | Security | Successful Logon. Look for **Logon Type 3** (Network). |
| **5140** | Security | A network share object was accessed (e.g., `\\*\ADMIN$`, `\\*\C$`). |
| **5145** | Security | A network share object was checked to see whether client can be granted desired access. Detailed share access. |

## Smoking Guns
- Access to `ADMIN$` or `C$` shares usually indicates administrative activity.
- PsExec (and Cobalt Strike psexec) creates a named pipe (e.g., `\PSEXESVC`).
