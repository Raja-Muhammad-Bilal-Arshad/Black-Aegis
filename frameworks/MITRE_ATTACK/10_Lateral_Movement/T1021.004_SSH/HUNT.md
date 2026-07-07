# T1021.004 - SSH Hunting Guide

## Log Artifacts (Linux)

- `/var/log/auth.log` or `/var/log/secure`
- **Accepted publickey**: Successful key auth.
- **Accepted password**: Successful password auth.

## Windows (e.g., OpenSSH Server)
- **Event 4624**: Logon Type 3 (if network) or similar depending on implementation.
- **PowerShell/Sysmon**: Process execution `ssh.exe` or `sshd.exe`.

## Indicators
- High volume of connections from one host to many (SSH Worm/Scanner).
- Root logins (if permitted).
