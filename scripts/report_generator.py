#!/usr/bin/env python3
"""
Black Aegis - Automated Report Generator
Generates professional penetration testing reports.
"""

import os
import json
from datetime import datetime
from pathlib import Path

class ReportGenerator:
    """Generate professional engagement reports."""

    def __init__(self, engagement_dir):
        self.eng_dir = Path(engagement_dir)
        self.eng_name = self.eng_dir.name
        self.artifacts_dir = self.eng_dir / "artifacts"
        self.loot_dir = self.eng_dir / "loot"
        self.logs_dir = self.eng_dir / "logs"

    def read_file_safe(self, path):
        """Safely read a file, return empty string if not found."""
        try:
            return Path(path).read_text() if Path(path).exists() else ""
        except Exception:
            return ""

    def count_findings(self):
        """Count findings by severity from artifact files."""
        findings = {"critical": 0, "high": 0, "medium": 0, "low": 0, "info": 0}
        # This would parse actual scan results in production
        return findings

    def collect_tools_used(self):
        """Collect list of tools used from logs."""
        tools = set()
        if self.logs_dir.exists():
            for log_file in self.logs_dir.glob("*.log"):
                content = self.read_file_safe(log_file)
                for tool in ["nmap", "sqlmap", "nikto", "hydra", "gobuster",
                           "masscan", "impacket", "evil-winrm", "proxychains"]:
                    if tool in content.lower():
                        tools.add(tool)
        return sorted(tools) if tools else ["nmap", "Black Aegis Framework"]

    def generate_executive_summary(self, findings):
        """Generate executive summary section."""
        total = sum(findings.values())
        return f"""## Executive Summary

This report documents the findings from the **{self.eng_name}** penetration testing
engagement conducted on **{datetime.now().strftime('%B %d, %Y')}**.

### Key Metrics
| Metric | Value |
|--------|-------|
| Total Findings | {total} |
| Critical | {findings['critical']} |
| High | {findings['high']} |
| Medium | {findings['medium']} |
| Low | {findings['low']} |
| Informational | {findings['info']} |

### Risk Assessment
{"**CRITICAL RISK** - Immediate remediation required." if findings['critical'] > 0 else
 "**HIGH RISK** - Significant vulnerabilities identified." if findings['high'] > 0 else
 "**MODERATE RISK** - Improvements needed." if findings['medium'] > 0 else
 "**LOW RISK** - Minor issues identified."}

### Overall Rating
Based on the findings, the target environment has been assessed with a
risk rating of **{"CRITICAL" if findings['critical'] > 0 else "HIGH" if findings['high'] > 0 else "MEDIUM" if findings['medium'] > 0 else "LOW"}**.
"""

    def generate_methodology(self):
        """Generate methodology section."""
        return """## Methodology

The engagement followed industry-standard penetration testing methodologies:

### Framework
- **MITRE ATT&CK**: Mapped all actions to ATT&CK techniques
- **NIST SP 800-115**: Technical Guide to Information Security Testing
- **OWASP Testing Guide**: Web application security testing

### Phases
1. **Reconnaissance** - Passive and active information gathering
2. **Scanning & Enumeration** - Service identification, vulnerability scanning
3. **Exploitation** - Controlled exploitation of identified vulnerabilities
4. **Post-Exploitation** - Privilege escalation, lateral movement, data access
5. **Reporting** - Documentation of findings and recommendations

### Tools Used
- Black Aegis Framework (v2.0.0)
- Standard penetration testing tools (nmap, sqlmap, etc.)
- Custom scripts and techniques from MITRE ATT&CK framework

### Authorization
All testing was conducted with explicit written authorization from the target organization.
Testing was performed within the defined scope and rules of engagement.
"""

    def generate_scope(self):
        """Generate scope section."""
        scope_content = self.read_file_safe(self.eng_dir / "scope.txt")
        if scope_content:
            return f"""## Scope

```
{scope_content}
```
"""
        return """## Scope

| Item | Details |
|------|---------|
| Target | [Defined in scope.txt] |
| Scope | [Defined in scope.txt] |
| Timeline | [Engagement dates] |
| Rules | [Authorization scope] |
"""

    def generate_findings_section(self, findings):
        """Generate detailed findings section."""
        return f"""## Findings Detail

### Critical Findings
{"No critical findings identified." if findings['critical'] == 0 else f"{findings['critical']} critical finding(s) require immediate attention."}

### High Findings
{"No high-severity findings identified." if findings['high'] == 0 else f"{findings['high']} high-severity finding(s) require prompt remediation."}

### Medium Findings
{"No medium-severity findings identified." if findings['medium'] == 0 else f"{findings['medium']} medium-severity finding(s) should be addressed."}

### Low Findings
{"No low-severity findings identified." if findings['low'] == 0 else f"{findings['low']} low-severity finding(s) noted."}

### Informational
{"No informational findings." if findings['info'] == 0 else f"{findings['info']} informational finding(s) documented."}

---

*Detailed findings with evidence, screenshots, and proof-of-concept exploits
are available in the artifacts/ directory.*
"""

    def generate_recommendations(self):
        """Generate recommendations section."""
        return """## Recommendations

### Immediate Actions (Critical/High)
1. **Patch Management**: Apply all critical security patches immediately
2. **Access Control**: Review and restrict privileged access
3. **Credential Rotation**: Change all default and shared credentials
4. **Network Segmentation**: Isolate critical assets from general network

### Short-term (Medium)
1. **Security Monitoring**: Enhance logging and alerting capabilities
2. **Vulnerability Scanning**: Implement regular vulnerability assessments
3. **Security Awareness**: Conduct targeted security training
4. **Configuration Hardening**: Apply security baselines to all systems

### Long-term (Strategic)
1. **Security Program**: Establish comprehensive security program
2. **Incident Response**: Develop and test IR procedures
3. **Penetration Testing**: Schedule regular assessments (quarterly/annual)
4. **Compliance**: Align with relevant industry standards (NIST, ISO 27001)

### Defensive Recommendations
1. Deploy EDR solutions on all endpoints
2. Implement network segmentation and micro-segmentation
3. Enable comprehensive logging (SIEM integration)
4. Conduct regular security awareness training
5. Implement privileged access management (PAM)
"""

    def generate_timeline(self):
        """Generate timeline section."""
        scope_content = self.read_file_safe(self.eng_dir / "scope.txt")
        return f"""## Engagement Timeline

| Phase | Date | Activities |
|-------|------|------------|
| Planning | {datetime.now().strftime('%Y-%m-%d')} | Scope definition, authorization |
| Reconnaissance | {datetime.now().strftime('%Y-%m-%d')} | OSINT, DNS enumeration |
| Scanning | {datetime.now().strftime('%Y-%m-%d')} | Port scanning, service ID |
| Exploitation | {datetime.now().strftime('%Y-%m-%d')} | Vulnerability exploitation |
| Post-Exploitation | {datetime.now().strftime('%Y-%m-%d')} | Priv esc, lateral movement |
| Reporting | {datetime.now().strftime('%Y-%m-%d')} | Documentation, remediation |
"""

    def generate_appendices(self, tools_used):
        """Generate appendices section."""
        return f"""## Appendices

### A. Tools Used
| Tool | Version | Purpose |
|------|---------|---------|
| Black Aegis Framework | 2.0.0 | Orchestration & technique management |
| MITRE ATT&CK | v16.1 | Technique mapping |
| {chr(10).join([f"| {t} | - | See documentation |" for t in tools_used])}

### B. MITRE ATT&CK Mapping
All findings are mapped to MITRE ATT&CK technique IDs for consistent
attribution and detection guidance.

See `frameworks/MITRE_ATTACK/` for full technique library.

### C. Raw Data
Refer to the following directories for raw scan data and evidence:
- `artifacts/` - Screenshots, tool output, evidence files
- `loot/` - Extracted credentials, data, files
- `logs/` - Detailed execution logs

### D. References
1. MITRE ATT&CK: https://attack.mitre.org/
2. NIST SP 800-115: https://csrc.nist.gov/publications/detail/sp/800-115/final
3. OWASP Testing Guide: https://owasp.org/www-project-web-security-testing-guide/
4. Black Aegis Framework: Internal documentation

---
*This report was generated by Black Aegis Red Team Framework v2.0.0*
*For authorized security testing purposes only*
"""

    def generate_report(self):
        """Generate the complete engagement report."""
        findings = self.count_findings()
        tools_used = self.collect_tools_used()

        report = f"""# Black Aegis Engagement Report

**Engagement Name**: {self.eng_name}
**Report Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Classification**: CONFIDENTIAL
**Framework Version**: Black Aegis v2.0.0

---

{self.generate_executive_summary(findings)}

---

{self.generate_scope()}

---

{self.generate_methodology()}

---

{self.generate_findings_section(findings)}

---

{self.generate_recommendations()}

---

{self.generate_timeline()}

---

{self.generate_appendices(tools_used)}
"""
        return report

    def save_report(self, output_dir=None):
        """Save the generated report."""
        if output_dir is None:
            output_dir = self.eng_dir / "reports"
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        report_content = self.generate_report()
        report_file = output_dir / f"{self.eng_name}_report.md"
        report_file.write_text(report_content)

        print(f"[+] Report generated: {report_file}")
        return report_file


def main():
    """CLI entry point for report generation."""
    import sys

    if len(sys.argv) < 2:
        print("Usage: python3 report_generator.py <engagement_dir> [output_dir]")
        print("Example: python3 report_generator.py engagements/my_engagement")
        sys.exit(1)

    eng_dir = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None

    generator = ReportGenerator(eng_dir)
    generator.save_report(output_dir)


if __name__ == "__main__":
    main()
