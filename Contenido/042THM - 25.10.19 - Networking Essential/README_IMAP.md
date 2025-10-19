# IMAP

## 📘 Summary
This document serves as a personal technical note focused on the **Internet Message Access Protocol (IMAP)**, which enables synchronized email access across multiple devices. IMAP allows clients to read, organize, and manage emails stored on a mail server, maintaining consistent mailbox states between desktop, web, and mobile clients. It operates primarily on **TCP port 143** and uses **port 993** for secure communication via SSL/TLS.

---

## 🧠 Key Concepts

### IMAP Overview
- **IMAP (Internet Message Access Protocol)** enables real-time synchronization between email clients and servers.
- It allows users to access the same mailbox from multiple devices without removing messages from the server.
- Unlike POP3, IMAP keeps emails stored on the server, preserving message states (read, unread, flagged, deleted, etc.) across clients.

| Feature | IMAP | POP3 |
|----------|------|------|
| Default Port | 143 | 110 |
| Secure Port | 993 (IMAPS) | 995 (POP3S) |
| Synchronization | Yes | No |
| Message Storage | Server | Local |
| Multi-device Access | Full | Limited |
| Security | STARTTLS / SSL | SSL |

---

## 💻 Tools and Programs

### 🔹 Telnet
Used for manual interaction with IMAP servers to test and understand protocol behavior.

Example session:
```
$ telnet 10.10.41.192 143
* OK [CAPABILITY IMAP4rev1 SASL-IR LOGIN-REFERRALS ID ENABLE IDLE ...] Dovecot (Ubuntu) ready.
A LOGIN strategos password
A OK Logged in
B SELECT inbox
* FLAGS (\Answered \Flagged \Deleted \Seen \Draft)
* 4 EXISTS
B OK [READ-WRITE] Select completed
C FETCH 3 body[]
* 3 FETCH (BODY[] {445}
Return-path: <user@client.thm>
To: strategos@server.thm
Subject: Telnet email

Hello. I am using telnet to send you an email!
)
C OK Fetch completed
D LOGOUT
* BYE Logging out
D OK Logout completed
```
This demonstrates a complete IMAP session using `telnet` — from authentication to message retrieval and logout.

---

## ✉️ IMAP Command Summary

| Command | Description |
|----------|-------------|
| **LOGIN <user> <password>** | Authenticates the user with credentials. |
| **SELECT <mailbox>** | Chooses the mailbox (e.g., inbox) to access. |
| **FETCH <msg> <data>** | Retrieves the contents of a message. |
| **MOVE <seq> <mailbox>** | Moves specified messages to another mailbox. |
| **COPY <seq> <mailbox>** | Copies messages to a different mailbox. |
| **LOGOUT** | Ends the IMAP session cleanly. |

---

## 🔐 Security Considerations
- Standard IMAP sessions transmit data in plain text, including credentials.
- **IMAPS (port 993)** encrypts the connection using SSL/TLS, ensuring message and authentication confidentiality.
- **STARTTLS** can upgrade an unencrypted session to a secure one on port 143.

---

## 🧩 Notes for Future Reference
- IMAP provides **bidirectional synchronization** — actions performed on one device (read, delete, move) are reflected everywhere.
- **Telnet** remains one of the simplest ways to interact directly with IMAP servers for learning or troubleshooting.
- Familiarity with IMAP command flow helps diagnose issues like slow mailbox sync, authentication errors, or missing folders.

