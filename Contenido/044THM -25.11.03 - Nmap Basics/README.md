# Nmap Basics

## Overview
This document summarizes key concepts and commands learned during the Nmap exploration session. It serves as a personal learning note for future reference.

---

## Key Topics

### 1. Host Discovery
- `-sL`: List scan – lists targets without scanning.
- `-sn`: Ping scan – performs host discovery only.

### 2. Port Scanning
- `-sT`: TCP Connect Scan – completes the three-way handshake.
- `-sS`: TCP SYN Scan – only the first step of the handshake (requires root).
- `-sU`: UDP Scan.
- `-F`: Fast mode – scans the 100 most common ports.
- `-p [range]`: Defines a range of ports (`-p-` scans all ports).
- `-Pn`: Treats all hosts as online, even those appearing offline.

### 3. Service and OS Detection
- `-O`: Detects the operating system.
- `-sV`: Detects service versions.
- `-A`: Enables OS detection, version detection, and advanced features.

### 4. Timing and Performance
- `-T<0-5>`: Timing templates from `paranoid (0)` to `insane (5)`.
- `--min-parallelism` / `--max-parallelism`: Controls the number of parallel probes.
- `--min-rate` / `--max-rate`: Sets packet send rate.
- `--host-timeout`: Limits how long to wait for a host.

### 5. Output and Reporting
- `-v`, `-vv`: Verbosity levels for more detailed output.
- `-d`, `-d9`: Debug levels for deeper troubleshooting.
- `-oN <filename>`: Normal output.
- `-oX <filename>`: XML output.
- `-oG <filename>`: Grepable output.
- `-oA <basename>`: Saves in all formats.


### 6. Initial Recon
| Tipo de escaneo        | Comando de ejemplo                          |
| ---------------------- | ------------------------------------------- |
| ARP Scan               | `sudo nmap -PR -sn MACHINE_IP/24`           |
| ICMP Echo Scan         | `sudo nmap -PE -sn MACHINE_IP/24`           |
| ICMP Timestamp Scan    | `sudo nmap -PP -sn MACHINE_IP/24`           |
| ICMP Address Mask Scan | `sudo nmap -PM -sn MACHINE_IP/24`           |
| TCP SYN Ping Scan      | `sudo nmap -PS22,80,443 -sn MACHINE_IP/30`  |
| TCP ACK Ping Scan      | `sudo nmap -PA22,80,443 -sn MACHINE_IP/30`  |
| UDP Ping Scan          | `sudo nmap -PU53,161,162 -sn MACHINE_IP/30` |

| Opción | Propósito                                             |
| ------ | ----------------------------------------------------- |
| `-n`   | Desactiva búsqueda DNS                                |
| `-R`   | Fuerza búsqueda reverse-DNS para todos los hosts      |
| `-sn`  | Solo descubrimiento de hosts (sin escaneo de puertos) |

---