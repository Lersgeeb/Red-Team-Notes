# Primitive Network & System Scanner Notes

## Tools & How They Fit Together

- **traceroute / tracert**
  - Purpose: Map path (hops) from source to destination.
  - Usage:
    - Linux/macOS: `traceroute MACHINE_IP`
    - Windows: `tracert MACHINE_IP`

- **ping**
  - Purpose: Check if the target responds to ICMP Echo and measure latency.
  - Usage:
    - Linux/macOS: `ping -c 10 MACHINE_IP`
    - Windows: `ping -n 10 MACHINE_IP`

- **telnet**
  - Purpose: Test TCP reachability by attempting a connection to a specific port.
  - Usage:
    - `telnet MACHINE_IP PORT_NUMBER`
  - Note: telnet only attempts to open a connection; it is useful for quick manual checks.

- **netcat (nc)**
  - Purpose: Flexible TCP/UDP client and server for manual port checks and simple listeners.
  - Usage as client:
    - `nc MACHINE_IP PORT_NUMBER`
  - Usage as server (listener):
    - `nc -lvnp PORT_NUMBER`

## Notes & Learning Points
- This primitive scanner is **not a replacement for nmap**; it lacks many features (OS detection, service/version detection, advanced timing and evasion options).
- Useful for quick, ad-hoc checks when nmap is unavailable or when you want minimal footprint.
- Telnet is dated but handy for basic TCP connect tests; `nc` (netcat) is more flexible and script-friendly.

# Commands Quick Reference

| Purpose | Tool | Example |
|---------|------|---------|
| ICMP reachability | ping | `ping -c 10 MACHINE_IP` (Linux/macOS) |
| ICMP reachability | ping | `ping -n 10 MACHINE_IP` (Windows) |
| Path mapping | traceroute | `traceroute MACHINE_IP` (Linux/macOS) |
| Path mapping | tracert | `tracert MACHINE_IP` (Windows) |
| TCP connect test | telnet | `telnet MACHINE_IP PORT_NUMBER` |
| TCP client | netcat | `nc MACHINE_IP PORT_NUMBER` |
| TCP server | netcat | `nc -lvnp PORT_NUMBER` |
