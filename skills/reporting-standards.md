---
name: reporting-standards
description: Executive summaries vs Technical breakdown.
---

# Reporting Standards Protocol

## 1. Principles
- **Bottom Line Up Front (BLUF)**: The CEO should understand the risk in the first paragraph.
- **Reproducibility**: A junior dev should be able to reproduce the finding using your steps.
- **Impact > Technicality**: "We got RCE" -> "We can steal all customer data".

## 2. Structure
- **Executive Summary**: High-level risk, business impact, strategic recommendations.
- **Attack Narrative**: Story format of the kill chain.
- **Technical Findings**:
    - Vulnerability Name
    - Severity (Critical/High/Med/Low)
    - CVSS Score
    - Proof of Concept (Screenshots/Code)
    - Remediation

## 3. Checklist
- [ ] Spell checked?
- [ ] Screenshots sanitized (no other client data)?
- [ ] Risk rated correctly?
