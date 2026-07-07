# Detection Logic: T1011 - Exfiltration Over Other Network Medium (T1011)

## Tactic: 13_Exfiltration

## Noise Level
- **Initial**: Medium (varies by technique)
- **With Logging**: High

## Log Sources
- **Windows**: Security Event Log, Sysmon, PowerShell Logging
- **Linux**: auditd, syslog, /var/log/auth.log
- **Network**: Firewall logs, DNS logs, Proxy logs

## Sigma Rule Template
```yaml
title: Detect Exfiltration Over Other Network Medium (T1011) (T1011)
id: cb63044e-e34ae371
status: experimental
description: Detects Exfiltration Over Other Network Medium (T1011) technique
references:
    - https://attack.mitre.org/techniques/T1011/
author: Black Aegis
date: 2026/07/07
logsource:
    category: process_creation
    product: windows
detection:
    selection:
        # Add specific detection criteria here
        # Example:
        # Image|endswith: '\tool.exe'
        # CommandLine|contains: 'suspicious_string'
    condition: selection
falsepositives:
    - Legitimate administrative activity
level: medium
tags:
    - attack.13_exfiltration
    - attack.t1011
```

## SIEM Queries

### Splunk
```spl
index=windows sourcetype=WinEventLog:EventCode=4688
| search CommandLine="*T1011*"
| stats count by ComputerName, CommandLine
```

### Elastic
```json
{"query": {"match": {"process.command_line": "T1011"}}}
```

### Sentinel
```kusto
SecurityEvent
| where EventID == 4688
| where CommandLine contains "T1011"
```

## Detection Recommendations
1. Enable process creation logging (Event ID 4688)
2. Enable command-line auditing
3. Deploy Sysmon with appropriate config
4. Enable PowerShell script block logging
5. Monitor for suspicious process relationships
