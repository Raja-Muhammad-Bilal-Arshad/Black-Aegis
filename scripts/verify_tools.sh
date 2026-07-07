#!/bin/bash

# Black Aegis Tool Verification Script
# "Trust, but verify."

echo "[*] Initializing Orbital Tool Check..."

# Tool List
TOOLS=("nmap" "msfconsole" "proxychains" "sqlmap" "burpsuite" "gobuster" "impacket-psexec")

MISSING=0

for tool in "${TOOLS[@]}"; do
    if command -v $tool &> /dev/null; then
        echo -e "[\e[32m+\e[0m] $tool found: $(which $tool)"
    else
        echo -e "[\e[31m-\e[0m] $tool MISSING!"
        MISSING=$((MISSING+1))
    fi
done

echo "----------------------------------------"
if [ $MISSING -eq 0 ]; then
    echo "[*] System Ready. All systems nominal."
    exit 0
else
    echo "[!] Critical System Failure. $MISSING tools missing."
    echo "[!] Run: sudo apt install <tool>"
    exit 1
fi
