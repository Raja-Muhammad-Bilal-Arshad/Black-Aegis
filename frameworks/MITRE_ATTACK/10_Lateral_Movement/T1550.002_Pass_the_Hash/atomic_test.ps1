Write-Host "[*] T1550.002 - Use Alternate Authentication Material: Pass the Hash"
Write-Host "This script explains the methodology. We do NOT execute offensive binaries here."

Write-Host "[*] Concept:"
Write-Host "    Attackers use the NTLM hash of a user to authenticate via SMB/WMI without knowing the plaintext password."

Write-Host "[*] Common Tools:"
Write-Host "    1. Mimikatz: sekurlsa::pth /user:Administrator /domain:. /ntlm:<HASH>"
Write-Host "    2. Invoke-TheHash (PowerShell)"
Write-Host "    3. Impacket (psexec.py -hashes <LM:NT> ...)"

Write-Host "[*] Detection Logic Simulation:"
Write-Host "    Generating a 'Network' logon (Type 3) using alternate credentials..."
# This is a weak simulation, but generating Type 3 without corresponding Type 4648 is the goal of detection.
