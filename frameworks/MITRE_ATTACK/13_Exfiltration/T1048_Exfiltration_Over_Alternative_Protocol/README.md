# T1048.003 - Exfiltration Over Alternative Protocol

## Description
Adversaries may steal data by exfiltrating it over a different protocol than that used for Command and Control.

## Analysis
- **DNS Exfiltration**: Very effective because almost all corporate networks allow DNS (UDP 53) outbound to resolve hostnames.
- **Mechanism**: The attacker sets up a malicious NS record. The victim queries `subdomain.attacker.com`. The attacker logs the subdomain (which contains the encoded stolen data).

## Best Practices
- **Defense**: DNS Sinkholing.
- **Detection**: High volume of queries to unique subdomains of a single domain. Long query strings.

## References
- [MITRE T1048](https://attack.mitre.org/techniques/T1048/)
