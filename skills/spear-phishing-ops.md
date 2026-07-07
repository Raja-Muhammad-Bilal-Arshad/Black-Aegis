---
name: spear-phishing-ops
description: Payload delivery, credential harvesting.
---

# Spear Phishing Operations Protocol

## 1. Principles
- **Context is King**: A generic "Invoice" fails. A "Q3 Budget Review" from the CFO succeeds.
- **Urgency**: Create a time constraint ("Action required by 5 PM").
- **Trust**: Spoof internal domains or partner domains.

## 2. Techniques
- **Credential Harvesting**: Clone the O365 login page. Capture MFA tokens.
- **Payload Delivery**:
    - HTML Smuggling (files build themselves in browser)
    - OneNote attachments (.one)
    - Password protected Zips (bypasses Scanners)

## 3. Checklist
- [ ] Domain reputation warmed up?
- [ ] SPF/DKIM/DMARC configured?
- [ ] Landing page has SSL?
- [ ] Typosquatting domain registered?
