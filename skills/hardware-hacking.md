---
name: hardware-hacking
description: JTAG, UART, firmware extraction, IoT device exploitation.
---

# Hardware Hacking Techniques

## 1. Reconnaissance

### Identify Interfaces
```bash
# Look for:
- JTAG headers (10-20 pin, often labeled)
- UART headers (4 pins: VCC, GND, TX, RX)
- SPI flash chips (8 pins)
- I2C EEPROM (8 pins)
- USB ports
- Ethernet ports
- SD card slots

# Tools:
- Multimeter (identify power/ground)
- Logic analyzer (decode protocols)
- Bus Pirate (multi-protocol)
- JTAGulator (identify JTAG pins)
```

## 2. UART Access

```bash
# Identify TX/RX pins (look for activity with oscilloscope)
# Connect: TX→RX, RX→TX, GND→GND, VCC→VCC (optional)

# Use screen/picocom
screen /dev/ttyUSB0 115200
# or
picocom -b 115200 /dev/ttyUSB0

# Common baud rates: 9600, 19200, 38400, 57600, 115200
```

## 3. JTAG Access

```bash
# Connect to JTAG interface
# Tools: J-Link, Bus Pirate, JTAGulator

# OpenOCD
openocd -f interface/jlink.cfg -f target/stm32f1x.cfg
# Connect
telnet localhost 4444
# Dump firmware
dump_image firmware.bin 0x08000000 0x100000
```

## 4. Firmware Extraction

### SPI Flash
```bash
# Use CH341A programmer
flashrom -p ch341a_spi -r firmware.bin

# Or with Bus Pirate
flashrom -p buspirate_spi -r firmware.bin
```

### NAND Flash
```bash
# Use FlashROM or raw programmer
# May need to handle ECC and bad blocks
```

### Via UART/JTAG
```bash
# Read filesystem directly
cat /proc/mtd  # Identify partitions
dd if=/dev/mtd0 of=/tmp/firmware.bin
```

## 5. Firmware Analysis

```bash
# Extract filesystem
binwalk -e firmware.bin

# Analyze
file squashfs-root/*
strings squashfs-root/usr/bin/app

# Find secrets
grep -r "password" squashfs-root/
grep -r "key" squashfs-root/
find squashfs-root/ -name "*.pem" -o -name "*.key"

# Check for hardcoded credentials
strings squashfs-root/usr/bin/* | grep -i "pass\|admin\|root"
```

## 6. Common IoT Vulnerabilities

| Vulnerability | Description |
|---------------|-------------|
| Default creds | admin:admin, root:root |
| Hardcoded secrets | API keys in firmware |
| Debug interfaces | JTAG/UART enabled |
| No secure boot | Firmware can be modified |
| Clear-text protocols | Telnet, HTTP, FTP |
| Outdated libraries | Known CVEs |

## 7. Tools

| Tool | Purpose |
|------|---------|
| Bus Pirate | Multi-protocol interface |
| CH341A | SPI/I2C programmer |
| JTAGulator | JTAG pin identification |
| OpenOCD | JTAG/SWD debugging |
| Binwalk | Firmware analysis |
| Ghidra | Binary reverse engineering |
| Proxmark3 | RFID/NFC research |
