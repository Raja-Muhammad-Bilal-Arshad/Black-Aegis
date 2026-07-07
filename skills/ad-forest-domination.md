---
name: ad-forest-domination
description: Golden Ticket, DCSync, BloodHound paths.
---

# Active Directory Domination Protocol

## 1. Principles
- **Think in Graphs**: AD is a graph of relationships (MemberOf, CanRDPHere, HasSession). Use BloodHound.
- **Least Privilege is a Myth**: You only need one path to DA.
- **Live off the Land**: Use built-in tools (PowerShell, WMI, NET) to avoid dropping binaries.

## 2. Techniques
- **BloodHound**: Gather data with SharpHound (stealth flags). Analyze path to Domain Admin.
- **DCSync**: Simulate a Domain Controller to request password hashes (requires DC replication rights).
- **Golden Ticket**: Forge a TGT using the `krbtgt` hash. Persistence for 10 years.

## 3. Checklist
- [ ] BloodHound data collected?
- [ ] Shortest path to DA identified?
- [ ] Kerberoasting performed?
- [ ] AS-REP Roasting performed?
- [ ] DACL abuse identified (GenericAll, WriteDacl)?
