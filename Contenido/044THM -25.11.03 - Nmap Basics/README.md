# Nmap Basics

## Overview
This document summarizes key concepts and commands learned during the Nmap exploration session. It serves as a personal learning note for future reference.

---

## Key Topics

### 1. Host Discovery
- `-sL`: List scan – lists targets without scanning.
- `-sn`: Ping scan – performs host discovery only.

#### 1.1 Initial Recon
| Tipo de escaneo        | Comando de ejemplo                          |
| ---------------------- | ------------------------------------------- |
| ARP Scan               | `sudo nmap -PR -sn MACHINE_IP/24`           |
| ICMP Echo Scan         | `sudo nmap -PE -sn MACHINE_IP/24`           |
| ICMP Timestamp Scan    | `sudo nmap -PP -sn MACHINE_IP/24`           |
| ICMP Address Mask Scan | `sudo nmap -PM -sn MACHINE_IP/24`           |
| TCP SYN Ping Scan      | `sudo nmap -PS22,80,443 -sn MACHINE_IP/30`  |
| TCP ACK Ping Scan      | `sudo nmap -PA22,80,443 -sn MACHINE_IP/30`  |
| UDP Ping Scan          | `sudo nmap -PU53,161,162 -sn MACHINE_IP/30` |
| DNS SERVER             | `sudo nmap --dns-servers DNS_SERVER`        |

---

### 2. Port Scanning
- `-sT`: TCP Connect Scan – completes the three-way handshake.
- `-sS`: TCP SYN Scan – only the first step of the handshake (requires root).
- `-sU`: UDP Scan.
- `-F`: Fast mode – scans the 100 most common ports.
- `-p [range]`: Defines a range of ports (`-p-` scans all ports).
- `-Pn`: Treats all hosts as online, even those appearing offline.

#### 2.1 Overview of Nmap Port States

Nmap uses several states to describe the accessibility and behavior of a TCP or UDP port:

- **Open** — A service is actively listening on the port. Nmap receives a SYN/ACK in response to its SYN packet.
- **Closed** — No service is listening on the port, but the port is reachable. Nmap receives an RST in response.
- **Filtered** — Nmap cannot determine the port state because a firewall or security device blocks traffic or responses.
- **Unfiltered** — The port is reachable, but Nmap cannot determine whether it is open or closed. Seen in ACK scans (`-sA`).
- **Open|Filtered** — Nmap cannot determine whether the port is open or filtered, often in UDP, NULL, FIN, or Xmas scans.
- **Closed|Filtered** — Nmap cannot determine whether the port is closed or filtered; ambiguous firewall behavior.

#### 2.2 Port Scan types
| **Scan Type** | **Example Command** | **Description** |
|----------------|--------------------|-----------------|
| **TCP Null Scan** | `sudo nmap -sN 10.65.177.128` | Sends packets with no flags set. Closed ports respond with RST; open ports remain silent. |
| **TCP FIN Scan** | `sudo nmap -sF 10.65.177.128` | Sends packets with the FIN flag. Closed ports reply with RST; open ports ignore. |
| **TCP Xmas Scan** | `sudo nmap -sX 10.65.177.128` | Uses FIN, URG, and PSH flags. Detects open/closed ports like Null/FIN scans. |
| **TCP Maimon Scan** | `sudo nmap -sM 10.65.177.128` | Sends FIN/ACK packets; exploits uncommon TCP behavior for fingerprinting. |
| **TCP ACK Scan** | `sudo nmap -sA 10.65.177.128` | Determines whether ports are filtered/unfiltered (firewall detection). |
| **TCP Window Scan** | `sudo nmap -sW 10.65.177.128` | Similar to ACK scan, but uses TCP window size values to infer port states. |
| **Custom TCP Scan** | `sudo nmap --scanflags URGACKPSHRSTSYNFIN 10.65.177.128` | Sets custom TCP flags for advanced or evasive probing. |

#### 2.2 Evasion and Stealth Techniques
| **Technique** | **Example** | **Purpose** |
|----------------|-------------|-------------|
| **Spoofed Source IP** | `sudo nmap -S SPOOFED_IP 10.65.177.128` | Masks the origin IP. Requires routing control. |
| **Spoofed MAC Address** | `--spoof-mac SPOOFED_MAC` | Alters the hardware-level address for anonymity. |
| **Decoy Scan** | `nmap -D DECOY_IP,ME 10.65.177.128` | Blends traffic among multiple fake IPs to hide the true scanner. |
| **Idle (Zombie) Scan** | `sudo nmap -sI ZOMBIE_IP 10.65.177.128` | Uses a third-party host (zombie) to perform scans invisibly. |

#### 2.3 Packet Fragmentation and Manipulation

| **Option** | **Description** |
|-------------|----------------|
| `-f` | Fragments IP packets into 8-byte segments. Useful for IDS evasion. |
| `-ff` | Increases fragmentation to 16-byte segments. |
| `--source-port PORT_NUM` | Sets the source port (e.g., 53 to mimic DNS). |
| `--data-length NUM` | Appends random data to reach a specific packet size. |

---

### 3. Service and OS Detection
- `-O`: Detects the operating system.
- `-sV`: Detects service versions.
- `-A`: Enables OS detection, version detection, and advanced features.

---

### 4. Timing and Performance
- `-T<0-5>`: Timing templates from `paranoid (0)` to `insane (5)`.
- `--min-parallelism` / `--max-parallelism`: Controls the number of parallel probes.
- `--min-rate` / `--max-rate`: Sets packet send rate.
- `--host-timeout`: Limits how long to wait for a host.

---

### 5. Output and Reporting
- `-v`, `-vv`: Verbosity levels for more detailed output.
- `-d`, `-d9`: Debug levels for deeper troubleshooting.
- `-oN <filename>`: Normal output.
- `-oX <filename>`: XML output.
- `-oG <filename>`: Grepable output.
- `-oA <basename>`: Saves in all formats.

---

### 6. Useful

| Opción | Propósito                                             |
| ------ | ----------------------------------------------------- |
| `-n`   | Desactiva búsqueda DNS                                |
| `-R`   | Fuerza búsqueda reverse-DNS para todos los hosts      |
| `-sn`  | Solo descubrimiento de hosts (sin escaneo de puertos) |

---

### 7. Informational and Debugging Options

| **Option** | **Purpose** |
|-------------|-------------|
| `--reason` | Explains Nmap's conclusions about port states. |
| `-v`, `-vv` | Increases verbosity. |
| `-d`, `-dd` | Enables detailed debugging output. |
