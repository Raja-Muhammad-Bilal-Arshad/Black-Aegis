# DLP Bypass Guide: Alternative Protocols (T1048)

## Why It Works
Many firewalls allow ICMP (Ping) and DNS (UDP 53) outbound by default for troubleshooting and connectivity. DLP systems often focus on TCP streams (HTTP, SMTP, FTP) and ignore these stateless protocols.

## Evasion Techniques
1.  **Low and Slow**: Send 1 byte per ping. Millions of pings. Hard to detect if scattered over weeks.
2.  **Protocol Compliance**: Ensure the headers look legitimate. Malformed packets are dropped by firewalls.
3.  **Encoding**: Hex encode data in the "Data" field of the ICMP Echo Request.
