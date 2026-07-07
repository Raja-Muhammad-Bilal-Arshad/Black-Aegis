---
name: osint-deep-dive
description: Passive recon, dark web correlation.
---

# OSINT Deep Dive Protocol

## 1. Principles
- **No Active Scans**: Do not touch the target infrastructure.
- **Everything is Indexed**: Google Dorks reveal PDF configs, SQL dumps.
- **Humans Leak**: LinkedIn + Instagram = Password hints.

## 2. Techniques
- **Google Dorking**: `site:target.com ext:pdf "confidential"`.
- **GitHub Recon**: Searching for "TargetAPI" or leaked keys in personal repos of employees.
- **Breach Data**: Searching DeHashed/HaveIBeenPwned for credentials.

## 3. Checklist
- [ ] ASN mapped (Amass/Hurricane Electric)?
- [ ] Subdomains enumerated (Subfinder)?
- [ ] Employee emails harvested (Hunter.io)?
- [ ] Leaked passwords found?
