<#
    Technique: T1020
    Name: Automated Exfiltration
    Description: Monitoring a directory and automatically uploading new files.
#>

Write-Host "[*] EXECUTING ATOMIC SMUGGLER (Watchdog)..." -ForegroundColor Cyan

$watchFolder = "$env:TEMP\T1020_Watch"
New-Item -ItemType Directory -Force -Path $watchFolder | Out-Null

Write-Host "[>] Watching $watchFolder for 10 seconds..."

# Setup FileSystemWatcher
$watcher = New-Object System.IO.FileSystemWatcher
$watcher.Path = $watchFolder
$watcher.Filter = "*.*"
$watcher.IncludeSubdirectories = $false
$watcher.EnableRaisingEvents = $true

$action = {
    $path = $Event.SourceEventArgs.FullPath
    Write-Host "[!] New file detected: $path" -ForegroundColor Red
    Write-Host "[>] AUTOMATED EXFIL INITIATED for $path" 
    # Add upload logic here
}

$eventJob = Register-ObjectEvent $watcher "Created" -Action $action

# Trigger
Start-Sleep -Seconds 2
Set-Content "$watchFolder\passwords.txt" "secret"
Start-Sleep -Seconds 2

# Cleanup
Unregister-Event -SourceIdentifier $eventJob.Name
Remove-Item $watchFolder -Recurse -Force
Write-Host "[*] Watchdog Test Complete."
