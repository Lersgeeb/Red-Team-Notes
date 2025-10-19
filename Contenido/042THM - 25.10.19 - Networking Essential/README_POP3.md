# POP3

## 📘 Summary
This note covers the **Post Office Protocol version 3 (POP3)** — a protocol designed to allow email clients to retrieve messages from a mail server. It complements SMTP (used for sending emails) by providing the mechanism for receiving and managing email messages locally. The document highlights command-line interactions and packet-level analysis captured through **tshark/Wireshark**.

---

## 🧠 Key Concepts

### POP3 Overview
- **POP3 (Post Office Protocol v3)** is used by email clients to **download emails** from a remote mail server.
- Operates on **TCP port 110** by default.
- Communication is **plain-text**, meaning commands and credentials can be easily intercepted without encryption (unless POP3S over port 995 is used).
- POP3 works like retrieving letters from your personal mailbox, whereas SMTP resembles sending mail at the post office.

### SMTP vs POP3 Analogy
| Function | Protocol | Analogy |
|-----------|-----------|----------|
| Sending emails | **SMTP** | Delivering a letter at the post office |
| Receiving emails | **POP3** | Checking your mailbox for new letters |

---

## 💻 Tools and Commands

### 🔹 tshark
Used to capture and analyze the POP3 traffic over TCP.
Example capture sequence:
```
1. Client → Server: TCP SYN
2. Server → Client: TCP SYN, ACK
3. Client → Server: TCP ACK
4. Server → Client: POP3 +OK Banner (Dovecot)
5. Client → Server: AUTH / USER / PASS / STAT / LIST / RETR / DELE / QUIT
```
From packet 4 onward, the communication is clearly identified as POP3.

### 🔹 telnet
Allows for manual POP3 session simulation. Example:
```
$ telnet 10.201.52.114 110
+OK [XCLIENT] Dovecot (Ubuntu) ready.
USER strategos
+OK
PASS mypassword
+OK Logged in.
STAT
+OK 3 1264
LIST
+OK 3 messages:
1 407
2 412
3 445
RETR 3
+OK 445 octets
QUIT
+OK Logging out.
```
This manual interaction shows each stage of POP3 communication, identical to what a mail client automates.

---

## ✉️ POP3 Command Summary

| Command | Description |
|----------|-------------|
| **USER <username>** | Identifies the user to the server. |
| **PASS <password>** | Provides the user password. |
| **STAT** | Requests total number and size of messages. |
| **LIST** | Lists messages with their respective sizes. |
| **RETR <msg_number>** | Retrieves the content of the selected message. |
| **DELE <msg_number>** | Marks a message for deletion. |
| **QUIT** | Ends the POP3 session, applying deletions. |

---

## 📊 Common POP3 Response Codes

| Response | Meaning |
|-----------|----------|
| **+OK** | Positive acknowledgment; operation successful. |
| **-ERR** | Error in command or operation. |

These are used consistently throughout POP3 interactions to indicate success or failure.

---

## 🧩 Notes on Security
- **POP3 transmits data in plaintext**, meaning credentials (USER/PASS) are visible to anyone capturing network traffic.
- To secure POP3, use **POP3S** (POP3 over SSL/TLS) on port **995**.
- Tools like **Wireshark** can easily expose unencrypted credentials in a network capture.

---

## 🔍 Example: Packet Capture Behavior
A sample `tshark` capture shows how each POP3 command and response corresponds to packets exchanged between the client (10.21.16.214) and server (10.201.52.114):

```
4  0.486893479  Server → Client POP 91 S: +OK Dovecot ready
10 68.234068154 Client → Server POP 64 C: USER linda
14 95.450371207 Client → Server POP 66 C: PASS Pa$$123
16 95.760185323 Server → Client POP 68 S: +OK Logged in
18 107.651781961 Client → Server POP 58 C: STAT
22 120.955415924 Client → Server POP 58 C: LIST
27 153.892269605 Client → Server POP 60 C: RETR 1
45 222.718121870 Client → Server POP 60 C: DELE 4
53 232.389941083 Client → Server POP 58 C: QUIT
```

Each **C:** denotes a client command, and **S:** a server response. The sequential dialogue mirrors a complete POP3 retrieval and logout session.

