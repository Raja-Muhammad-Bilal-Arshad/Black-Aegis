# T1021.001 - RDP Hunting Guide

## Log Artifacts

| Event ID | Source | Description |
|----------|--------|-------------|
| **4624** | Security | Successful Logon. Look for **Logon Type 10** (RemoteInteractive). |
| **4778** | Security | A session was reconnected to a Window Station. |
| **1149** | TerminalServices-LocalSessionManager | User authentication succeeded. |
| **21** | TerminalServices-LocalSessionManager | Session logon succeeded. |

## Query Patterns
- `EventID=4624 AND LogonType=10`
- Source IP in Event 4624 WorkstationName/IpAddress fields.
