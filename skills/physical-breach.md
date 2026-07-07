---
name: physical-breach
description: Lock picking, badge cloning, CCTV bypass, physical entry techniques.
---

# Physical Breach Techniques

## 1. Lock Picking

### Pin Tumbler (Standard)
```bash
# Tools: Tension wrench + Pick
# 1. Apply tension with wrench
# 2. Push pins up with pick until all set
# 3. Turn wrench to open

# Bypass tools:
- Snap gun (vibration picking)
- Bump key (force all pins)
- Lishi picks (decode + pick)
```

### Common Lock Types
| Type | Vulnerability | Tool |
|------|--------------|------|
| Pin Tumbler | Picking, bumping | Tension + pick |
| Wafer | Low security picks | Wafer pick |
| Disc Detainer | Decoding | Disc detainer pick |
| Smart Lock | Bypass via default creds | Default pin list |
| Padlock | Shimming, cutting | Shims, bolt cutters |

### Bypass Methods
```bash
# Credit card bypass (latch locks)
# Slide card between door and frame

# Bypass knife (push back latch)

# Key impressioning (create key from lock)
```

## 2. Badge/Access Control

### RFID Cloning (125kHz)
```bash
# Read badge
proxmark3> lf hid read
# Clone to blank card
proxmark3> lf hid clone -r <raw_data>
```

### RFID Cloning (13.56MHz)
```bash
# Read (requires more powerful reader)
# Some cards are encrypted and cannot be cloned
proxmark3> hf mf classic dump
```

### Keypad Bypass
```bash
# Default codes: 1234, 0000, 1111, 9999
# Thermal imaging (residual heat from pressed keys)
# Brute force (if no lockout)
# Shoulder surfing
```

## 3. CCTV Bypass

```bash
# Find cameras via IR light at night
# Camera locations: corners, hallways, entrances

# Common bypass methods:
# - Cover camera with spray paint/latex
# - Redirect with mirrors
# - Exploit IP camera default creds
# - Jam WiFi cameras (2.4GHz)
```

## 4. Tailgating/Piggybacking

```bash
# Follow authorized person through:
# - Mantrap/airlock
# - Badge-protected door
# - Secure elevator

# Pretext: Carry boxes, look busy, hold phone to ear
```

## 5. Dumpster Diving

```bash
# Find: Old documents, sticky notes, old hardware
# Legal in many jurisdictions (trash = no expectation of privacy)
# Check: Shredded documents, old drives, printed configs
```

## 6. Detection

- Access control logs (time, location, user)
- CCTV analytics (unusual movement patterns)
- Tailgating detection sensors
- Regular physical security audits

## 7. Mitigations

- Anti-pick locks (security pins, restricted keyways)
- Mantraps at high-security areas
- CCTV monitoring with analytics
- Badge photo verification
- Shredding policy for documents
- Clean desk policy
