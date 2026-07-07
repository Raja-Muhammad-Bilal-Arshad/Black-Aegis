# Black Aegis Red Team Architecture

> Elite Offensive Security & Adversary Simulation Framework
> **"We do not test defenses. We become the threat."**
> **Free for companies who cannot afford expensive audits.**

---

## Overview

**Black Aegis** is a **full-spectrum offensive security architecture** designed for penetration testers, exploit developers, and red team operators. It provides a complete, free alternative to expensive commercial security audit tools.

The framework includes:
- **20 Elite AI Agents** (ranked T0-T5)
- **31 Offensive Capabilities** (skills)
- **12 Kill-Chain Workflows** (slash commands)
- **992+ MITRE ATT&CK Techniques** with executable scripts
- **Automated Orchestration Engine** with engagement management
- **Professional Report Generation**

---

## Directory Structure

```
Pentesting_agent_Company/
├── agents/                          # 20 Elite Operators (Rank-Based)
│   ├── supreme-architect.md         # T0 - Unit Commander
│   ├── red-ops-master.md            # T1 - Ops Lead
│   ├── exploit-research-master.md   # T1 - R&D Lead
│   ├── malware-domain-commander.md  # T2 - Malware Lead
│   ├── network-domain-commander.md  # T2 - Network Lead
│   ├── cloud-domain-commander.md    # T2 - Cloud Lead
│   ├── application-domain-commander.md  # T2 - Web Lead
│   ├── human-domain-commander.md    # T2 - Human Lead
│   ├── principal-exploit-dev.md     # T3 - Exploit Dev
│   ├── principal-reverse-engineer.md # T3 - RE Expert
│   ├── principal-cloud-attacker.md  # T3 - Cloud Operator
│   ├── principal-network-attacker.md # T3 - Network Operator
│   ├── principal-social-engineer.md # T3 - SE Operator
│   ├── firmware-hardware-specialist.md  # T4 - Hardware
│   ├── wireless-rf-specialist.md    # T4 - Signals
│   ├── anti-detection-specialist.md # T4 - Evasion
│   ├── insider-threat-simulator.md  # T4 - Insider
│   ├── physical-breach-specialist.md # T4 - Physical
│   ├── threat-intel-officer.md      # T5 - Intel
│   └── validation-reporting-officer.md # T5 - QA/Reporting
│
├── skills/                          # 31 Offensive Capabilities
│   ├── malware-design.md            # Custom C2, loaders, payloads
│   ├── av-evasion-expert.md         # AMSI bypass, syscall hooking
│   ├── memory-corruption.md         # Buffer overflows, UAF, ROP
│   ├── shellcode-dev.md             # PIC shellcode, egg hunters
│   ├── edr-bypass.md                # EDR/AV evasion, unhooking
│   ├── siem-blinding.md             # Log evasion, false flags
│   ├── ad-forest-domination.md      # AD compromise, Golden Ticket
│   ├── kerberos-abuse.md            # Kerberoasting, AS-REP Roast
│   ├── lateral-movement.md          # SMB/WinRM pivoting
│   ├── cloud-killchain.md           # AWS/Azure/GCP attacks
│   ├── cloud-persistence.md         # Stealth cloud backdoors
│   ├── container-escape.md          # Docker/K8s breakout
│   ├── advanced-web-exploitation.md # Deserialization, SSTI
│   ├── api-logic-abuse.md           # BOLA, Mass Assignment
│   ├── osint-deep-dive.md           # Passive recon, dark web
│   ├── spear-phishing-ops.md        # Phishing campaigns
│   ├── psychological-profiling.md   # Target profiling, pretexting
│   ├── physical-breach.md           # Lock picking, badge clone
│   ├── insider-simulation.md        # Legitimate access abuse
│   ├── data-exfiltration.md         # DNS exfil, steganography
│   ├── mitre-mapping.md             # ATT&CK technique mapping
│   ├── opsec-control.md             # Log cleaning, timestomping
│   ├── reporting-standards.md       # Professional reporting
│   ├── threat-intelligence.md       # APT profiling, IOC analysis
│   ├── zero-day-strategy.md         # Vuln research, disclosure
│   ├── exploit-weaponization.md     # Payload dev, shellcode wrap
│   ├── hardware-hacking.md          # JTAG, UART, IoT
│   ├── firmware-extraction.md       # Firmware dumping & analysis
│   ├── wifi-cracking.md             # WPA/WPA2/WPA3 attacks
│   ├── rf-signal-attack.md          # SDR, RFID, Bluetooth
│   └── [additional skills in skills/]
│
├── workflows/                       # 12 Kill-Chain Procedures
│   ├── recon.md                     # /recon - Reconnaissance
│   ├── weaponize.md                 # /weaponize - Payload development
│   ├── initial-access.md            # /initial-access - Gaining entry
│   ├── evade.md                     # /evade - Defense evasion
│   ├── enumerate.md                 # /enumerate - Internal discovery
│   ├── privesc.md                   # /privesc - Privilege escalation
│   ├── lateral.md                   # /lateral - Lateral movement
│   ├── persist.md                   # /persist - Maintaining access
│   ├── collect.md                   # /collect - Data collection
│   ├── exfiltrate.md                # /exfiltrate - Data extraction
│   ├── impact.md                    # /impact - Achieving objectives
│   └── report.md                    # /report - Documentation
│
├── rules/                           # Engagement Doctrine
│   └── doctrine.md                  # ROE, Stealth Levels, Ethics
│
├── scripts/                         # Core System Scripts
│   ├── black_aegis.py               # Main orchestrator (entry point)
│   ├── generate_mitre_framework.py  # MITRE technique generator
│   ├── report_generator.py          # Automated report generation
│   ├── verify_tools.sh              # Tool verification
│   └── check_tools.sh               # Quick tool check
│
├── frameworks/                      # Security Frameworks
│   ├── MITRE_ATTACK.md              # Quick reference lookup
│   ├── MITRE_ATTACK/                # Full technique library
│   │   ├── 01_Reconnaissance/       # 93 techniques
│   │   ├── 02_Resource_Development/ # 47 techniques
│   │   ├── 03_Initial_Access/       # 60 techniques
│   │   ├── 04_Execution/            # 39 techniques
│   │   ├── 05_Persistence/          # 52 techniques
│   │   ├── 06_Privilege_Escalation/ # 18 techniques
│   │   ├── 07_Defense_Evasion/      # 120+ techniques
│   │   ├── 08_Credential_Access/    # 45+ techniques
│   │   ├── 09_Discovery/            # 40+ techniques
│   │   ├── 10_Lateral_Movement/     # 25+ techniques
│   │   ├── 11_Collection/           # 35+ techniques
│   │   ├── 12_Command_Control/      # 30+ techniques
│   │   ├── 13_Exfiltration/         # 20+ techniques
│   │   ├── 14_Impact/               # 18+ techniques
│   │   └── enterprise-attack.json   # Full ATT&CK dataset
│   ├── OWASP_TOP_10.md              # Web security standard
│   └── NIST_SP_800_115.md           # Pen testing process
│
├── intelligence/                    # Intel Gathering
│   └── target_profile_template.md   # Target profiling template
│
├── Resources/                       # Reference Materials
│   ├── Books/                       # PDFs, ATT&CK Excel
│   └── Github/                      # Open-source tools
│
├── engagements/                     # Active Engagement Projects
├── reports/                         # Generated Reports
│
├── install.sh                       # Full installation script
├── ARCHITECTURE.md                  # This file
├── BUILD_LOG.md                     # Build history
└── PROGRESS.md                      # Project progress tracker
```

---

## The Elite Operators (20)

**Strict Hierarchy:** Tier 0 (Supreme) → Tier 1 (Strategic) → Tier 2 (Domain) → Tier 3 (Principal) → Tier 4 (Specialist) → Tier 5 (Support)

| Rank | Agent | Focus | Core Skills |
|------|-------|-------|-------------|
| **T0** | `supreme-architect` | Unit Commander | `doctrine-enforcement`, `mission-override` |
| **T1** | `red-ops-master` | Ops Lead | `opsec-control`, `multi-vector-coordination` |
| **T1** | `exploit-research-master` | R&D Lead | `zero-day-strategy`, `exploit-weaponization` |
| **T2** | `malware-domain-commander` | Malware Lead | `malware-design`, `av-evasion-expert` |
| **T2** | `network-domain-commander` | Network Lead | `ad-forest-domination`, `network-warfare` |
| **T2** | `cloud-domain-commander` | Cloud Lead | `cloud-killchain`, `iam-privesc` |
| **T2** | `application-domain-commander` | Web Lead | `advanced-web-exploitation`, `api-logic-abuse` |
| **T2** | `human-domain-commander` | PsyOps Lead | `psychological-profiling`, `physical-breach-tactics` |
| **T3** | `principal-exploit-dev` | Exploit Dev | `memory-corruption`, `shellcode-dev` |
| **T3** | `principal-reverse-engineer` | RE Expert | `static-analysis`, `dynamic-instrumentation` |
| **T3** | `principal-cloud-attacker` | Cloud Operator | `cloud-persistence`, `serverless-attack` |
| **T3** | `principal-network-attacker` | Network Operator | `lateral-movement`, `kerberos-abuse` |
| **T3** | `principal-social-engineer` | SE Operator | `spear-phishing-ops`, `osint-deep-dive` |
| **T4** | `firmware-hardware-specialist` | Hardware | `hardware-hacking`, `firmware-extraction` |
| **T4** | `wireless-rf-specialist` | Signals | `rf-signal-attack`, `wifi-cracking` |
| **T4** | `anti-detection-specialist` | Evasion | `edr-bypass`, `siem-blinding` |
| **T4** | `insider-threat-simulator` | Insider | `data-exfiltration`, `insider-simulation` |
| **T4** | `physical-breach-specialist` | Physical | `lock-bypass`, `badge-cloning` |
| **T5** | `threat-intel-officer` | Intel | `mitre-mapping`, `threat-intelligence` |
| **T5** | `validation-reporting-officer` | QA/Reporting | `reporting-standards`, `exploit-validation` |

---

## Offensive Capabilities (31 Skills)

### Malware & Evasion (6)
| Skill | Description |
|-------|-------------|
| `malware-design` | Custom C2, loaders, polyglot payloads |
| `av-evasion-expert` | AMSI bypass, syscall hooking, unhooking |
| `memory-corruption` | Buffer overflows, UAF, format strings, ROP |
| `shellcode-dev` | PIC shellcode, egg hunters, encoders |
| `edr-bypass` | EDR/AV evasion, process injection, syscalls |
| `siem-blinding` | Log evasion, false flags, timestomping |

### Network & Active Directory (4)
| Skill | Description |
|-------|-------------|
| `ad-forest-domination` | Golden Ticket, DCSync, BloodHound paths |
| `kerberos-abuse` | Kerberoasting, AS-REP Roasting, delegation abuse |
| `lateral-movement` | SMB/WinRM pivoting, SSH tunneling, RDP |
| `wifi-cracking` | WPA/WPA2/WPA3 attacks, Evil Twin, PMKID |

### Cloud & Infrastructure (3)
| Skill | Description |
|-------|-------------|
| `cloud-killchain` | AWS/Azure/GCP attack paths |
| `cloud-persistence` | Stealth persistence, Lambda backdoors |
| `container-escape` | Docker/K8s breakout, namespace abuse |

### Web & API (2)
| Skill | Description |
|-------|-------------|
| `advanced-web-exploitation` | Deserialization, SSTI, Request Smuggling |
| `api-logic-abuse` | BOLA, Mass Assignment, GraphQL injection |

### Human & Physical (5)
| Skill | Description |
|-------|-------------|
| `osint-deep-dive` | Passive recon, dark web correlation |
| `spear-phishing-ops` | Payload delivery, credential harvesting |
| `psychological-profiling` | Target profiling, pretext development |
| `physical-breach` | Lock picking, badge cloning, CCTV bypass |
| `insider-simulation` | Legitimate access abuse, social engineering |

### Doctrine & Intelligence (6)
| Skill | Description |
|-------|-------------|
| `mitre-mapping` | Mapping actions to ATT&CK Matrix |
| `opsec-control` | Log cleaning, time-stomp, proxy chains |
| `reporting-standards` | Executive summaries vs Technical breakdown |
| `threat-intelligence` | APT TTP mapping, intelligence collection |
| `zero-day-strategy` | Vulnerability research, disclosure decisions |
| `exploit-weaponization` | Payload development, shellcode wrapping |

### Hardware & Signals (2)
| Skill | Description |
|-------|-------------|
| `hardware-hacking` | JTAG, UART, IoT exploitation |
| `firmware-extraction` | Firmware dumping, reverse engineering |
| `rf-signal-attack` | SDR, RFID cloning, Bluetooth attacks |

---

## Kill-Chain Workflows (12)

| Command | Purpose | Phase |
|---------|---------|-------|
| `/recon` | Passive/Active Intel Gathering | Reconnaissance |
| `/weaponize` | Build payloads & exploits | Resource Dev |
| `/initial-access` | Execute phish or exploit | Initial Access |
| `/evade` | Bypass EDR/AV/Firewalls | Defense Evasion |
| `/enumerate` | Internal discovery & mapping | Discovery |
| `/privesc` | Elevate to System/Root/Admin | Privilege Escalation |
| `/lateral` | Pivot to other hosts | Lateral Movement |
| `/persist` | Install backdoors/implants | Persistence |
| `/collect` | Identify & stage sensitive data | Collection |
| `/exfiltrate` | Steal data covertly | Exfiltration |
| `/impact` | Execute objective (Ransom/Wipe) | Impact |
| `/report` | Generate final engagement report | Reporting |

---

## Usage

### Quick Start
```bash
# Install dependencies
./install.sh

# Start interactive mode
python3 scripts/black_aegis.py -i

# Create an engagement
python3 scripts/black_aegis.py --engage "client_name" "target.com"

# Run a workflow
python3 scripts/black_aegis.py --workflow recon

# Check installed tools
python3 scripts/black_aegis.py --tools

# Generate report
python3 scripts/report_generator.py engagements/client_name
```

### Interactive Mode Commands
```
black-aegis> help          # Show available commands
black-aegis> agents        # List all 20 agents
black-aegis> skills        # List all 31 skills
black-aegis> workflows     # List all 12 workflows
black-aegis> techniques    # Browse MITRE techniques
black-aegis> engage <n> <t> # Create engagement
black-aegis> workflow <name> # Run workflow
black-aegis> tools         # Verify installed tools
black-aegis> report <eng>  # Generate report
```

---

## Rules of Engagement (Doctrine)

### 1. Stealth Levels (DEFCON)
- **Level 1: SILENT** - Zero direct contact (Passive Recon)
- **Level 2: COVERT** - Local traffic only (Standard Operations)
- **Level 3: LOUD** - Mass scanning (Requires T0 Override)

### 2. Data Ethics
- No exfiltration of real PII (only proofs)
- No DoS on production systems
- Immediate abort for healthcare/critical infrastructure
- Complete cleanup after engagement

### 3. Safety Protocols
- Every file dropped must be logged
- Every user created must be deleted
- Every firewall rule changed must be reverted

---

## MITRE ATT&CK Coverage

Each technique directory contains:
- `TACTICAL_GUIDE.md` - Step-by-step execution guide
- `DETECTION.md` - Detection logic + Sigma rules
- `OPSEC_WARNINGS.md` - Operational security warnings
- Executable script (`.sh`) - Ready-to-use attack tool

**Total: 992 technique directories across 14 tactics**

---

## For Small Companies

This framework is designed to be **completely free** and usable by small companies that cannot afford expensive security audits. It provides:

1. **Complete MITRE ATT&CK coverage** with ready-to-use scripts
2. **Standardized methodology** (NIST SP 800-115, OWASP)
3. **Automated reporting** for professional deliverables
4. **AI-assisted guidance** through the agent hierarchy
5. **Free tools integration** (open-source security tools)

---

## Legal Notice

**AUTHORIZED TESTING ONLY**: This framework is for authorized penetration testing and security assessments only. Unauthorized access to computer systems is illegal. Always obtain written permission before testing.

---

*Black Aegis v2.0.0 - "We do not test defenses. We become the threat."*
