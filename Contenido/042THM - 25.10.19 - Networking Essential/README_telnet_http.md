# Telnet Notes and Practical Commands

## Summary

This document provides a concise overview of using **Telnet** for interacting with web servers and troubleshooting HTTP connections.

## Key Concepts

- **HTTP and TCP Ports**:  
  - `HTTP` typically uses **port 80**.  
  - `HTTPS` uses **port 443** (Telnet cannot handle HTTPS encryption).  
- **Manual HTTP Communication**:  
  Telnet enables sending raw HTTP requests directly to the server, which is useful for:
  - Testing server responses.
  - Inspecting HTTP headers.
  - Debugging web server configurations.


## Basic Telnet Commands

### 1. Connect to a Web Server on Port 80

```bash
telnet $WEB_SEVER_IP 80
```

If the connection is successful, Telnet will display a message such as:
```
Trying $WEB_SEVER_IP...
Connected to $WEB_SEVER_IP.
```

### 2. Send an HTTP GET Request

After connecting, type the following manually (press Enter after each line, and twice at the end to send the blank line):

```bash
GET / HTTP/1.1
Host: anything
```

The server will respond with raw HTTP headers and the HTML content of the path