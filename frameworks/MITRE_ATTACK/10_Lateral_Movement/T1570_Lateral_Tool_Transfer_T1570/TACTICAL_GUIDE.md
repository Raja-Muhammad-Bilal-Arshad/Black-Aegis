# Tactical Guide: T1570 - Lateral Tool Transfer (T1570)

## Overview
**Technique**: T1570
**Name**: Lateral Tool Transfer (T1570)
**Tactic**: 10_Lateral_Movement
**Platform**: Cross-platform (varies by sub-technique)

## Description
This technique is part of the MITRE ATT&CK framework under the 10_Lateral_Movement tactic.
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
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1570/
- Black Aegis Framework: See `frameworks/MITRE_ATTACK.md`

## Authorization
**REQUIRED**: Written authorization before execution.
This technique is for authorized security testing only.
