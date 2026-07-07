---
name: siem-blinding
description: Log evasion, false flags, timestamp manipulation, alert suppression.
---

# SIEM Blinding Techniques

## 1. Log Clearing / Suppression

```bash
# Windows Event Log Clearing (LOUD - triggers Event 1102)
wevtutil cl Security
wevtutil cl System
wevtutil cl Application

# Selective log deletion
wevtutil qe Security /c:10 /f:text /rd:true  # Read recent events
# Delete specific events (requires tools like Danderspritz)

# Linux
echo > /var/log/auth.log
echo > /var/log/syslog
history -c  # Clear bash history
```

## 2. Timestamp Manipulation (Timestomping)

```bash
# Change file timestamps to blend in
touch -r /bin/ls /tmp/backdoor.exe  # Copy timestamps from legitimate file
timestomp /tmp/backdoor.exe /created:"01/01/2020 00:00:00"

# Windows
(Get-Item file.exe).LastWriteTime = (Get-Date "01/01/2020")
(Get-Item file.exe).CreationTime = (Get-Date "01/01/2020")
```

## 3. False Flags

```bash
# Plant false attribution
# - Use Russian/Chinese keyboard layouts
# - Insert strings in other languages
# - Use known APT tools (but modified)
# - Set timezone to other regions

# Example: Add Russian strings to binary
echo "Привет мир" >> /tmp/backdoor.exe
```

## 4. Traffic Blending

```bash
# Use legitimate protocols
# - HTTPS to blend with normal web traffic
# - DNS for covert channels
# - Use common User-Agents (Chrome, Firefox)
# - Match normal beacon intervals (not too regular)

# Beacon jitter
sleep $(( RANDOM % 3600 + 300 ))  # 5-60 minute random interval
```

## 5. Process Masquerading

```bash
# Rename processes to match legitimate ones
cp payload.exe svchost.exe
cp payload.exe csrss.exe
cp payload.exe lsass.exe

# Run from legitimate paths
C:\Windows\System32\svchost.exe -k netsvcs
```

## 6. Alert Suppression

```bash
# Generate noise to hide real activity
# - Create many benign alerts
# - Overwhelm SIEM with log noise
# - Use common vulnerability scanners (trigger known alerts)
```

## 7. Detection Countermeasures

| Technique | Detection Method |
|-----------|-----------------|
| Log clearing | Event 1102, log gaps |
| Timestomping | USN Journal, $STANDARD_INFORMATION |
| False flags | Behavioral analysis, not just IOCs |
| Process masquerading | Command line arguments, parent process |

## 8. Mitigations

- Centralized logging (attacker can't reach all logs)
- WORM storage for logs
- Real-time alerting
- Behavioral analytics (UEBA)
- File integrity monitoring
