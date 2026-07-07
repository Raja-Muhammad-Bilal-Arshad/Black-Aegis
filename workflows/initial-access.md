---
description: Execute phish or exploit
---

# Initial Access Workflow

## 1. Phishing (Social)
1.  **Send**: Launch campaign via Gophish.
2.  **Monitor**: Watch for "Email Opened" -> "Link Clicked" -> "Payload Downloaded".
3.  **Catch**: Wait for Callback (C2 Beacon).

## 2. Application Exploitation (Technical)
1.  **Target**: Vulnerable web app or public service.
2.  **Exploit**: Send payload (serialized object, SQLi, RCE).
3.  **Stabilize**: If shell is unstable (web shell), upgrade to C2 beacon immediately.

## 3. Physical/Hardware
1.  **Plant**: Dropout Device (Raspberry Pi/Lan Turtle) connected to ethernet.
2.  **Reverse SSH**: Phone home to C2 infrastructure.
