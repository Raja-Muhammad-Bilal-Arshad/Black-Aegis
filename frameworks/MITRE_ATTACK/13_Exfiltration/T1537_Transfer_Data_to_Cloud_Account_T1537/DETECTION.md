# Detection Logic: T1537 - Transfer Data to Cloud Account (T1537)

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
title: Detect Transfer Data to Cloud Account (T1537) (T1537)
id: 4a70b1cc-a2d1aa7f
status: experimental
description: Detects Transfer Data to Cloud Account (T1537) technique
references:
    - https://attack.mitre.org/techniques/T1537/
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
    - attack.t1537
```

## SIEM Queries

### Splunk
```spl
index=windows sourcetype=WinEventLog:EventCode=4688
| search CommandLine="*T1537*"
| stats count by ComputerName, CommandLine
```

### Elastic
```json
{"query": {"match": {"process.command_line": "T1537"}}}
```

### Sentinel
```kusto
SecurityEvent
| where EventID == 4688
| where CommandLine contains "T1537"
```

## Detection Recommendations
1. Enable process creation logging (Event ID 4688)
2. Enable command-line auditing
3. Deploy Sysmon with appropriate config
4. Enable PowerShell script block logging
5. Monitor for suspicious process relationships
