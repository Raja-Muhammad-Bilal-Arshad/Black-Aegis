# OPSEC Warnings: T1563.002 - RDP Hijacking (T1563.002)

## ⚠️ CRITICAL WARNINGS

### Detection Risk
- **Level**: varies by technique and environment
- **Detection Sources**: Security logs, EDR, network monitoring

### Evidence Left Behind
- Process creation events
- File system artifacts
- Network connections
- Registry modifications
- Log entries

### Cleanup Checklist
- [ ] Remove dropped files
- [ ] Restore modified configurations
- [ ] Clear relevant logs (if authorized)
- [ ] Remove created users/schedules
- [ ] Restore network settings

### Timing
- **Best Window**: Business hours (blends with normal activity) or maintenance windows
- **Avoid**: High-security monitoring periods

### Network Considerations
- Use encrypted channels
- Proxy through multiple hops
- Match normal traffic patterns
- Avoid beaconing patterns

### Endpoint Considerations
- Memory-only execution when possible
- Avoid known malicious signatures
- Use signed binaries when possible
- Don't trigger AV/EDR alerts

## Legal Notice
Only perform this technique with explicit written authorization.
Unauthorized use is illegal and unethical.
