---
name: threat-intelligence
description: APT TTP mapping, threat actor profiling, intelligence collection.
---

# Threat Intelligence Protocol

## 1. Intelligence Collection

### OSINT Sources
| Source | Type | Information |
|--------|------|-------------|
| MITRE ATT&CK | Framework | TTPs, techniques, procedures |
| AlienVault OTX | IOC feed | Indicators of compromise |
| VirusTotal | Malware analysis | File/network behavior |
| Shodan/Censys | Infrastructure | Exposed services |
| Security blogs | Analysis | New threats, campaigns |
| Dark web | Underground | Tools, services, data |

### IOC Types
| Type | Example |
|------|---------|
| IP Address | `192.168.1.100` |
| Domain | `evil.com` |
| URL | `https://evil.com/payload` |
| File Hash | `sha256:abc123...` |
| Email Address | `attacker@evil.com` |
| CVE | `CVE-2024-12345` |

## 2. APT Profiling

### Threat Actor Template
```markdown
# Threat Actor: [NAME]

## Overview
- **Aliases**: [Other names]
- **Region**: [Country/Region]
- **Active Since**: [Year]
- **Targets**: [Industries/Regions]
- **Motivation**: [Espionage, Financial, Hacktivism]

## TTPs (MITRE ATT&CK)
| Tactic | Technique | ID |
|--------|-----------|-----|
| Initial Access | Spearphishing | T1566 |
| Execution | PowerShell | T1059.001 |
| Persistence | Registry Run Keys | T1547.001 |
| Privilege Escalation | Bypass UAC | T1548.002 |
| Defense Evasion | Obfuscated Files | T1027 |
| Credential Access | LSASS Memory | T1003.001 |
| Lateral Movement | Remote Services | T1021 |
| Exfiltration | Over C2 Channel | T1041 |

## Infrastructure
- C2: HTTPS, DNS, Custom protocols
- Domains: Algorithmically generated (DGA)
- Hosting: Bulletproof VPS

## Attribution Confidence
- **High**: [Evidence]
- **Medium**: [Evidence]
```

## 3. TTP Mapping Process

```
1. Collect observations (logs, IOCs, behavior)
2. Map to MITRE ATT&CK technique IDs
3. Identify tactic progression (kill chain)
4. Compare to known threat actor profiles
5. Assess intent and capability
6. Produce intelligence report
```

## 4. Intelligence Analysis

### Diamond Model
```
Adversary ←→ Infrastructure
    ↕              ↕
Capability ←→ Victim
```

### Kill Chain Analysis
```
Recon → Weaponize → Deliver → Exploit → Install → C2 → Actions
```

## 5. Reporting

### Intelligence Report Structure
1. **Executive Summary**: Key findings, impact
2. **Technical Details**: IOCs, TTPs, evidence
3. **Attribution**: Threat actor mapping
4. **Recommendations**: Mitigations, detections
5. **Appendices**: Raw data, IOC lists

## 6. Tools

| Tool | Purpose |
|------|---------|
| MITRE ATT&CK Navigator | TTP visualization |
| MISP | Threat intelligence platform |
| TheHive | Incident response |
| Cortex | Observable analysis |
| OpenCTI | Intelligence management |
| greynoise | Internet scanning data |
