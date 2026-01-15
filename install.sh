#!/bin/bash
# BlueSkyOSINT Installation Script

echo "═══════════════════════════════════════════════════════════"
echo "           BlueSkyOSINT - Installation Script              "
echo "═══════════════════════════════════════════════════════════"
echo ""

# Check Python version
echo "[*] Checking Python version..."
if ! command -v python3 &> /dev/null; then
    echo "[!] Python 3 not found. Please install Python 3.7 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "[+] Found Python $PYTHON_VERSION"

# Check if pip is available
echo "[*] Checking pip..."
if ! command -v pip3 &> /dev/null; then
    echo "[!] pip3 not found. Please install pip."
    exit 1
fi
echo "[+] pip3 found"

# Install dependencies
echo ""
echo "[*] Installing dependencies..."
pip3 install -r requirements.txt --break-system-packages 2>/dev/null || pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "[+] Dependencies installed successfully"
else
    echo "[!] Failed to install dependencies"
    exit 1
fi

# Make script executable
echo ""
echo "[*] Making script executable..."
chmod +x blueskyosint.py

echo ""
echo "═══════════════════════════════════════════════════════════"
echo "            Installation Complete!                          "
echo "═══════════════════════════════════════════════════════════"
echo ""
echo "To run BlueSkyOSINT:"
echo "  python3 blueskyosint.py"
echo ""
echo "For OPSEC (with Tor):"
echo "  proxychains4 python3 blueskyosint.py"
echo ""
echo "═══════════════════════════════════════════════════════════"
