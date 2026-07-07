---
name: zero-day-strategy
description: Vulnerability research, 0-day discovery, responsible disclosure decisions.
---

# Zero-Day Research Strategy

## 1. Vulnerability Research Workflow

```
1. Target Selection
   ├── Open-source software (widely used)
   ├── Proprietary software (high value)
   └── Protocol analysis (fundamental)

2. Research Phase
   ├── Code review (static analysis)
   ├── Fuzzing (dynamic analysis)
   ├── Reverse engineering
   └── Patch diffing (regression bugs)

3. Vulnerability Classification
   ├── Type: Memory corruption, logic, auth bypass
   ├── Severity: Critical, High, Medium, Low
   ├── Exploitability: Easy, Moderate, Difficult
   └── Impact: RCE, Priv Esc, Info Leak

4. Exploitation
   ├── Proof of Concept development
   ├── Exploit reliability testing
   ├── Defense bypass (ASLR, DEP, CFI)
   └── Weaponization (if authorized)

5. Disclosure Decision
   ├── Full disclosure (immediate)
   ├── Coordinated disclosure (90-day)
   ├── Private disclosure (vendor only)
   └── Keep for offensive use (authorized only)
```

## 2. Research Techniques

### Static Analysis
```bash
# Code review with semgrep
semgrep --config=auto /path/to/code

# Binary analysis with Ghidra
ghidra /path/to/binary

# Find dangerous functions
grep -rn "strcpy\|sprintf\|gets\|scanf" /path/to/code
```

### Fuzzing
```bash
# AFL++ fuzzing
afl-fuzz -i seeds/ -o output/ ./target @@

# libFuzzer
./target corpus/ -max_len=1024

# WinAFL (Windows)
winafl.exe -fuzz_iterations 10000 -target_module target.dll -target_offset 0x1234 -fuzzer_args -timeout=10 target.exe
```

### Patch Diffing
```bash
# Compare patched vs unpatched binaries
# Tools: Diaphora (IDA), diffsclosure, BinDiff
# Find what was fixed → reverse engineer the bug
```

## 3. Vulnerability Classes

| Class | Description | Common In |
|-------|-------------|-----------|
| Heap Overflow | Write past heap buffer | C/C++ apps |
| Use-After-Free | Access freed memory | Browsers, apps |
| Type Confusion | Wrong type interpretation | Script engines |
| Auth Bypass | Skip authentication | Web apps, APIs |
| Logic Flaw | Business logic error | Any application |
| Deserialization | Unsafe object conversion | Java, Python, PHP |
| SQL Injection | Database query manipulation | Web apps |
| Command Injection | OS command execution | Any app with shell calls |

## 4. Disclosure Decision Matrix

| Factor | Offensive Use | Coordinated | Full |
|--------|--------------|-------------|------|
| Vendor responsive | No | Yes | No |
| Under active exploitation | Yes | Yes | Yes |
| Critical infrastructure | Yes | Yes | No |
| No vendor available | Yes | N/A | Yes |
| Authorized engagement | Yes | Optional | No |

## 5. Tools

| Tool | Purpose |
|------|---------|
| Ghidra / IDA Pro | Reverse engineering |
| AFL++ / libFuzzer | Fuzzing |
| Semgrep | Static analysis |
| Diaphora | Patch diffing |
| pwndbg / GEF | Exploit debugging |
| pwntools | Exploit development |
