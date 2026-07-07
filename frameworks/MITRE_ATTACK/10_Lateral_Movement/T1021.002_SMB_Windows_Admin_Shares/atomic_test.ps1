Write-Host "[*] T1021.002 - Remote Services: SMB / Admin Shares"

$Target = "127.0.0.1"

Write-Host "[*] Attempting Null Session to IPC$ share on $Target..."
# Usage: net use \\Target\IPC$ "" /u:""
$Cmd = "net use \\$Target\IPC$ `"`" /u:`"`""

Write-Host "[:] Executing: $Cmd"
Invoke-Expression $Cmd

if ($LASTEXITCODE -eq 0) {
    Write-Host "[+] Null session established successfully."
    Write-Host "[*] Cleanup: net use \\$Target\IPC$ /delete"
    net use "\\$Target\IPC$" /delete | Out-Null
} else {
    Write-Host "[-] Null session failed. Target might require auth."
}

Write-Host "[*] Note: PSEXEC and SMB lateral movement rely on ADMIN$ or C$ access."
