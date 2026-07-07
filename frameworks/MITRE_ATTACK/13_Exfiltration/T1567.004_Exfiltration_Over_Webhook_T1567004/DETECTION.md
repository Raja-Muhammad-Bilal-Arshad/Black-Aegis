# Detection Logic: T1567.004 - Exfiltration Over Webhook (T1567.004)

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
title: Detect Exfiltration Over Webhook (T1567.004) (T1567.004)
id: 358ddfef-28553baa
status: experimental
description: Detects Exfiltration Over Webhook (T1567.004) technique
references:
    - https://attack.mitre.org/techniques/T1567/
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
    - attack.t1567004
```

## SIEM Queries

### Splunk
```spl
index=windows sourcetype=WinEventLog:EventCode=4688
| search CommandLine="*T1567.004*"
| stats count by ComputerName, CommandLine
```

### Elastic
```json
{"query": {"match": {"process.command_line": "T1567.004"}}}
```

### Sentinel
```kusto
SecurityEvent
| where EventID == 4688
| where CommandLine contains "T1567.004"
```

## Detection Recommendations
1. Enable process creation logging (Event ID 4688)
2. Enable command-line auditing
3. Deploy Sysmon with appropriate config
4. Enable PowerShell script block logging
5. Monitor for suspicious process relationships
