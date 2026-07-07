Write-Host "[*] T1021.004 - Remote Services: SSH"

Write-Host "This test simulates the logic of using an SSH key. It does not connect."

$KeyPath = "$env:USERPROFILE\.ssh\id_rsa"
$Hosts = @("192.168.1.10", "192.168.1.11")

if (Test-Path $KeyPath) {
    Write-Host "[+] Found private key at: $KeyPath"
} else {
    Write-Host "[-] No default private key found (this is common)."
}

foreach ($HostName in $Hosts) {
    Write-Host "[*] Emulating: ssh -i $KeyPath root@$HostName"
    # Actual command: ssh -i $KeyPath root@$HostName
}
