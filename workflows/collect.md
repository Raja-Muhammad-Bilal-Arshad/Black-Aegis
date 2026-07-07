---
description: Identify & stage sensitive data
---

# Collection Workflow

## 1. Discovery
1.  **File Search**:
    - `dir /s *password*`, `*budget*`, `*confidential*`.
    - `find / -name "*.db"`.
2.  **Browser Data**: Dump Chrome/Firefox cookies and saved logins.
3.  **Email**: Download local Outlook `.ost` or `.pst` files.

## 2. Staging
1.  **Location**: Pick a temp folder (e.g., `C:\Windows\Temp` or `%APPDATA%`).
2.  **Encryption**: Compress with password protection.
    - `7z a -pSecret123 data.7z C:\Data\`
    - `tar -czvf - /data | openssl des3 -salt -out data.tar.gz`
