---
description: Steal data covertly
---

# Exfiltration Workflow

## 1. Channel Selection
1.  **HTTPS**: Standard POST requests (looks like file upload).
2.  **DNS**: Encode data in subdomains (very slow, very stealthy).
3.  **Cloud Sync**: Upload to legitimate DropBox/Google Drive (often allowlisted).

## 2. Execution
1.  **Throttling**: Don't upload 10GB in 5 minutes. Spread it out.
2.  **User-Agent**: Match the standard browser of the organization.

## 3. Cleanup
1.  **Delete**: Remove the staged archives.
2.  **Wipe**: SDelete (Secure Delete) if possible, or just normal delete.
