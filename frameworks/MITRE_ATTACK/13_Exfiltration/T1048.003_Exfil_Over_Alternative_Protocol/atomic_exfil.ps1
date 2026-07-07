<#
    Technique: T1048.003
    Name: Exfil Over Alternative Protocol: Unencrypted/Obfuscated (ICMP)
    Description: Padding PING packets with stolen data.
#>

Write-Host "[*] EXECUTING ATOMIC SMUGGLER (ICMP/Ping)..." -ForegroundColor Cyan

$secret = "CONFIDENTIAL_DATA_CHUNKS"
$target = "127.0.0.1"

Write-Host "[>] Sending Data via Ping to $target..."

# Windows Ping allows specifying buffer size (-l) but not content directly via command line easily without raw sockets.
# Linux ping allows -p for pattern.
# Here we simulate 'Large Packet' exfil behavior which DLP might flag.

# Send large pings (1000 bytes)
ping.exe $target -n 5 -l 1000

Write-Host "[*] ICMP Traffic Generated."
Write-Host "[!] Note: Real ICMP exfil tools (like generic-icmp-tunnel) verify payload integrity."
