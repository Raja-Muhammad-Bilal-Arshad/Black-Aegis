
# BLACK AEGIS

### Elite Offensive Security & Adversary Simulation Framework

**"We do not test defenses. We become the threat."**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
[![Issues](https://img.shields.io/github/issues/badges/BlackAegis.svg)](https://github.com/BlackAegis/BlackAegis/issues)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![MITRE ATT&CK](https://img.shields.io/badge/MITRE%20ATT%26CK-v16.1-red.svg)](https://attack.mitre.org/)

A **free, open-source** penetration testing framework designed for security professionals and small companies who cannot afford expensive commercial audit tools.

[Getting Started](#-getting-started) • [Features](#-features) • [Documentation](#-documentation) • [Contributing](#-contributing) • [License](#-license)

</div>

---

## What is Black Aegis?

Black Aegis is a **comprehensive, AI-powered penetration testing framework** that provides:

- **20 Elite AI Agents** working in a military-style hierarchy
- **30 Offensive Capabilities** (skills) covering every attack vector
- **992+ MITRE ATT&CK Techniques** with ready-to-execute scripts
- **12 Kill-Chain Workflows** mapping to the full attack lifecycle
- **Automated Orchestration** with engagement management
- **Professional Report Generation** for client deliverables

Built on the MITRE ATT&CK framework, NIST SP 800-115, and OWASP standards, Black Aegis provides enterprise-grade penetration testing capabilities **completely free**.

> **Mission**: We believe every company deserves access to security testing, regardless of budget. Black Aegis exists to democratize cybersecurity.

---

## Table of Contents

- [Features](#-features)
- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [Usage Guide](#-usage-guide)
- [Architecture](#-architecture)
- [Agents](#-agents)
- [Skills](#-skills)
- [Workflows](#-workflows)
- [MITRE ATT&CK Coverage](#-mitre-attck-coverage)
- [Frameworks](#-frameworks)
- [Directory Structure](#-directory-structure)
- [Statistics](#-statistics)
- [Contributing](#-contributing)
- [Roadmap](#-roadmap)
- [License](#-license)
- [Disclaimer](#-disclaimer)
- [Acknowledgments](#-acknowledgments)

---

## Features

### Core Capabilities

| Feature | Description |
|---------|-------------|
| **AI Agent System** | 20 specialized agents with defined roles, skills, and hierarchy |
| **MITRE ATT&CK Integration** | 992+ technique directories with executable scripts |
| **Kill-Chain Workflows** | 12 slash commands mapping to the full attack lifecycle |
| **Engagement Management** | Create, track, and manage penetration test engagements |
| **Automated Reporting** | Generate professional client-ready reports |
| **Tool Verification** | Check that all required tools are installed |
| **Interactive Mode** | Full CLI with command palette and help system |
| **Modular Skills** | 30 plug-and-play capability modules |

### Attack Coverage

| Domain | Skills |
|--------|--------|
| **Malware & Evasion** | Custom C2, AMSI bypass, memory corruption, shellcode development, EDR bypass, SIEM blinding |
| **Network & AD** | AD forest domination, Kerberos abuse, lateral movement, WiFi cracking |
| **Cloud** | AWS/Azure/GCP attack chains, container escapes, cloud persistence |
| **Web & API** | Deserialization, SSTI, API logic abuse, auth bypass |
| **Human & Physical** | OSINT, spear phishing, psychological profiling, lock picking, badge cloning |
| **Hardware** | JTAG, UART, firmware extraction, SDR, RFID cloning |
| **Intelligence** | APT profiling, threat intelligence, zero-day research |

### What You Can Do

- **Full Penetration Tests**: From reconnaissance to reporting
- **Red Team Engagements**: APT-level adversary simulation
- **Vulnerability Assessments**: Systematic security testing
- **Compliance Audits**: NIST, OWASP, MITRE-aligned assessments
- **Security Training**: Learn offensive techniques safely
- **Incident Response**: Understand attacker methodologies

---

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/BlackAegis/BlackAegis.git
cd BlackAegis/Pentesting_agent_Company

# 2. Install dependencies
./install.sh

# 3. Start the framework
python3 scripts/black_aegis.py -i

# 4. Create an engagement
black-aegis> engage my_client target.com

# 5. Start testing
black-aegis> workflow recon
```

---

## Installation

### Prerequisites

- **Operating System**: Linux (Kali, Ubuntu, Debian) or macOS
- **Python**: 3.8 or higher
- **Privileges**: sudo access for tool installation

### Automatic Installation

```bash
cd Pentesting_agent_Company
chmod +x install.sh
./install.sh
```

The install script will:
1. Update system packages
2. Install 13+ system tools (nmap, masscan, hydra, etc.)
3. Install Python dependencies (impacket, scapy, pwntools, etc.)
4. Install Go tools (gobuster, subfinder, kerbrute)
5. Set up project structure
6. Verify the installation

### Manual Installation

If you prefer manual setup:

```bash
# System tools
sudo apt update
sudo apt install -y nmap masscan hydra nikto curl wget git python3 python3-pip whois netcat-openbsd proxychains4

# Python packages
pip install pyyaml openpyxl requests beautifulsoup4 impacket scapy pwntools

# Go tools (optional)
go install github.com/OJ/gobuster/v3@latest
go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
```

### Verify Installation

```bash
python3 scripts/black_aegis.py --tools
```

Expected output:
```
╔══════════════════════════════════════════╗
║         TOOL VERIFICATION                ║
╚══════════════════════════════════════════╝
  [✓] curl                      │ HTTP requests
  [✓] evil-winrm                │ WinRM shell
  [✓] git                       │ Version control
  [✓] gobuster                  │ Directory enumeration
  [✓] hydra                     │ Brute force
  [✓] impacket-psexec           │ Windows lateral movement
  [✓] masscan                   │ Fast port scanning
  [✓] nikto                     │ Web vulnerability scanning
  [✓] nmap                      │ Network scanning
  [✓] proxychains               │ Proxy chains
  [✓] python3                   │ Scripting
  [✓] sqlmap                    │ SQL injection
  [✓] wget                      │ File downloads
  Installed: 13/13  │  Missing: 0
```

---

## Usage Guide

### Command Line Interface

Black Aegis provides both interactive and command-line modes.

#### Interactive Mode

```bash
python3 scripts/black_aegis.py -i
```

```
╔══════════════════════════════════════════════════════════════╗
║                    BLACK AEGIS v2.0.0                     ║
║              Elite Offensive Security Framework             ║
║                    "Black Aegis"                        ║
╠══════════════════════════════════════════════════════════════╣
║  Agents:  20  │  Skills:  30  │  Workflows:  12           ║
║  MITRE Techniques: 992+  │  Scripts: 1312+                ║
╚══════════════════════════════════════════════════════════════╝

Type 'help' for available commands.

black-aegis>
```

#### Command Line Mode

```bash
# List all agents
python3 scripts/black_aegis.py --list agents

# List all skills
python3 scripts/black_aegis.py --list skills

# List all workflows
python3 scripts/black_aegis.py --list workflows

# List MITRE techniques
python3 scripts/black_aegis.py --list techniques

# Create an engagement
python3 scripts/black_aegis.py --engage "client_name" "target.com"

# Run a workflow
python3 scripts/black_aegis.py --workflow recon

# Check tools
python3 scripts/black_aegis.py --tools

# Generate a report
python3 scripts/report_generator.py engagements/client_name
```

### Interactive Commands

| Command | Description | Example |
|---------|-------------|---------|
| `help` | Show available commands | `help` |
| `agents` | List all 20 agents | `agents` |
| `skills` | List all 30 skills | `skills` |
| `workflows` | List all 12 workflows | `workflows` |
| `techniques` | Browse MITRE techniques | `techniques` |
| `techniques <tactic>` | Filter by tactic | `techniques initial-access` |
| `engage <name> <target>` | Create engagement | `engage acme_corp example.com` |
| `workflow <name>` | Run a workflow | `workflow recon` |
| `tools` | Verify installed tools | `tools` |
| `report <engagement>` | Generate report | `report acme_corp` |
| `version` | Show version info | `version` |
| `exit` / `quit` | Exit framework | `exit` |

### Workflow Commands

| Command | Phase | Description |
|---------|-------|-------------|
| `/recon` | Reconnaissance | Passive/active information gathering |
| `/weaponize` | Resource Development | Build payloads and exploits |
| `/initial-access` | Initial Access | Execute phishing or exploitation |
| `/evade` | Defense Evasion | Bypass EDR/AV/Firewalls |
| `/enumerate` | Discovery | Internal system enumeration |
| `/privesc` | Privilege Escalation | Elevate to SYSTEM/root/admin |
| `/lateral` | Lateral Movement | Pivot to other hosts |
| `/persist` | Persistence | Install backdoors/implants |
| `/collect` | Collection | Identify and stage sensitive data |
| `/exfiltrate` | Exfiltration | Steal data covertly |
| `/impact` | Impact | Execute objective (simulation) |
| `/report` | Reporting | Generate final engagement report |

### Engagement Workflow

```bash
# Step 1: Create engagement
black-aegis> engage acme_corp 192.168.1.0/24

# Step 2: Start reconnaissance
black-aegis> workflow recon

# Step 3: Weaponize (build payloads)
black-aegis> workflow weaponize

# Step 4: Initial access
black-aegis> workflow initial-access

# Step 5: Post-exploitation
black-aegis> workflow privesc
black-aegis> workflow lateral
black-aegis> workflow persist

# Step 6: Data collection
black-aegis> workflow collect

# Step 7: Generate report
black-aegis> report acme_corp
```

### Running MITRE Technique Scripts

Each of the 992 MITRE technique directories contains executable scripts:

```bash
# Navigate to a technique
cd frameworks/MITRE_ATTACK/03_Initial_Access/T1566_Phishing/

# Run the technique script
./execute.sh

# Read the tactical guide
cat TACTICAL_GUIDE.md

# Check detection logic
cat DETECTION.md

# Review OPSEC warnings
cat OPSEC_WARNINGS.md
```

### Generating MITRE Framework

To regenerate the entire MITRE technique library:

```bash
cd Pentesting_agent_Company
python3 scripts/generate_mitre_framework.py
```

This reads the MITRE ATT&CK Excel file and generates:
- 992+ technique directories
- 2520+ markdown documentation files
- 1242+ executable bash scripts

---

## Architecture

### System Design

```
                    ┌─────────────────────┐
                    │   SUPREME ARCHITECT  │
                    │      (Tier 0)        │
                    │  Doctrine & Ethics   │
                    └──────────┬──────────┘
                               │
            ┌──────────────────┼──────────────────┐
            │                  │                  │
    ┌───────┴───────┐  ┌──────┴──────┐  ┌───────┴───────┐
    │  RED OPS MASTER│  │  EXPLOIT    │  │  THREAT INTEL │
    │    (Tier 1)    │  │  RESEARCH   │  │   OFFICER     │
    │   Orchestrator │  │   MASTER    │  │   (Tier 5)    │
    └───────┬───────┘  │   (Tier 1)  │  └───────────────┘
            │          └──────┬──────┘
            │                 │
    ┌───────┴─────────────────┴─────────────────┐
    │              DOMAIN COMMANDERS             │
    │                 (Tier 2)                   │
    │  Malware │ Network │ Cloud │ Web │ Human   │
    └───────────────────┬───────────────────────┘
                        │
    ┌───────────────────┴───────────────────────┐
    │           PRINCIPAL OPERATORS              │
    │               (Tier 3)                     │
    │  Exploit Dev │ RE │ Cloud │ Network │ SE   │
    └───────────────────┬───────────────────────┘
                        │
    ┌───────────────────┴───────────────────────┐
    │              SPECIALISTS                   │
    │              (Tier 4)                      │
    │  Firmware │ Wireless │ EDR │ Insider │ Phys│
    └───────────────────────────────────────────┘
```

### Agent Hierarchy

| Tier | Agents | Responsibility |
|------|--------|----------------|
| **T0** | Supreme Architect | Final authority, doctrine enforcement, mission override |
| **T1** | Red Ops Master, Exploit Research Master | Campaign orchestration, R&D decisions |
| **T2** | 5 Domain Commanders | Malware, Network, Cloud, Web, Human domain leads |
| **T3** | 5 Principal Operators | Exploit dev, RE, Cloud, Network, Social Engineering |
| **T4** | 5 Specialists | Firmware, Wireless, EDR bypass, Insider, Physical |
| **T5** | 2 Officers | Threat intelligence, Validation & Reporting |

### Data Flow

```
User Request → Agent Selection → Skill Loading → Technique Execution → Reporting
     ↓              ↓                ↓                  ↓                ↓
  Command      Hierarchy        Capabilities        MITRE Scripts    Reports
  Parsing      Resolution       Activation          Execution        Generation
```

---

## Agents

### Tier 0 - Command

| Agent | Role | Description |
|-------|------|-------------|
| `supreme-architect` | Unit Commander | Final authority on doctrine, ethics, and mission override. Decides strategy and resolves conflicts. |

### Tier 1 - Strategic

| Agent | Role | Description |
|-------|------|-------------|
| `red-ops-master` | Ops Lead | Orchestrates live multi-vector campaigns. Manages kill-chain progression and OPSEC. |
| `exploit-research-master` | R&D Lead | Weaponization vs. disclosure decisions. Zero-day strategy and exploit development oversight. |

### Tier 2 - Domain Commanders

| Agent | Domain | Description |
|-------|--------|-------------|
| `malware-domain-commander` | Malware | Custom implants, AV evasion, kernel tradecraft. |
| `network-domain-commander` | Network | Active Directory domination, lateral movement, network warfare. |
| `cloud-domain-commander` | Cloud | AWS/Azure/GCP attack paths, container escapes, IAM abuse. |
| `application-domain-commander` | Web | API logic abuse, authentication bypass, web exploitation. |
| `human-domain-commander` | Human | Social engineering, psychological profiling, physical entry. |

### Tier 3 - Principal Operators

| Agent | Role | Description |
|-------|------|-------------|
| `principal-exploit-dev` | Exploit Dev | Memory corruption, ROP chains, heap exploitation. |
| `principal-reverse-engineer` | RE Expert | Binary analysis, de-obfuscation, dynamic instrumentation. |
| `principal-cloud-attacker` | Cloud Operator | Stealth persistence, metadata abuse, serverless attacks. |
| `principal-network-attacker` | Network Operator | Pivoting, Kerberos abuse, internal network traversal. |
| `principal-social-engineer` | SE Operator | Spear phishing, vishing, pretexting, OSINT deep dives. |

### Tier 4 - Specialists

| Agent | Domain | Description |
|-------|--------|-------------|
| `firmware-hardware-specialist` | Hardware | JTAG, UART, IoT supply chain exploitation. |
| `wireless-rf-specialist` | Signals | Wi-Fi, BLE, SDR, cellular interception. |
| `anti-detection-specialist` | Evasion | EDR bypass, noise reduction, false flags. |
| `insider-threat-simulator` | Insider | Legitimate access abuse, data exfiltration. |
| `physical-breach-specialist` | Physical | Lock picking, badge cloning, CCTV bypass. |

### Tier 5 - Support

| Agent | Role | Description |
|-------|------|-------------|
| `threat-intel-officer` | Intelligence | APT TTP mapping, threat actor profiling, realistic emulation. |
| `validation-reporting-officer` | QA/Reporting | Proof of concept validation, business impact assessment, report generation. |

---

## Skills

### Malware & Evasion (6)

| Skill | Description | Key Techniques |
|-------|-------------|----------------|
| `malware-design` | Custom C2 frameworks, loaders, polyglot payloads | C2 development, payload packaging |
| `av-evasion-expert` | AMSI bypass, syscall hooking, unhooking | PowerShell obfuscation, DLL sideloading |
| `memory-corruption` | Buffer overflows, use-after-free, format strings | ROP chains, heap exploitation, format string bugs |
| `shellcode-dev` | Position-independent code, egg hunters | PIC shellcode, XOR encoding, syscall shellcode |
| `edr-bypass` | EDR/AV evasion, process injection, direct syscalls | SysWhispers, process hollowing, unhooking |
| `siem-blinding` | Log evasion, false flags, timestomping | Log clearing, timestamp manipulation, traffic blending |

### Network & Active Directory (4)

| Skill | Description | Key Techniques |
|-------|-------------|----------------|
| `ad-forest-domination` | Golden Ticket, DCSync, BloodHound paths | Kerberos attacks, trust abuse |
| `kerberos-abuse` | Kerberoasting, AS-REP Roasting, delegation abuse | Ticket forging, service account compromise |
| `lateral-movement` | SMB/WinRM pivoting, SSH tunneling | PsExec, WMI, DCOM, Chisel proxying |
| `wifi-cracking` | WPA/WPA2/WPA3 attacks, Evil Twin | Handshake capture, PMKID, deauth attacks |

### Cloud & Infrastructure (3)

| Skill | Description | Key Techniques |
|-------|-------------|----------------|
| `cloud-killchain` | AWS/Azure/GCP attack paths | IAM abuse, metadata exploitation |
| `cloud-persistence` | Stealth persistence, Lambda backdoors | IAM backdoors, function triggers |
| `container-escape` | Docker/K8s breakout, namespace abuse | Privileged container escape, SA token abuse |

### Web & API (2)

| Skill | Description | Key Techniques |
|-------|-------------|----------------|
| `advanced-web-exploitation` | Deserialization, SSTI, request smuggling | Java/Python deserialization, template injection |
| `api-logic-abuse` | BOLA, mass assignment, GraphQL injection | Authorization bypass, business logic flaws |

### Human & Physical (5)

| Skill | Description | Key Techniques |
|-------|-------------|----------------|
| `osint-deep-dive` | Passive recon, dark web correlation | Social media profiling, breach database searches |
| `spear-phishing-ops` | Payload delivery, credential harvesting | Email crafting, landing page creation |
| `psychological-profiling` | Target profiling, pretext development | Personality assessment, manipulation tactics |
| `physical-breach` | Lock picking, badge cloning, CCTV bypass | RFID cloning, tailgating, dumpster diving |
| `insider-simulation` | Legitimate access abuse, social engineering | Authorized channel exploitation |

### Doctrine & Intelligence (6)

| Skill | Description | Key Techniques |
|-------|-------------|----------------|
| `mitre-mapping` | Mapping actions to ATT&CK Matrix | Technique identification, tactic progression |
| `opsec-control` | Log cleaning, time-stomp, proxy chains | Operational security, evidence cleanup |
| `reporting-standards` | Executive summaries vs technical breakdown | CVSS scoring, remediation guidance |
| `threat-intelligence` | APT TTP mapping, intelligence collection | Diamond model, kill chain analysis |
| `zero-day-strategy` | Vulnerability research, disclosure decisions | Fuzzing, patch diffing, responsible disclosure |
| `exploit-weaponization` | Payload development, shellcode wrapping | msfvenom, ScareCrow, Nimcrypt2 |

### Hardware & Signals (3)

| Skill | Description | Key Techniques |
|-------|-------------|----------------|
| `hardware-hacking` | JTAG, UART, IoT exploitation | Interface identification, firmware extraction |
| `firmware-extraction` | Firmware dumping, reverse engineering | Binwalk analysis, filesystem extraction |
| `rf-signal-attack` | SDR, RFID cloning, Bluetooth attacks | Proxmark3, HackRF, BLE exploitation |

---

## Workflows

### Reconnaissance Phase

```bash
black-aegis> workflow recon
```

**Activities:**
- Passive OSINT (theHarvester, WHOIS, DNS)
- Subdomain enumeration (subfinder, amass)
- Port scanning (masscan, nmap)
- Service identification
- Web screenshotting (gowitness)

### Weaponization Phase

```bash
black-aegis> workflow weaponize
```

**Activities:**
- Exploit selection (searchsploit, Patch Diffs)
- Payload development (msfvenom, ScareCrow)
- Evasion wrapping (Nimcrypt2, custom loaders)
- Staging infrastructure setup

### Initial Access Phase

```bash
black-aegis> workflow initial-access
```

**Activities:**
- Phishing campaign execution
- Public-facing application exploitation
- Valid credential usage
- External remote services access

### Defense Evasion Phase

```bash
black-aegis> workflow evade
```

**Activities:**
- AMSI/ETW bypass
- Process injection
- Syscall direct invocation
- Log clearing and timestomping

### Discovery Phase

```bash
black-aegis> workflow enumerate
```

**Activities:**
- Account enumeration (local, domain)
- Network service scanning
- System information gathering
- Share and file enumeration

### Privilege Escalation Phase

```bash
black-aegis> workflow privesc
```

**Activities:**
- UAC bypass
- Kernel exploit identification
- Token impersonation
- Sudo misconfigurations

### Lateral Movement Phase

```bash
black-aegis> workflow lateral
```

**Activities:**
- PsExec/WinRM/WMI execution
- SSH pivoting
- Kerberoasting
- Pass-the-hash/ticket

### Persistence Phase

```bash
black-aegis> workflow persist
```

**Activities:**
- Registry run keys
- Scheduled tasks
- Service creation
- SSH authorized_keys

### Collection Phase

```bash
black-aegis> workflow collect
```

**Activities:**
- Sensitive file discovery
- Screen capture
- Keylogging
- Clipboard monitoring

### Exfiltration Phase

```bash
black-aegis> workflow exfiltrate
```

**Activities:**
- DNS exfiltration
- HTTPS tunneling
- Cloud storage upload
- Steganography

### Impact Phase

```bash
black-aegis> workflow impact
```

**Activities:**
- Data encryption simulation
- Service disruption simulation
- Defacement simulation
- **SIMULATION ONLY - No real damage**

### Reporting Phase

```bash
black-aegis> workflow report
```

**Activities:**
- Findings aggregation
- CVSS scoring
- Evidence compilation
- Remediation recommendations

---

## MITRE ATT&CK Coverage

### Tactic Distribution

| # | Tactic | Directory | Techniques |
|---|--------|-----------|------------|
| 01 | Reconnaissance | `01_Reconnaissance/` | 93 |
| 02 | Resource Development | `02_Resource_Development/` | 47 |
| 03 | Initial Access | `03_Initial_Access/` | 60 |
| 04 | Execution | `04_Execution/` | 39 |
| 05 | Persistence | `05_Persistence/` | 52 |
| 06 | Privilege Escalation | `06_Privilege_Escalation/` | 18 |
| 07 | Defense Evasion | `07_Defense_Evasion/` | 120+ |
| 08 | Credential Access | `08_Credential_Access/` | 45+ |
| 09 | Discovery | `09_Discovery/` | 40+ |
| 10 | Lateral Movement | `10_Lateral_Movement/` | 25+ |
| 11 | Collection | `11_Collection/` | 35+ |
| 12 | Command and Control | `12_Command_Control/` | 30+ |
| 13 | Exfiltration | `13_Exfiltration/` | 20+ |
| 14 | Impact | `14_Impact/` | 18+ |
| | **TOTAL** | | **992+** |

### Technique Directory Contents

Each of the 992 technique directories contains:

```
T1566_Phishing/
├── TACTICAL_GUIDE.md    # Step-by-step execution guide
├── DETECTION.md         # Detection logic + Sigma rules
├── OPSEC_WARNINGS.md    # Operational security warnings
└── execute.sh           # Ready-to-use attack script
```

### Example: T1566 Phishing

```bash
cd frameworks/MITRE_ATTACK/03_Initial_Access/T1566_Phishing/

# View the tactical guide
cat TACTICAL_GUIDE.md

# Run the attack script
./execute.sh

# Check detection logic
cat DETECTION.md
```

### Regenerating the Framework

```bash
python3 scripts/generate_mitre_framework.py
```

Reads the MITRE ATT&CK Excel (`Resources/Books/MITRE Enterprise ATTACK v16.1.xlsx`) and regenerates all 992+ technique directories.

---

## Frameworks

### MITRE ATT&CK

- **Version**: Enterprise ATT&CK v16.1
- **Coverage**: All 14 tactics, 992+ techniques
- **Files**: `frameworks/MITRE_ATTACK/` directory
- **Quick Reference**: `frameworks/MITRE_ATTACK.md`
- **Source Data**: `frameworks/MITRE_ATTACK/enterprise-attack.json`

### OWASP Top 10 (2025)

- **Coverage**: All 10 vulnerability categories
- **File**: `frameworks/OWASP_TOP_10.md`
- **Focus**: Web application security testing

### NIST SP 800-115

- **Coverage**: Full penetration testing process
- **File**: `frameworks/NIST_SP_800_115.md`
- **Focus**: Federal standard for security testing

---

## Directory Structure

```
Pentesting_agent_Company/
│
├── agents/                              # 20 AI Agent definitions
│   ├── supreme-architect.md             # T0 - Commander
│   ├── red-ops-master.md                # T1 - Ops Lead
│   ├── exploit-research-master.md       # T1 - R&D Lead
│   ├── malware-domain-commander.md      # T2 - Malware Lead
│   ├── network-domain-commander.md      # T2 - Network Lead
│   ├── cloud-domain-commander.md        # T2 - Cloud Lead
│   ├── application-domain-commander.md  # T2 - Web Lead
│   ├── human-domain-commander.md        # T2 - Human Lead
│   ├── principal-exploit-dev.md         # T3 - Exploit Dev
│   ├── principal-reverse-engineer.md    # T3 - RE Expert
│   ├── principal-cloud-attacker.md      # T3 - Cloud Operator
│   ├── principal-network-attacker.md    # T3 - Network Operator
│   ├── principal-social-engineer.md     # T3 - SE Operator
│   ├── firmware-hardware-specialist.md  # T4 - Hardware
│   ├── wireless-rf-specialist.md        # T4 - Signals
│   ├── anti-detection-specialist.md     # T4 - EDR Bypass
│   ├── insider-threat-simulator.md      # T4 - Insider
│   ├── physical-breach-specialist.md    # T4 - Physical
│   ├── threat-intel-officer.md          # T5 - Intel
│   └── validation-reporting-officer.md  # T5 - Reporting
│
├── skills/                              # 30 Capability modules
│   ├── malware-design.md
│   ├── av-evasion-expert.md
│   ├── memory-corruption.md
│   ├── shellcode-dev.md
│   ├── edr-bypass.md
│   ├── siem-blinding.md
│   ├── ad-forest-domination.md
│   ├── kerberos-abuse.md
│   ├── lateral-movement.md
│   ├── cloud-killchain.md
│   ├── cloud-persistence.md
│   ├── container-escape.md
│   ├── advanced-web-exploitation.md
│   ├── api-logic-abuse.md
│   ├── osint-deep-dive.md
│   ├── spear-phishing-ops.md
│   ├── psychological-profiling.md
│   ├── physical-breach.md
│   ├── insider-simulation.md
│   ├── data-exfiltration.md
│   ├── mitre-mapping.md
│   ├── opsec-control.md
│   ├── reporting-standards.md
│   ├── threat-intelligence.md
│   ├── zero-day-strategy.md
│   ├── exploit-weaponization.md
│   ├── hardware-hacking.md
│   ├── firmware-extraction.md
│   ├── wifi-cracking.md
│   └── rf-signal-attack.md
│
├── workflows/                           # 12 Kill-chain procedures
│   ├── recon.md
│   ├── weaponize.md
│   ├── initial-access.md
│   ├── evade.md
│   ├── enumerate.md
│   ├── privesc.md
│   ├── lateral.md
│   ├── persist.md
│   ├── collect.md
│   ├── exfiltrate.md
│   ├── impact.md
│   └── report.md
│
├── rules/                               # Engagement doctrine
│   └── doctrine.md                      # ROE, stealth levels, ethics
│
├── scripts/                             # Core system scripts
│   ├── black_aegis.py                   # Main orchestrator
│   ├── generate_mitre_framework.py      # MITRE generator
│   ├── report_generator.py              # Report generator
│   └── verify_tools.sh                  # Tool verification
│
├── frameworks/                          # Security frameworks
│   ├── MITRE_ATTACK.md                  # Quick reference
│   ├── MITRE_ATTACK/                    # 992 technique directories
│   │   ├── 01_Reconnaissance/
│   │   ├── 02_Resource_Development/
│   │   ├── 03_Initial_Access/
│   │   ├── 04_Execution/
│   │   ├── 05_Persistence/
│   │   ├── 06_Privilege_Escalation/
│   │   ├── 07_Defense_Evasion/
│   │   ├── 08_Credential_Access/
│   │   ├── 09_Discovery/
│   │   ├── 10_Lateral_Movement/
│   │   ├── 11_Collection/
│   │   ├── 12_Command_Control/
│   │   ├── 13_Exfiltration/
│   │   ├── 14_Impact/
│   │   └── enterprise-attack.json
│   ├── OWASP_TOP_10.md
│   └── NIST_SP_800_115.md
│
├── intelligence/                        # Intel gathering
│   └── target_profile_template.md
│
├── Resources/                           # Reference materials
│   ├── Books/                           # PDFs, ATT&CK Excel
│   └── Github/                          # Open-source tools
│
├── engagements/                         # Active engagement projects
├── reports/                             # Generated reports
│
├── install.sh                           # Installation script
├── ARCHITECTURE.md                      # System architecture
├── BUILD_LOG.md                         # Build history
├── PROGRESS.md                          # Project progress
└── README.md                            # This file
```

---

## Statistics

### Project Metrics

| Metric | Count |
|--------|-------|
| **AI Agents** | 20 |
| **Skills/Capabilities** | 30 |
| **Kill-Chain Workflows** | 12 |
| **MITRE Technique Directories** | 992 |
| **Total Markdown Files** | 4,403 |
| **Total Shell Scripts** | 1,312 |
| **Total Python Scripts** | 2,836 |
| **Total Files** | 15,792 |

### MITRE ATT&CK Coverage

| Tactic | Techniques |
|--------|------------|
| Reconnaissance | 93 |
| Resource Development | 47 |
| Initial Access | 60 |
| Execution | 39 |
| Persistence | 52 |
| Privilege Escalation | 18 |
| Defense Evasion | 120+ |
| Credential Access | 45+ |
| Discovery | 40+ |
| Lateral Movement | 25+ |
| Collection | 35+ |
| Command and Control | 30+ |
| Exfiltration | 20+ |
| Impact | 18+ |

### Tool Integration

| Tool | Purpose |
|------|---------|
| nmap | Network scanning |
| masscan | Fast port scanning |
| sqlmap | SQL injection |
| hydra | Brute force |
| gobuster | Directory enumeration |
| nikto | Web vulnerability scanning |
| impacket-psexec | Windows lateral movement |
| evil-winrm | WinRM shell |
| proxychains | Proxy chains |
| curl/wget | HTTP requests |
| python3 | Scripting |
| git | Version control |

---

## Contributing

**We welcome contributions!** Black Aegis is an open-source project and we believe in the power of community collaboration.

### How to Contribute

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Ways to Contribute

| Type | Description |
|------|-------------|
| **Bug Reports** | Found a bug? [Open an issue](https://github.com/BlackAegis/BlackAegis/issues) |
| **Feature Requests** | Have an idea? [Request a feature](https://github.com/BlackAegis/BlackAegis/issues) |
| **New Skills** | Create new capability modules |
| **New Techniques** | Add MITRE ATT&CK technique implementations |
| **Documentation** | Improve guides, tutorials, or examples |
| **Testing** | Test the framework and report issues |
| **Translations** | Help translate documentation |

### Development Guidelines

- Follow the existing code style
- Add documentation for new features
- Test changes before submitting
- Update PROGRESS.md with your changes
- Use meaningful commit messages

### Issue Templates

When opening an issue, please use one of these templates:

- **Bug Report**: Describe the issue, steps to reproduce, expected vs actual behavior
- **Feature Request**: Describe the feature, use case, and implementation ideas
- **Skill Request**: Propose a new capability module
- **Technique Request**: Request a new MITRE ATT&CK technique implementation

### Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help maintain a welcoming community
- No tolerance for harassment or discrimination

---

## Roadmap

### Completed

- [x] 20 AI Agent definitions
- [x] 30 skill modules
- [x] 12 kill-chain workflows
- [x] 992 MITRE ATT&CK technique directories
- [x] Orchestration engine
- [x] Report generator
- [x] Installation script
- [x] Tool verification

### In Progress

- [ ] Web-based dashboard UI
- [ ] REST API for automation
- [ ] Docker containerization
- [ ] CI/CD pipeline integration

### Planned

- [ ] AI-powered vulnerability analysis
- [ ] Automated exploit generation
- [ ] Real-time collaboration features
- [ ] Integration with SIEM platforms
- [ ] Mobile application
- [ ] Additional language support
- [ ] Cloud deployment options
- [ ] Enterprise multi-tenant support

---

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2026 Black Aegis

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## Disclaimer

> **IMPORTANT: READ THIS BEFORE USING BLACK AEGIS**

### Legal Notice

Black Aegis is provided for **authorized security testing and educational purposes only**. This framework is designed to help security professionals identify and remediate vulnerabilities in systems they own or have explicit written permission to test.

### No Warranty

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

### User Responsibility

**Users are solely responsible for:**
- Ensuring they have proper authorization before testing
- Complying with all applicable local, state, national, and international laws
- Understanding and accepting the legal implications of their actions
- Any damages or consequences resulting from misuse of this framework

### No Liability

**Black Aegis contributors and maintainers are NOT responsible for:**
- Any damage caused by this software
- Any illegal activity conducted using this framework
- Any misuse of the techniques or tools included
- Any consequences of unauthorized access to systems

### Authorization Required

**Before using Black Aegis:**
1. Obtain **written authorization** from the system owner
2. Define clear **scope and rules of engagement**
3. Ensure compliance with **all applicable laws**
4. Have **incident response procedures** in place
5. **Never test production systems** without explicit permission

### Educational Use

This framework is also intended for **educational purposes** to help:
- Security professionals learn offensive techniques
- Students understand attack methodologies
- Organizations train their defensive teams
- Researchers study adversary behavior

---

## Acknowledgments

### Frameworks & Standards

- [MITRE ATT&CK](https://attack.mitre.org/) - Adversary tactics and techniques
- [NIST SP 800-115](https://csrc.nist.gov/publications/detail/sp/800-115/final) - Penetration testing guide
- [OWASP](https://owasp.org/) - Web application security

### Open Source Tools

- [Impacket](https://github.com/fortra/impacket) - Network protocols
- [Nmap](https://nmap.org/) - Network discovery
- [Metasploit](https://www.metasploit.com/) - Exploitation framework
- [BloodHound](https://github.com/BloodHoundAD/BloodHound) - AD attack paths

### Community

- Thanks to all contributors who help improve Black Aegis
- Special thanks to the security research community
- Gratitude to open-source tool maintainers

---

<div align="center">

**Built with purpose. Free for those who need it most.**

[Black Aegis](https://github.com/BlackAegis/BlackAegis) © 2026

*"We do not test defenses. We become the threat."*

</div>
