
# Command Injection & XSS Security Notes

Reference:https://github.com/payloadbox/command-injection-payload-list

## What is Command Injection?
OS command injection (a.k.a. shell injection) is a vulnerability where an application constructs and executes system-level commands using unsanitized user input. If the input directly reaches a shell or command interpreter, an attacker can append or replace operations to execute arbitrary commands on the host operating system.

## Payload categories (high level)
- **Simple separators / chaining**: `;`, `&&`, `||`, `|` — append additional commands.  
- **Substitution & expansion**: backticks `` `cmd` ``, `$(cmd)` — execute and substitute output.  
- **Redirections & background**: `> /tmp/out`, `2>&1`, `&` — capture output, spawn background jobs.  
- **Pipes / filters**: `|`, `xargs`, `tee` — chain output into other commands.  
- **Blind injection**: commands that cause time delay or side-effects (e.g., `sleep 5`, `ping -c 5 127.0.0.1`) for blind scenarios.  
- **Encoding / double-encoding**: URL-encoded or percent-encoded payloads to bypass filters (e.g., `%3B`, `%60`).  
- **Shellshock / environment attacks**: specially crafted headers or environment variables that exploit vulnerable `bash` versions.  
- **Platform-specific payloads**: Windows (cmd.exe / PowerShell) vs Unix shells (sh, bash).  
- **File-based payloads**: use `echo '...' > /tmp/payload.sh && sh /tmp/payload.sh` to persist stagers.  

## Illustrative examples
- Unix chaining: `8.8.8.8; id` → runs `id` after `ping`.  
- Command substitution: `$(whoami)` → injects output of `whoami`.  
- Blind timing: `sleep 5` or `ping -c 5 127.0.0.1` to observe response delays.  
- Windows: `& whoami` or `| dir C:\` appended to vulnerable parameters.
