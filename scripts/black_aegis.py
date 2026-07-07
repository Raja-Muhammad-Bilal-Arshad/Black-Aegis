#!/usr/bin/env python3
"""
Black Aegis - Main Orchestration Engine
Entry point for the penetration testing framework.
Manages engagements, agents, techniques, and reporting.
"""

import os
import sys
import json
import yaml
import hashlib
import argparse
import subprocess
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
AGENTS_DIR = BASE_DIR / "agents"
SKILLS_DIR = BASE_DIR / "skills"
WORKFLOWS_DIR = BASE_DIR / "workflows"
FRAMEWORKS_DIR = BASE_DIR / "frameworks"
SCRIPTS_DIR = BASE_DIR / "scripts"
ENGAGEMENTS_DIR = BASE_DIR / "engagements"
REPORTS_DIR = BASE_DIR / "reports"

class BlackAegis:
    """Main orchestration engine for Black Aegis Red Team framework."""

    VERSION = "2.0.0"
    CODENAME = "Black Aegis"

    def __init__(self):
        self.ensure_dirs()
        self.agents = self.load_agents()
        self.skills = self.load_skills()
        self.workflows = self.load_workflows()

    def ensure_dirs(self):
        """Ensure all required directories exist."""
        for d in [AGENTS_DIR, SKILLS_DIR, WORKFLOWS_DIR, FRAMEWORKS_DIR,
                  SCRIPTS_DIR, ENGAGEMENTS_DIR, REPORTS_DIR]:
            d.mkdir(parents=True, exist_ok=True)

    def load_agents(self):
        """Load all agent definitions."""
        agents = {}
        if AGENTS_DIR.exists():
            for f in AGENTS_DIR.glob("*.md"):
                if f.name.startswith("."):
                    continue
                try:
                    content = f.read_text()
                    # Parse YAML frontmatter
                    if content.startswith("---"):
                        end = content.find("---", 3)
                        if end != -1:
                            meta = yaml.safe_load(content[3:end])
                            if meta:
                                agents[f.stem] = {
                                    "name": meta.get("name", f.stem),
                                    "description": meta.get("description", ""),
                                    "skills": meta.get("skills", []),
                                    "file": str(f)
                                }
                except Exception:
                    agents[f.stem] = {"name": f.stem, "file": str(f)}
        return agents

    def load_skills(self):
        """Load all skill definitions."""
        skills = {}
        if SKILLS_DIR.exists():
            for f in SKILLS_DIR.glob("*.md"):
                if f.name.startswith("."):
                    continue
                try:
                    content = f.read_text()
                    if content.startswith("---"):
                        end = content.find("---", 3)
                        if end != -1:
                            meta = yaml.safe_load(content[3:end])
                            if meta:
                                skills[f.stem] = {
                                    "name": meta.get("name", f.stem),
                                    "description": meta.get("description", ""),
                                    "file": str(f)
                                }
                except Exception:
                    skills[f.stem] = {"name": f.stem, "file": str(f)}
        return skills

    def load_workflows(self):
        """Load all workflow definitions."""
        workflows = {}
        if WORKFLOWS_DIR.exists():
            for f in WORKFLOWS_DIR.glob("*.md"):
                if f.name.startswith("."):
                    continue
                try:
                    content = f.read_text()
                    if content.startswith("---"):
                        end = content.find("---", 3)
                        if end != -1:
                            meta = yaml.safe_load(content[3:end])
                            if meta:
                                workflows[f.stem] = {
                                    "name": meta.get("name", f.stem),
                                    "description": meta.get("description", ""),
                                    "file": str(f)
                                }
                except Exception:
                    workflows[f.stem] = {"name": f.stem, "file": str(f)}
        return workflows

    def banner(self):
        """Display the Black Aegis banner."""
        banner = f"""
╔══════════════════════════════════════════════════════════════╗
║                    BLACK AEGIS v{self.VERSION}                     ║
║              Elite Offensive Security Framework             ║
║                    "{self.CODENAME}"                        ║
╠══════════════════════════════════════════════════════════════╣
║  Agents: {len(self.agents):>3}  │  Skills: {len(self.skills):>3}  │  Workflows: {len(self.workflows):>3}  ║
║  MITRE Techniques: 656+  │  Scripts: 1242+                ║
╚══════════════════════════════════════════════════════════════╝
"""
        print(banner)

    def list_agents(self):
        """List all available agents."""
        print("\n╔══════════════════════════════════════════╗")
        print("║          AVAILABLE AGENTS                ║")
        print("╚══════════════════════════════════════════╝")
        for name, info in sorted(self.agents.items()):
            desc = info.get("description", "No description")[:50]
            skills = info.get("skills", [])
            skill_str = ", ".join(skills[:3]) if skills else "N/A"
            print(f"  {name:<35} │ {desc:<50} │ [{skill_str}]")

    def list_skills(self):
        """List all available skills."""
        print("\n╔══════════════════════════════════════════╗")
        print("║          AVAILABLE SKILLS                ║")
        print("╚══════════════════════════════════════════╝")
        for name, info in sorted(self.skills.items()):
            desc = info.get("description", "No description")[:60]
            print(f"  {name:<35} │ {desc}")

    def list_workflows(self):
        """List all available workflows."""
        print("\n╔══════════════════════════════════════════╗")
        print("║        AVAILABLE WORKFLOWS               ║")
        print("╚══════════════════════════════════════════╝")
        for name, info in sorted(self.workflows.items()):
            desc = info.get("description", "No description")[:60]
            print(f"  /{name:<34} │ {desc}")

    def list_techniques(self, tactic=None):
        """List MITRE ATT&CK techniques, optionally filtered by tactic."""
        mitre_dir = FRAMEWORKS_DIR / "MITRE_ATTACK"
        if not mitre_dir.exists():
            print("[!] MITRE ATT&CK framework not found")
            return

        tactics = sorted([d.name for d in mitre_dir.iterdir()
                         if d.is_dir() and d.name[0].isdigit()])

        if tactic:
            tactics = [t for t in tactics if tactic.lower() in t.lower()]

        for t in tactics:
            t_dir = mitre_dir / t
            techs = sorted([d.name for d in t_dir.iterdir() if d.is_dir()])
            print(f"\n  {t} ({len(techs)} techniques)")
            for tech in techs[:10]:
                print(f"    ├── {tech}")
            if len(techs) > 10:
                print(f"    └── ... and {len(techs) - 10} more")

    def create_engagement(self, name, target, scope=""):
        """Create a new engagement project."""
        eng_dir = ENGAGEMENTS_DIR / name
        eng_dir.mkdir(parents=True, exist_ok=True)

        # Create engagement structure
        (eng_dir / "scope.txt").write_text(f"Target: {target}\nScope: {scope}\nCreated: {datetime.now().isoformat()}\n")
        (eng_dir / "notes.md").write_text(f"# Engagement: {name}\n\n## Target\n{target}\n\n## Notes\n\n")
        (eng_dir / "tasks.md").write_text(f"# Tasks\n\n- [ ] Reconnaissance\n- [ ] Vulnerability Assessment\n- [ ] Exploitation\n- [ ] Post-Exploitation\n- [ ] Reporting\n")
        (eng_dir / "artifacts").mkdir(exist_ok=True)
        (eng_dir / "loot").mkdir(exist_ok=True)
        (eng_dir / "logs").mkdir(exist_ok=True)

        print(f"[+] Engagement '{name}' created at {eng_dir}")
        print(f"    Target: {target}")
        print(f"    Structure:")
        print(f"      ├── scope.txt")
        print(f"      ├── notes.md")
        print(f"      ├── tasks.md")
        print(f"      ├── artifacts/")
        print(f"      ├── loot/")
        print(f"      └── logs/")

        return eng_dir

    def run_workflow(self, workflow_name, engagement=None):
        """Execute a workflow."""
        wf = self.workflows.get(workflow_name)
        if not wf:
            print(f"[!] Workflow '{workflow_name}' not found")
            return

        print(f"\n[*] Executing workflow: /{workflow_name}")
        print(f"    Description: {wf.get('description', 'N/A')}")

        wf_file = Path(wf.get("file", ""))
        if wf_file.exists():
            content = wf_file.read_text()
            print(f"\n{content}")

        return True

    def check_tools(self):
        """Verify required tools are installed."""
        tools = {
            "nmap": "Network scanning",
            "masscan": "Fast port scanning",
            "sqlmap": "SQL injection",
            "hydra": "Brute force",
            "gobuster": "Directory enumeration",
            "nikto": "Web vulnerability scanning",
            "impacket-psexec": "Windows lateral movement",
            "evil-winrm": "WinRM shell",
            "proxychains": "Proxy chains",
            "curl": "HTTP requests",
            "wget": "File downloads",
            "python3": "Scripting",
            "git": "Version control",
        }

        print("\n╔══════════════════════════════════════════╗")
        print("║         TOOL VERIFICATION                ║")
        print("╚══════════════════════════════════════════╝")

        installed = 0
        missing = 0
        for tool, desc in sorted(tools.items()):
            result = subprocess.run(["which", tool], capture_output=True, text=True)
            if result.returncode == 0:
                print(f"  [✓] {tool:<25} │ {desc}")
                installed += 1
            else:
                print(f"  [✗] {tool:<25} │ {desc} (MISSING)")
                missing += 1

        print(f"\n  Installed: {installed}/{len(tools)}  │  Missing: {missing}")

    def generate_report(self, engagement):
        """Generate engagement report."""
        eng_dir = ENGAGEMENTS_DIR / engagement
        if not eng_dir.exists():
            print(f"[!] Engagement '{engagement}' not found")
            return

        report_dir = REPORTS_DIR / engagement
        report_dir.mkdir(parents=True, exist_ok=True)

        report = f"""# Black Aegis Engagement Report

**Engagement**: {engagement}
**Generated**: {datetime.now().isoformat()}
**Framework**: Black Aegis v{self.VERSION}

---

## Executive Summary

This report documents the findings from the penetration testing engagement
conducted using the Black Aegis Red Team framework.

## Scope

Target information and scope defined in engagement scope.txt.

## Methodology

The engagement followed the MITRE ATT&CK framework and NIST SP 800-115 guidelines.

### Phases
1. **Reconnaissance** - Information gathering
2. **Resource Development** - Infrastructure setup
3. **Initial Access** - Gaining entry
4. **Execution** - Running code on target
5. **Persistence** - Maintaining access
6. **Privilege Escalation** - Elevating permissions
7. **Defense Evasion** - Avoiding detection
8. **Credential Access** - Harvesting credentials
9. **Discovery** - Internal enumeration
10. **Lateral Movement** - Moving through network
11. **Collection** - Gathering data
12. **Command and Control** - Remote access
13. **Exfiltration** - Data extraction
14. **Impact** - Achieving objectives

## Findings

### Critical Findings
- [List critical findings here]

### High Findings
- [List high findings here]

### Medium Findings
- [List medium findings here]

### Low Findings
- [List low findings here]

## Recommendations

### Immediate Actions
1. [Critical remediation steps]

### Short-term
1. [High priority fixes]

### Long-term
1. [Strategic improvements]

## Appendices

### A. Tools Used
- Black Aegis Framework v{self.VERSION}
- MITRE ATT&CK Techniques Applied
- Standard penetration testing tools

### B. Timeline
[Add engagement timeline here]

### C. Raw Data
Refer to artifacts/ directory for raw scan data and evidence.

---
*Report generated by Black Aegis Red Team Framework*
*Authorized security testing only*
"""

        report_file = report_dir / "engagement_report.md"
        report_file.write_text(report)
        print(f"[+] Report generated: {report_file}")

    def interactive_mode(self):
        """Start interactive mode."""
        self.banner()
        print("Type 'help' for available commands.\n")

        while True:
            try:
                cmd = input("black-aegis> ").strip()
                if not cmd:
                    continue

                parts = cmd.split()
                action = parts[0].lower()

                if action in ("exit", "quit", "q"):
                    print("[*] Shutting down Black Aegis.")
                    break
                elif action == "help":
                    self.print_help()
                elif action == "agents":
                    self.list_agents()
                elif action == "skills":
                    self.list_skills()
                elif action == "workflows":
                    self.list_workflows()
                elif action == "techniques":
                    tactic = parts[1] if len(parts) > 1 else None
                    self.list_techniques(tactic)
                elif action == "engage":
                    if len(parts) >= 3:
                        self.create_engagement(parts[1], parts[2])
                    else:
                        print("Usage: engage <name> <target>")
                elif action == "workflow":
                    if len(parts) >= 2:
                        self.run_workflow(parts[1])
                    else:
                        self.list_workflows()
                elif action == "tools":
                    self.check_tools()
                elif action == "report":
                    if len(parts) >= 2:
                        self.generate_report(parts[1])
                    else:
                        print("Usage: report <engagement_name>")
                elif action == "version":
                    print(f"Black Aegis v{self.VERSION} ({self.CODENAME})")
                else:
                    print(f"Unknown command: {action}. Type 'help' for commands.")

            except KeyboardInterrupt:
                print("\n[*] Interrupted. Type 'exit' to quit.")
            except Exception as e:
                print(f"[!] Error: {e}")

    def print_help(self):
        """Print available commands."""
        print("""
╔══════════════════════════════════════════╗
║           AVAILABLE COMMANDS             ║
╚══════════════════════════════════════════╝
  help              Show this help message
  agents            List all agents
  skills            List all skills
  workflows         List all workflows
  techniques [tac]  List MITRE techniques (optional: filter by tactic)
  engage <n> <t>    Create new engagement
  workflow <name>   Run a workflow
  tools             Check installed tools
  report <engage>   Generate engagement report
  version           Show version info
  exit / quit       Exit Black Aegis
""")


def main():
    parser = argparse.ArgumentParser(description="Black Aegis Red Team Framework")
    parser.add_argument("-i", "--interactive", action="store_true", help="Start interactive mode")
    parser.add_argument("-l", "--list", choices=["agents", "skills", "workflows", "techniques"], help="List components")
    parser.add_argument("-e", "--engage", nargs=2, metavar=("NAME", "TARGET"), help="Create engagement")
    parser.add_argument("-w", "--workflow", help="Run workflow")
    parser.add_argument("-t", "--tools", action="store_true", help="Check tools")
    parser.add_argument("-r", "--report", metavar="ENGAGEMENT", help="Generate report")

    args = parser.parse_args()
    engine = BlackAegis()

    if args.interactive:
        engine.interactive_mode()
    elif args.list:
        if args.list == "agents":
            engine.list_agents()
        elif args.list == "skills":
            engine.list_skills()
        elif args.list == "workflows":
            engine.list_workflows()
        elif args.list == "techniques":
            engine.list_techniques()
    elif args.engage:
        engine.create_engagement(args.engage[0], args.engage[1])
    elif args.workflow:
        engine.run_workflow(args.workflow)
    elif args.tools:
        engine.check_tools()
    elif args.report:
        engine.generate_report(args.report)
    else:
        engine.banner()
        engine.print_help()


if __name__ == "__main__":
    main()
