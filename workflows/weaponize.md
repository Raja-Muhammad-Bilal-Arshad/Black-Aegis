---
description: Build payloads & exploits
---

# Weaponization Workflow

## 1. Exploit Selection
1.  **Search**: `searchsploit <service version>` or analyze Patch Diffs.
2.  **Review**: NEVER run a script without reading it. Check for "rm -rf" or beaconing.

## 2. Payload Development
1.  **Form**: Pick format (EXE, DLL, HTA, VBS, Macro).
2.  **Generate**:
    - Don't use `msfvenom` default templates.
    - Use `scarecrow` or `nim-loader` to wrap shellcode.
3.  **Test**: Run in local VM with Defender enabled. Fails? Refactor.

## 3. Staging
1.  **Host**: Setup HTTPS server or C2 redirector.
2.  **Delivery**: Zip it with a password or embed in ISO.
