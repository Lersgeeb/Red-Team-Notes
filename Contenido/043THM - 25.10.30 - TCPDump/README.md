# Tcpdump and Packet Filtering Notes

## Overview

These notes summarize the main concepts and examples discussed regarding **tcpdump** usage and **packet filtering** in network analysis. Tcpdump is a powerful command-line tool used to capture and analyze packets transmitted over a network interface. Understanding how to filter and interpret packets is essential for troubleshooting, performance tuning, and network forensics.

---

## 1. Basic Tcpdump Commands

| Command | Description |
|----------|--------------|
| `tcpdump -i INTERFACE` | Capture packets on a specific network interface |
| `tcpdump -w FILE` | Write captured packets to a file |
| `tcpdump -r FILE` | Read packets from a capture file |
| `tcpdump -c COUNT` | Capture a defined number of packets |
| `tcpdump -n` | Do not resolve hostnames |
| `tcpdump -nn` | Do not resolve hostnames or protocol names |
| `tcpdump -v`, `-vv`, `-vvv` | Increase verbosity of packet details |
| `tcpdump -q` | Quick and quiet mode – brief packet info |
| `tcpdump -e` | Include MAC addresses in output |
| `tcpdump -A` | Display packets as ASCII text |
| `tcpdump -xx` | Display packets in hexadecimal |
| `tcpdump -X` | Display packets in both hex and ASCII |

---

## 2. Filtering Basics

| Command | Description |
|----------|--------------|
| `tcpdump host IP` | Filter by specific host IP or hostname |
| `tcpdump src host IP` | Filter by source host |
| `tcpdump dst host IP` | Filter by destination host |
| `tcpdump port PORT_NUMBER` | Filter by port number |
| `tcpdump src port PORT_NUMBER` | Filter by source port |
| `tcpdump dst port PORT_NUMBER` | Filter by destination port |
| `tcpdump PROTOCOL` | Filter by protocol (ip, ip6, icmp, etc.) |

---

## 3. Advanced Filters with pcap-filter

Tcpdump can filter packets based on header byte contents using the syntax:

```
proto[expr:size]
```
- **proto**: Protocol name (e.g., `ether`, `ip`, `tcp`, `udp`, `icmp`)
- **expr**: Byte offset (0 = first byte)
- **size**: Optional number of bytes (1, 2, or 4)

### Examples

- `ether[0] & 1 != 0` → Matches packets sent to a **multicast Ethernet address**.  
- `ip[0] & 0xf != 5` → Matches **IPv4 packets with header options** (non-standard header length).

The use of expressions like `!= 0` or `!= 5` helps identify packets **different from normal behavior** (e.g., non-zero bits or special options).

---

## 4. Filtering TCP Flags

Tcpdump allows inspection of TCP control flags using `tcp[tcpflags]`.

| Flag | Description |
|-------|--------------|
| `tcp-syn` | Synchronize connection |
| `tcp-ack` | Acknowledge data |
| `tcp-fin` | Finish connection |
| `tcp-rst` | Reset connection |
| `tcp-push` | Push data immediately |

### Examples
- `tcpdump "tcp[tcpflags] == tcp-syn"` → Only SYN packets  
- `tcpdump "tcp[tcpflags] & tcp-syn != 0"` → Packets with SYN flag set  
- `tcpdump "tcp[tcpflags] & (tcp-syn|tcp-ack) != 0"` → SYN or ACK packets  

---

## 5. Packet Length Filters

| Command | Description |
|----------|--------------|
| `greater LENGTH` | Capture packets greater or equal to a given size |
| `less LENGTH` | Capture packets smaller or equal to a given size |

---

## 6. Useful Header Knowledge

Understanding key network headers helps create precise filters.

### Ethernet Header
- Contains **source/destination MAC** and **protocol type (Ethertype)**.  
  Example: `ether proto 0x0800` → IPv4 packets.

### IP Header
- Fields include **TTL**, **Protocol**, **Source/Destination IP**, and **Header Length**.  
  Example: `ip[8] < 10` → Filter packets with low TTL.

### TCP Header
- Includes **ports**, **sequence numbers**, and **flags**.  
  Example: `tcp[tcpflags] & tcp-fin != 0` → TCP FIN packets.

### UDP Header
- Contains **source/destination ports** and **length**.  
  Example: `udp port 53` → DNS traffic.

### ICMP Header
- Used for control messages (e.g., ping).  
  Example: `icmp[0] == 8` → ICMP Echo Request.

---

## 7. Summary Notes

- `tcpdump` is a packet sniffer tool useful for debugging and monitoring network traffic.  
- Filters help reduce noise and target specific packets.  
- Binary operations (`&`, `!=`, `==`) allow precise control over header fields.  
- Understanding headers (Ethernet, IP, TCP, UDP, ICMP) is crucial for advanced filtering.  
- Use `man pcap-filter` to explore more complex filtering options.

---