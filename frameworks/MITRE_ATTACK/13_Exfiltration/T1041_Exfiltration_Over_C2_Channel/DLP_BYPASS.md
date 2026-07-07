# DLP Bypass Guide: Exfiltration Over C2 (T1041)

## Detection Challenge
Since the data goes over the C2 channel (often encrypted HTTPS), Network DLP appliances cannot inspect the content unless they perform **SSL Inspection (Man-in-the-Middle)**.

## Evasion Techniques
1.  **Traffic Blending**: Matching the size and frequency of normal web traffic. Don't send 10GB in one go.
2.  **Chunking**: Break data into small 50KB chunks. Send them over hours.
3.  **Encoding**: Use custom encodings (e.g., XOR with a rolling key) inside the TLS stream to defeat "pattern matching" if SSL inspection is active.
4.  **Jitter**: Add random delays between chunks to defeat "Beaconing" detection.
