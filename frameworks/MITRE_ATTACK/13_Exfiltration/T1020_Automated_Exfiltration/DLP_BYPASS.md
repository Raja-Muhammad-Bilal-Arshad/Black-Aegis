# DLP Bypass Guide: Automated Exfiltration (T1020)

## Speed vs Stealth
Automated exfiltration is dangerous for the attacker because it creates a pattern. If I save a file and it's uploaded 1 second later, Correlation Engines can catch this.

## Evasion Techniques
1.  **Batching**: Wait until 50 files are collected, tar them, then upload once.
2.  **Thresholds**: Only upload if the file size is less than 1MB (to stay under alerts).
