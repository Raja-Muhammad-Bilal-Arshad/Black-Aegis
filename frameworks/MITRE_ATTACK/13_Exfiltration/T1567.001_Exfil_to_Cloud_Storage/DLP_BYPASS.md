# DLP Bypass Guide: Cloud Storage (T1567.001)

## The Trusted Domain Problem
Most organizations *must* allow traffic to Google, Microsoft, and Dropbox for legitimate business operations. DLP systems struggle to differentiate between "Project_Report.docx" (Legit) and "Customer_Database.docx" (Stolen) if both go to `drive.google.com`.

## Evasion Techniques
1.  **Bring Your Own Key (BYOK)**: Attacker uses their *own* personal API keys/accounts, not the corporate one.
2.  **Encrypted Archives**: Uploading a password-protected ZIP (T1027). DLP cannot inspect the contents.
3.  **Renaming**: Renaming `passwords.txt` to `family_photos.jpg`.
