Write-Host "[*] T1021.001 - Remote Services: RDP"

$Target = "127.0.0.1"

Write-Host "[*] Checking connectivity to RDP port (3389) on $Target..."
$Result = Test-NetConnection -ComputerName $Target -Port 3389 -InformationLevel Quiet

if ($Result) {
    Write-Host "[+] RDP Port is OPEN on $Target"
    Write-Host "[*] To simulate full connection (Interactive): mstsc /v:$Target"
} else {
    Write-Host "[-] RDP Port is CLOSED or blocked on $Target"
}

Write-Host "[*] Key Indicator: Successful RDP login generates Event 4624 (Logon Type 10)."
