---
name: mitre-mapping
description: Mapping actions to ATT&CK Matrix.
---

# MITRE ATT&CK Mapping Protocol

## 1. Principles
- **Standardized Language**: Don't say "we hacked it". Say "Executed T1059.001 (PowerShell)".
- **Attribution**: Helps the Blue Team identify the threat actor we are emulating.
- **Coverage**: ensure the campaign covers varied tactics (Initial Access -> Impact).

## 2. Techniques
- **T1566**: Phishing.
- **T1110**: Brute Force.
- **T1003**: OS Credential Dumping (LSASS).
- **T1053**: Scheduled Task/Job.

## 3. Procedure
- Log every command.
- Look up the Technique ID on attack.mitre.org.
- Tag the finding in the report with the ID.
