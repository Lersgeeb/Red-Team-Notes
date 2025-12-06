 Meterpreter Commands Overview

## Summary
This document summarizes essential information about **Meterpreter**, the advanced payload used in the **Metasploit Framework** for post-exploitation activities. It provides a structured overview of the main command categories, their purposes, and how they are typically used. These notes serve as a personal reference for learning and practice in ethical hacking and penetration testing environments.

## Command Categories

### 1. Core Commands
These commands control the Meterpreter session itself and manage interactions.
```
background   - Backgrounds the current session
exit         - Terminates the current session
guid         - Displays the session's unique identifier
help         - Displays available commands
load         - Loads additional Meterpreter extensions
migrate      - Moves Meterpreter to another process
run          - Executes a Meterpreter script or module
sessions     - Switches between active sessions
```

### 2. File System Commands
Used to explore, read, or modify files on the target system.
```
cd           - Change directory
ls / dir     - List directory contents
pwd          - Print working directory
cat          - Display file contents
edit         - Edit a file on the target
rm           - Delete a file
search       - Search for files
upload       - Upload files to the target
download     - Download files from the target
```

### 3. Networking Commands
Manage network interfaces and view active connections.
```
arp          - View the ARP table
ifconfig     - Display network interfaces
netstat      - Show current network connections
portfwd      - Forward local ports to remote services
route        - Manage the routing table
```

### 4. System Commands
Gather system information and manage processes.
```
clearev      - Clear event logs
execute      - Execute a program or command
getpid       - Show current process ID
getuid       - Show current user
kill / pkill - Terminate processes
ps           - List running processes
reboot       - Reboot the remote system
shutdown     - Shut down the system
shell        - Open a command shell
sysinfo      - Display system information
```

### 5. Other Functional Commands
Advanced features for privilege escalation and surveillance.
```
idletime         - Show how long the user has been idle
keyscan_start    - Start capturing keystrokes
keyscan_dump     - Dump captured keystrokes
keyscan_stop     - Stop keylogging
screenshare      - View the target's desktop in real time
screenshot       - Take a screenshot of the desktop
record_mic       - Record audio from the microphone
webcam_list      - List available webcams
webcam_snap      - Take a snapshot
webcam_stream    - Stream live video
getsystem        - Attempt privilege escalation
hashdump         - Dump password hashes from the SAM database
```