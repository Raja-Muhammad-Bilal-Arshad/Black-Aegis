# Tactical Guide: T1567.002 - Exfiltration to Cloud Storage (T1567.002)

## Overview
**Technique**: T1567.002
**Name**: Exfiltration to Cloud Storage (T1567.002)
**Tactic**: 13_Exfiltration
**Platform**: Cross-platform (varies by sub-technique)

## Description
This technique is part of the MITRE ATT&CK framework under the 13_Exfiltration tactic.
Adversaries use this technique during their operations to achieve specific objectives.

## Execution Steps
1. **Preparation**: Ensure proper authorization and scope
2. **Reconnaissance**: Identify target environment specifics
3. **Execution**: Use appropriate tools and methods
4. **Validation**: Verify successful execution
5. **Cleanup**: Remove artifacts and restore system state

## Required Tools
- See `recon.sh` / `execute.sh` / technique-specific script in this directory
- Operating system utilities
- Third-party security tools (see Resources/)

## OPSEC Considerations
- Minimize network noise
- Use encrypted channels
- Clean up artifacts after testing
- Document all actions for reporting

## Detection Points
- See `DETECTION.md` for detection logic and Sigma rules
- Focus on behavioral indicators, not just IOCs

## References
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1567/
- Black Aegis Framework: See `frameworks/MITRE_ATTACK.md`

## Authorization
**REQUIRED**: Written authorization before execution.
This technique is for authorized security testing only.
