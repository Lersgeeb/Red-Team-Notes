# tshark Notes

## Summary
This document provides a quick reference guide to using **tshark**, the command-line version of **Wireshark**. It covers installation steps, basic and advanced commands, filtering options, and practical examples for network traffic analysis. These notes are intended for personal study and quick recall.

## Installation
```bash
# On Debian/Ubuntu
sudo apt update
sudo apt install tshark

# On macOS (Homebrew)
brew install wireshark

# On Windows
# tshark is included with the Wireshark installation
```

## Common Protocol Filters

| Protocol | Filter Example | Description |
|-----------|----------------|--------------|
| HTTP | `-Y "http"` | Shows HTTP traffic |
| HTTPS | `-f "port 443"` | Captures HTTPS packets |
| DNS | `-Y "dns"` | Filters DNS requests and responses |
| ICMP | `-Y "icmp"` | Captures ping and network errors |
| ARP | `-Y "arp"` | Captures ARP requests/responses |
| DHCP | `-Y "bootp"` | Filters DHCP packets |
| FTP | `-Y "ftp"` | Captures FTP traffic |
| SMTP | `-Y "smtp"` | Filters email protocol traffic |

---

## Parameter Summary Table

| Parameter | Description | Example |
|------------|--------------|----------|
| `-i` | Selects the network interface | `-i eth0` |
| `-D` | Lists available interfaces | `tshark -D` |
| `-c` | Limits the number of packets captured | `-c 100` |
| `-a duration:X` | Stops capture after X seconds | `-a duration:30` |
| `-w` | Writes output to file (.pcap) | `-w output.pcap` |
| `-r` | Reads packets from a file | `-r file.pcap` |
| `-f` | Capture filter (BPF syntax) | `-f "port 80"` |
| `-Y` | Display filter (Wireshark syntax) | `-Y "ip.src == 10.0.0.1"` |
| `-T fields` | Custom field output format | `-T fields -e ip.src` |
| `-e` | Selects which fields to display | `-e ip.src -e ip.dst` |

---

## Basic Commands
```bash
# List available network interfaces
tshark -D

# Capture packets on a specific interface
sudo tshark -i eth0

# Save capture to a file
sudo tshark -i eth0 -w capture.pcap

# Read and display packets from a saved file
tshark -r capture.pcap
```

## Filtering Examples
```bash
# Capture only HTTP traffic
sudo tshark -i eth0 -f "port 80"

# Display only packets from a specific source IP
tshark -r capture.pcap -Y "ip.src == 192.168.1.10"

# Capture only TCP or UDP traffic
tshark -f "tcp"
tshark -f "udp"
```

## Displaying Specific Fields
```bash
tshark -r capture.pcap -T fields -e ip.src -e ip.dst -e tcp.port
```

## Limited Capture
```bash
# Capture 100 packets only
tshark -i eth0 -c 100
```

## Timed Capture Example
```bash
# Capture HTTP traffic for 30 seconds
sudo tshark -i eth0 -a duration:30 -f "tcp port 80" -w http.pcap
```