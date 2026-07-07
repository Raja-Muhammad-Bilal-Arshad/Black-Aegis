Write-Host "[*] T1550.003 - Use Alternate Authentication Material: Pass the Ticket"

Write-Host "[*] Concept:"
Write-Host "    Attackers export a Kerberos Ticket (TGT or TGS) and inject it into their session session."

Write-Host "[*] Commands (Mimikatz):"
Write-Host "    kerberos::ptt <ticket.kirbi>"

Write-Host "[*] Detection Logic (Klist):"
Write-Host "    Running 'klist' to show current tickets..."
klist

Write-Host "[*] Note: If you see tickets for a different user than the one logged in, or strange lifetimes, suspect PtT."
