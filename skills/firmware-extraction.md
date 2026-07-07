---
name: firmware-extraction
description: Firmware dumping, reverse engineering, embedded device analysis.
---

# Firmware Extraction & Analysis

## 1. Extraction Methods

### Software Extraction (Remote)
```bash
# Via web interface (firmware upgrade page)
wget http://target/firmware.bin

# Via TFTP
tftp target -c get firmware.bin

# Via SSH/Telnet
ssh root@target "cat /dev/mtd0" > firmware.bin

# Via SNMP
snmpwalk -v2c -c public target 1.3.6.1.4.1
```

### Hardware Extraction (Physical)
```bash
# SPI Flash (CH341A)
flashrom -p ch341a_spi -r firmware.bin

# JTAG (OpenOCD)
dump_image firmware.bin 0x08000000 0x100000

# UART (direct access)
cat /dev/ttyUSB0 > firmware.bin

# NAND (chip-off)
# Desolder chip, use programmer
```

## 2. Filesystem Extraction

```bash
# Identify filesystem type
file firmware.bin
binwalk firmware.bin

# Extract SquashFS
binwalk -e firmware.bin
# or unsquashfs firmware.bin

# Extract JFFS2
binwalk -e firmware.bin
# or jefferson -f firmware.bin -d output/

# Extract CramFS
binwalk -e firmware.bin
# or cramfsck -x output/ firmware.bin

# Extract UBIFS
ubireader_extract_images firmware.bin
```

## 3. Analysis Techniques

### Filesystem Analysis
```bash
# Find interesting files
find squashfs-root/ -type f \( -name "*.conf" -o -name "*.key" -o -name "*.pem" -o -name "*.sh" \)

# Search for secrets
grep -rn "password\|passwd\|secret\|key\|token" squashfs-root/
grep -rn "api_key\|apikey\|api-key" squashfs-root/

# Find network configs
find squashfs-root/ -name "*.conf" -exec grep -l "ip\|address\|gateway" {} \;
```

### Binary Analysis
```bash
# Static analysis
strings squashfs-root/usr/bin/app | head -50
objdump -d squashfs-root/usr/bin/app | head -100
readelf -a squashfs-root/usr/bin/app

# Dynamic analysis (with QEMU)
qemu-arm -L squashfs-root/ squashfs-root/usr/bin/app
```

## 4. Common Firmware Formats

| Format | Description | Tool |
|--------|-------------|------|
| SquashFS | Read-only compressed | unsquashfs |
| JFFS2 | Journaling Flash FS | jefferson |
| CramFS | Compressed ROM FS | cramfsck |
| UBIFS | Unsorted Block FS | ubireader |
| YAFFS2 | Yet Another Flash FS | unyaffs |
| ext2/3/4 | Standard Linux FS | mount, debugfs |

## 5. Vulnerability Patterns

| Pattern | Description |
|---------|-------------|
| Hardcoded credentials | Passwords in config files |
| Debug backdoors | Hidden SSH/telnet access |
| Command injection | Unsanitized input in shell calls |
| Buffer overflows | Unsafe C functions |
| Insecure updates | No signature verification |
| Clear-text protocols | Telnet, HTTP, FTP |

## 6. Tools

| Tool | Purpose |
|------|---------|
| Binwalk | Firmware analysis/extraction |
| Ghidra | Binary reverse engineering |
| radare2 | Binary analysis |
| flashrom | SPI flash reading |
| OpenOCD | JTAG/SWD debugging |
| QEMU | Emulation of embedded systems |
