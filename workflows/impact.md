---
description: Execute objective (Ransom/Wipe)
---

# Impact Workflow

## 1. Ransomware (Simulation)
1.  **Encryption**: Iterate through share drives and encrypt files (POC: Rename to `.lock`).
2.  **Note**: Drop `README.txt` with ransom instructions.

## 2. Data Destruction
1.  **Wipe**: `format c: /q` (Do NOT execute in prod without override).
2.  **Corrupt**: Overwrite MBR (Master Boot Record).

## 3. Denial of Service
1.  **Resource Exhaustion**: Fill disk space.
2.  **Fork Bomb**: `:(){ :|:& };:` (Linux).
