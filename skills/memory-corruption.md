---
name: memory-corruption
description: Buffer overflows, use-after-free, format strings, heap exploitation.
---

# Memory Corruption Exploitation

## 1. Vulnerability Classes

| Class | Description | Example |
|-------|-------------|---------|
| Stack Buffer Overflow | Write past buffer on stack, overwrite return addr | `strcpy(buf, input)` with oversized input |
| Heap Overflow | Overflow into heap metadata or adjacent chunks | `memcpy` with size > allocated |
| Use-After-Free (UAF) | Access freed memory | Double-free, dangling pointers |
| Format String | User-controlled format specifier | `printf(user_input)` |
| Integer Overflow | Arithmetic wraps around | `size = width * height` overflows |
| Type Confusion | Wrong type interpretation | C++ vtable abuse |

## 2. Exploitation Workflow

```
1. Identify vulnerable function (fuzzing/static analysis)
2. Determine crash type (EIP/RIP control, write-what-where)
3. Calculate offsets (pattern_create/pattern_offset or pwntools)
4. Bypass protections:
   - NX/DEP → ROP chains
   - ASLR → Info leak / brute force
   - Stack Canary → Leak canary / format string
   - PIE → Relative overwrite / info leak
5. Build payload (shellcode or ROP chain)
6. Achieve code execution
```

## 3. Tools

| Tool | Purpose |
|------|---------|
| `pwntools` | Python exploit development framework |
| `ROPgadget` / `ropper` | Find ROP gadgets |
| `GDB` + `pwndbg`/`GEF` | Debugging exploits |
| `radare2` / `Ghidra` | Reverse engineering |
| `American Fuzzy Lop (afl++)` | Fuzzing |
| `checksec` | Check binary protections |

## 4. Common Patterns

### Stack Overflow (x86-64 Linux)
```python
from pwn import *
p = process('./vuln')
padding = b'A' * offset
pop_rdi = 0x4011cb      # pop rdi; ret
bin_sh = 0x402004       # "/bin/sh"
system = 0x401030       # system@plt
payload = padding + p64(pop_rdi) + p64(bin_sh) + p64(system)
p.sendline(payload)
p.interactive()
```

### Format String Write
```python
# Write to GOT entry using %n
payload = p32(got_addr) + b'%123c%7$n'  # Write 123 to got_addr
```

### Heap UAF (tcache poisoning)
```python
# 1. Allocate and free chunks
# 2. Overwrite fd pointer in freed chunk
# 3. Allocate to get arbitrary address
# 4. Write __malloc_hook or return address
```

## 5. Protections & Bypasses

| Protection | Bypass |
|------------|--------|
| NX/DEP | ROP, ret2libc, mprotect |
| ASLR | Info leak, partial overwrite, brute force |
| Stack Canary | Leak via format string, fork brute force |
| PIE | Relative overwrites, info leak |
| RELRO | GOT overwrite (partial RELRO only) |

## 6. Practice Targets

- picoCTF, HackTheBox, TryHackMe (binary exploitation)
- Protostar, Nightmare, ROP Emporium
