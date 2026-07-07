Write-Host "[*] T1570 - Lateral Tool Transfer"

$Source = "$env:SystemRoot\System32\notepad.exe"
$Dest = "$env:TEMP\atomic_transfer_test.exe"

Write-Host "[*] Simulating tool staging via Copy-Item..."
Write-Host "    Source: $Source"
Write-Host "    Dest:   $Dest"

Copy-Item -Path $Source -Destination $Dest -Force

if (Test-Path $Dest) {
    Write-Host "[+] File copied successfully."
    $Hash = Get-FileHash $Dest
    Write-Host "    Hash: $($Hash.Hash)"
    
    Write-Host "[*] Cleanup..."
    Remove-Item $Dest -Force
} else {
    Write-Host "[-] Copy failed."
}

Write-Host "[*] Real-world equivalence:"
Write-Host "    - SCP / SFTP"
Write-Host "    - SMB Copy"
Write-Host "    - Certutil -urlcache -split -f <url> <file>"
