# SMTP

## 📘 Summary
This document serves as a personal technical note about the **Simple Mail Transfer Protocol (SMTP)** and its observation through **tshark/Wireshark** network analysis. It provides a summary of the packet flow, key SMTP commands, and relevant command-line tools used for protocol inspection.

---

## 🧠 Key Concepts

### SMTP Overview
- **SMTP (Simple Mail Transfer Protocol)** is the standard protocol for sending email messages across the Internet.
- Operates over **TCP port 25** by default.
- Involves plain-text communication between **clients** and **mail servers**.
- Typical use cases:
  - Client → Mail Server communication.
  - Mail Server → Mail Server relay.

### Network Flow Example
An SMTP session begins after a TCP three-way handshake. Using `tshark`, the packet flow can be visualized as follows:

```
1. Client → Server: TCP SYN
2. Server → Client: TCP SYN, ACK
3. Client → Server: TCP ACK
4. Server → Client: SMTP 220 Banner
5. Client → Server: TCP ACK
```

From packet #4 onward, the SMTP communication starts, where actual commands and email data are exchanged.

---

## 💻 Tools and Commands

### 🔹 tshark
`tshark` is the command-line version of Wireshark used for network capture and protocol analysis.

Example output snippet:
```
4 0.453624470 10.201.52.114 → 10.21.16.214 SMTP 142 S: 220 ip-10-201-52-114.ec2.internal ESMTP Exim 4.95 Ubuntu
```
This represents the server's **220 greeting** message, confirming that it is ready for SMTP communication.

### 🔹 telnet
`telnet` can be used to manually interact with an SMTP server, demonstrating each command exchange.

Example:
```
$ telnet 10.201.52.114 25
HELO client.thm
MAIL FROM:<user@client.thm>
RCPT TO:<recipient@server.thm>
DATA
From: user@client.thm
To: recipient@server.thm
Subject: Test

This is a test email.
.
QUIT
```
This sequence replicates the same communication your email client performs automatically.

---

## ✉️ SMTP Command Summary

| Command | Description |
|----------|-------------|
| **HELO / EHLO** | Initiates an SMTP session and identifies the client. |
| **MAIL FROM:** | Declares the sender’s address. |
| **RCPT TO:** | Specifies the recipient’s address. |
| **DATA** | Indicates the start of the message body. |
| **.** | Marks the end of message content. |
| **QUIT** | Ends the SMTP session cleanly. |

---

## 📊 Common SMTP Response Codes

| Code | Meaning |
|------|----------|
| **220** | Service ready / Server banner |
| **250** | OK, action completed successfully |
| **354** | Start mail input, awaiting data |
| **421** | Service not available |
| **550** | Mailbox unavailable or rejected |
| **221** | Closing transmission channel |

