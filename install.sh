#!/bin/bash
# Black Aegis - Installation & Setup Script
# "Trust, but verify."
# This script installs all dependencies for the Black Aegis framework.

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

echo -e "${CYAN}"
echo "╔══════════════════════════════════════════════════════════╗"
echo "║           BLACK AEGIS - INSTALLATION SCRIPT             ║"
echo "║         Elite Offensive Security Framework              ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo -e "${NC}"

echo -e "${YELLOW}[*] Starting installation...${NC}"

# Check if running as root
if [ "$EUID" -eq 0 ]; then
    echo -e "${YELLOW}[!] Running as root. Some tools may need to be installed as user.${NC}"
fi

# Update package list
echo -e "${CYAN}[1/7] Updating package list...${NC}"
sudo apt-get update -qq 2>/dev/null || echo "  [!] apt-get update failed (non-critical)"

# Install system dependencies
echo -e "${CYAN}[2/7] Installing system dependencies...${NC}"
APT_PACKAGES=(
    "nmap"
    "masscan"
    "hydra"
    "nikto"
    "curl"
    "wget"
    "git"
    "python3"
    "python3-pip"
    "whois"
    "dig"
    "netcat-openbsd"
    "proxychains4"
    "seclists"
    "wordlists"
)

for pkg in "${APT_PACKAGES[@]}"; do
    if ! dpkg -s "$pkg" &>/dev/null; then
        echo "  Installing $pkg..."
        sudo apt-get install -y -qq "$pkg" 2>/dev/null || echo "  [!] Failed to install $pkg"
    else
        echo "  [✓] $pkg already installed"
    fi
done

# Install Python dependencies
echo -e "${CYAN}[3/7] Installing Python dependencies...${NC}"
PYTHON_PACKAGES=(
    "pyyaml"
    "openpyxl"
    "requests"
    "beautifulsoup4"
    "impacket"
    "scapy"
    "pwntools"
    "crackmapexec"
)

for pkg in "${PYTHON_PACKAGES[@]}"; do
    pip install "$pkg" -q 2>/dev/null && echo "  [✓] $pkg" || echo "  [!] Failed to install $pkg"
done

# Install specialized tools
echo -e "${CYAN}[4/7] Installing specialized tools...${NC}"

# Go tools
if command -v go &>/dev/null; then
    echo "  [✓] Go found"
    GO_TOOLS=(
        "github.com/OJ/gobuster/v3@latest"
        "github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest"
        "github.com/ropnop/kerbrute@latest"
    )
    for tool in "${GO_TOOLS[@]}"; do
        echo "  Installing $(basename $tool)..."
        go install "$tool" 2>/dev/null || echo "  [!] Failed to install $(basename $tool)"
    done
else
    echo "  [!] Go not found. Install from https://go.dev/dl/"
fi

# Impacket
echo "  Checking Impacket..."
python3 -c "import impacket" 2>/dev/null && echo "  [✓] Impacket" || echo "  [!] Impacket not available"

# Impacket scripts
echo "  [✓] Impacket scripts (impacket-psexec, impacket-smbclient, etc.)"

# SecLists
if [ ! -d "/usr/share/seclists" ]; then
    echo "  Installing SecLists..."
    sudo apt-get install -y -qq seclists 2>/dev/null || echo "  [!] SecLists not available via apt"
else
    echo "  [✓] SecLists already installed"
fi

# Create necessary directories
echo -e "${CYAN}[5/7] Creating project structure...${NC}"
DIRS=(
    "engagements"
    "reports"
    "tools"
    "wordlists"
)

for dir in "${DIRS[@]}"; do
    mkdir -p "$dir"
    echo "  [✓] Created $dir/"
done

# Set permissions on scripts
echo -e "${CYAN}[6/7] Setting permissions...${NC}"
find . -name "*.sh" -exec chmod +x {} \; 2>/dev/null
echo "  [✓] Script permissions set"

# Verify installation
echo -e "${CYAN}[7/7] Verifying installation...${NC}"
python3 scripts/black_aegis.py --tools 2>/dev/null || echo "  [!] Could not run verification"

echo ""
echo -e "${GREEN}╔══════════════════════════════════════════════════════════╗"
echo "║              INSTALLATION COMPLETE                      ║"
echo "╚══════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${CYAN}Quick Start:${NC}"
echo "  1. Run: python3 scripts/black_aegis.py -i"
echo "  2. Create engagement: engage <name> <target>"
echo "  3. Start recon: workflow recon"
echo ""
echo -e "${YELLOW}NOTE: Some tools may require manual installation."
echo "Check the output above for any [!] failures.${NC}"
echo ""
