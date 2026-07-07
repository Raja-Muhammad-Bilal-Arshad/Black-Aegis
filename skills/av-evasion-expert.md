---
name: av-evasion-expert
description: AMSI bypass, syscall hooking, unhooking.
---

# AV/EDR Evasion Protocol

## 1. Principles
- **Do not touch disk**: Run in memory whenever possible.
- **Unhook user-land**: EDRs hook ntdll.dll to inspect API calls. Restore the original bytes.
- **Direct Syscalls**: Bypass the hooked APIs entirely using assembly syscalls (Hell's Gate).

## 2. Techniques
- **AMSI Bypass**: Patch the `AmsiScanBuffer` function in memory to always return `AMSI_RESULT_CLEAN`.
- **PPID Spoofing**: Launch processes with a trusted parent (e.g., explorer.exe) to look legit.
- **BlockDLLs**: Prevent non-Microsoft signed DLLs from loading into your process.

## 3. Checklist
- [ ] AMSI patched?
- [ ] ETW (Event Tracing for Windows) patched?
- [ ] Syscalls used for sensitive ops (VirtualAlloc, CreateThread)?
- [ ] Metadata of the binary matches a legit system binary?
