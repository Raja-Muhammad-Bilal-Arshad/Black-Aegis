Write-Host "[*] T1021.006 - Remote Services: Windows Remote Management (WinRM)"

$Target = "localhost"

Write-Host "[*] Testing WinRM availability..."
$Result = Test-WSMan -ComputerName $Target -ErrorAction SilentlyContinue

if ($Result) {
    Write-Host "[+] WinRM is responding on $Target"
    Write-Host "[*] Protocol Version: $($Result.ProductVersion)"
    
    Write-Host "[*] Emulating Invoke-Command:"
    Write-Host "    Invoke-Command -ComputerName $Target -ScriptBlock { Get-Process notepad }"
} else {
    Write-Host "[-] WinRM not accessible (Service might be stopped or blocked)."
}

Write-Host "[*] Evil-WinRM and PS-Remoting rely on this service (Ports 5985/5986)."
