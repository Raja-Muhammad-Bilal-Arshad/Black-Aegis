---
name: rf-signal-attack
description: SDR, RFID cloning, Bluetooth attacks, cellular interception.
---

# RF Signal Attack Techniques

## 1. Software Defined Radio (SDR)

### Setup
```bash
# RTL-SDR (receive only)
rtl_sdr -f 100000000 -s 2000000 output.bin

# HackRF (transmit/receive)
hackrf_transfer -r output.bin -f 100000000 -s 2000000

# USRP (professional SDR)
# GNU Radio for complex processing
```

### Common Frequencies
| Frequency | Use |
|-----------|-----|
| 315 MHz | Garage doors, car key fobs |
| 433 MHz | ISM band, remotes |
| 868/915 MHz | LoRa, IoT |
| 2.4 GHz | WiFi, Bluetooth, Zigbee |
| 5.8 GHz | WiFi, video |
| 125 kHz | RFID (LF) |
| 13.56 MHz | RFID (HF), NFC |

## 2. RFID Attacks

### 125 kHz (LF RFID)
```bash
# Read
proxmark3> lf hid read
# Clone
proxmark3> lf hid clone -r <raw_data>
# Write
proxmark3> lf hid write -r <raw_data>
```

### 13.56 MHz (HF RFID/NFC)
```bash
# Read
proxmark3> hf mf classic dump
# Some cards are encrypted (MIFARE DESFire, etc.)
# Emulation
proxmark3> hf mf emulate
```

## 3. Bluetooth Attacks

```bash
# Scanning
hcitool scan
bluesnarfer -r 0,0 -s 6

# BLE (Bluetooth Low Energy)
gatttool -b <MAC> --characteristic-read
# Sniffing
ubertooth-btle
```

## 4. Zigbee/Z-Wave Attacks

```bash
# Zigbee sniffing (KillerBee)
zbwireshark  # Capture Zigbee traffic
zbdump -f 15 -w capture.pcap  # Capture on channel 15

# Z-Wave
zwave-ssniffer
```

## 5. Tools

| Tool | Purpose |
|------|---------|
| HackRF One | SDR transceiver |
| Proxmark3 | RFID research |
| Ubertooth | Bluetooth research |
| Yard Stick One | Sub-1 GHz |
| RTL-SDR | Budget receive-only SDR |
| BladeRF | Professional SDR |

## 6. Mitigations

- Use encrypted RFID systems
- Disable unused wireless interfaces
- Monitor for rogue devices
- Physical security for access control readers
