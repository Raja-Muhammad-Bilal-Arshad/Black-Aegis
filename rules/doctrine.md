# Black Aegis Doctrine

> "We operate in the shadows to illuminate the flaws."

## 1. Stealth Levels (DEFCON)

### 🔇 Level 1: SILENT (Ghost Mode)
- **Authorization**: Default for all Initial Access and Recon.
- **Network**: Zero packets sent to target directly (Passive Recon only).
- **Endpoint**: No binary drops. Memory injection only.
- **Traffic**: Beacon interval > 1 hour. High jitter.

### 🤫 Level 2: COVERT (Ninja Mode)
- **Authorization**: Standard operation for Lateral Movement.
- **Network**: Local traffic only (SMB/WinRM). No port scanning < 1000 pps.
- **Endpoint**: Dropping signed binaries allowed. Cleaning logs required.
- **Traffic**: Beacon interval 5-15 mins. Encrypted HTTPS/DNS.

### 🔊 Level 3: LOUD (Smash & Grab)
- **Authorization**: **REQUIRES `supreme-architect` OVERRIDE**.
- **Network**: Masscan allowed. Vulnerability scanners (Nessus) allowed.
- **Endpoint**: Ransomware simulation. Formatting drives.
- **Traffic**: Constant connection (Reverse Shell).

## 2. Data Ethics & Safety

### 🛡️ The "Do Not Crossing" Line
- **PII (Personal Identifiable Information)**: Never exfiltrate real credit card numbers or SSNs. Only proofs (first 4 digits/last 4 digits).
- **Production Uptime**: Do not exploit DOS vulnerabilities in Production. Verification only.
- **Healthcare/Critical infra**: If a target is identified as a Hospital or Power Grid, **ABORT IMMEDIATELY** and notify Command.

### 🧹 Cleanup Protocol
- Every file dropped must be logged in `artifacts.log`.
- Every user created must be deleted.
- Every firewall rule changed must be reverted.
