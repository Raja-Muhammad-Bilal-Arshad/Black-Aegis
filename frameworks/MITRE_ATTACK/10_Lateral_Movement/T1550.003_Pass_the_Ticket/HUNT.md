# T1550.003 - Pass the Ticket Hunting Guide

## Log Artifacts

| Event ID | Source | Description |
|----------|--------|-------------|
| **4769** | Security | Kerberos Service Ticket Request. Look for same Ticket ID being used from different IP addresses. |
| **4768** | Security | Kerberos TGT Request. |

## Indicators
- **Event 4769**: Account Name does not match the Computer Name/User initiating the request.
- Use of RC4 encryption (0x17) when AES (0x12) is available/enforced.
