# SQL Injection - Time and Boolean Based
This README collects concise, high-value notes about common SQL injection techniques you asked about: **Boolean-based (blind)**, **Time-based (blind)**

---

# Overview — What is Boolean-based (Blind) SQLi?
Boolean-based blind SQL Injection is a technique where you infer data from a database by observing **differences in application behavior or responses** caused by injected boolean conditions. The application does **not** directly return database values or SQL errors; instead it responds differently depending on whether an injected condition evaluates to **TRUE** or **FALSE**. By iteratively asking yes/no questions (often character-by-character), an attacker can reconstruct sensitive values.

### Key characteristics
- **No direct data in response:** the app does not show query results or stack traces.
- **Binary observations:** you rely on changes in page content, presence/absence of elements, response length, HTTP status, or redirection.
- **Slow but reliable:** extraction usually requires many requests and is slower than in-band techniques.
- **Works when other techniques fail:** especially useful against sanitized outputs but where the DB still evaluates injected logic.

---

## Signals / Indicators to detect Boolean-based blind SQLi
- Response differs when you inject a tautology (`' OR 1=1 --`) vs a contradiction (`' OR 1=2 --`) and the application shows different page content (e.g., login success vs failure).
- Variation in response **length** or **HTML structure** between conditionally true and false payloads.
- Conditional **redirects** or **presence/absence** of certain page elements (e.g., "Welcome" banner appears only when query returns rows).
- No visible SQL errors or data leakage, but consistent differences persist across repeated requests.

---

## Typical workflow / methodology (safe, lab-focused)
1. **Baseline**: capture the normal request/response for a parameter (e.g., `username` field).  
2. **Test trivial boolean**: inject a payload that should always be true vs always false and observe differences.  
   - Example conceptual payloads:
     - TRUE test: `' OR '1'='1'-- `
     - FALSE test: `' OR '1'='2'-- `
3. **Confirm blind behavior**: if you see a reliable difference, proceed to enumerate.
4. **Enumerate step-by-step**:
   - Decide the target datum (database name, table, column, password hash).
   - Extract length first (e.g., check `LENGTH()` or `CHAR_LENGTH()` via boolean checks).
   - Extract characters one-by-one, using either simple range checks or binary search to speed up.
5. **Optimize**:
   - Use **binary search** on ASCII values for each character to reduce number of requests (log₂(256) ≈ 8 checks/char).
   - Cache or parallelize non-dependent checks only if allowed/ethical and within scope.

---

## Common boolean payload patterns (conceptual — for labs)
> These are *examples* intended to show structure. Do not use them against systems without explicit permission.

- Check database name starts with 's':
  ```
  ' OR (SELECT DATABASE()) LIKE 's%'-- 
  ```
- Check length of admin password equals 32:
  ```
  ' OR (SELECT LENGTH(password) FROM users WHERE username='admin') = 32 -- 
  ```
- Compare ASCII value of nth character:
  ```
  ' OR ASCII(SUBSTRING((SELECT password FROM users WHERE username='admin'), 1, 1)) > 109 -- 
  ```
- Binary search template (ASCII):
  ```
  ' OR ASCII(SUBSTRING((SELECT col FROM tbl WHERE id=1), pos, 1)) > X -- 
  ```

**Note:** Use `SUBSTRING`/`MID`/`SUBSTR`/`SUBSTRING_INDEX` variants depending on DBMS. Functions and syntax vary per engine.

---

## Practical enumeration strategy (character-by-character)
1. Find length `L`:
   - Iterate `i = 1..N` and test `(LENGTH(field) > i)` until FALSE to discover L.
2. For each position `p` in `1..L`:
   - Use binary search over ASCII range (32–126 printable) to find the character:
     - Test if `ASCII(SUBSTRING(field, p, 1)) > mid`
     - Narrow range until exact ASCII value found.
3. Assemble characters to reconstruct the value.

**Optimization tips:**
- Limit charset to `0-9`, `a-z`, `A-Z`, punctuation if you know expected format.
- Use `CASE`/`IF` conditional expressions where available to create simpler boolean checks.
- Reduce noise by avoiding extremely common pages or noisy endpoints; practice politeness and scope limits.

---

## DBMS differences and function mappings
- **MySQL**
  - length: `LENGTH()` or `CHAR_LENGTH()`
  - substring: `SUBSTRING(col, pos, len)`
  - ascii: `ASCII()`
- **PostgreSQL**
  - length: `LENGTH()` or `CHAR_LENGTH()`
  - substring: `SUBSTRING(col FROM pos FOR len)`
  - ascii: `ASCII(SUBSTRING(...))`
- **SQL Server**
  - length: `LEN()`
  - substring: `SUBSTRING(col, pos, len)`
  - ascii: `ASCII()`

Always confirm syntax in your lab DBMS.

---

## Detection and logging (defensive)
- Monitor for repeated requests differing only in small payloads to the same parameter (pattern of enumeration).
- Alert on high-request-rate sequences from same client to sensitive endpoints.
- Log and inspect parameters for suspicious boolean logic (`OR`, `AND`, comparison operators, `SUBSTRING`, `ASCII`, `LENGTH`).
- Correlate authentication attempts with unusual conditional payloads.

---

## Mitigations & secure coding practices
- **Prepared statements / parameterized queries** — never concatenate user input into SQL.
- **Strong input validation** — whitelist valid characters and lengths for each parameter.
- **Least privilege** — DB account used by web app should have minimal permissions.
- **Output handling** — avoid leaking conditional differences in UI; standardize responses when feasible.
- **Rate limiting and WAF rules** — detect and block enumeration patterns.
- **Remove verbose SQL errors** — so attackers have fewer signals.

---

# Overview — What is Time-based (Blind) SQLi?
Time-based blind SQL Injection is a variant of blind SQLi where the attacker infers boolean outcomes by **measuring how long the database takes to respond**. The payload includes a database-native delay function (`SLEEP()`, `pg_sleep()`, `WAITFOR`) that executes **only when a condition is true**. Observing a measurable delay (compared to baseline) indicates the condition evaluated to TRUE. This method is useful when the application does not reveal content differences but the database will execute time delays.

### Key characteristics
- **No visible data or SQL errors** — relies solely on timing.
- **Requires DB delay functions** — availability depends on DBMS and permissions.
- **Sensitive to network jitter** — requires multiple measurements and statistical confidence.
- **Stealthy but noisy** — increases request latency significantly which can trigger detection.

---

## DBMS-specific delay primitives
- **MySQL:** `SLEEP(seconds)`
- **PostgreSQL:** `pg_sleep(seconds)`
- **SQL Server:** `WAITFOR DELAY 'hh:mm:ss'` or `WAITFOR DELAY '00:00:05'`
- **SQLite:** no native sleep — requires user-defined functions or external extensions.

---

## Typical payload structure (conceptual)
- Inject a conditional that calls `SLEEP()` when true:
  - MySQL example:
    ```
    ' OR IF((SELECT ASCII(SUBSTRING(password,1,1)) > 109), SLEEP(5), 0) -- 
    ```
  - PostgreSQL example:
    ```
    ' OR CASE WHEN (SELECT ASCII(SUBSTRING(password FROM 1 FOR 1)) > 109) THEN pg_sleep(5) ELSE NULL END --
    ```
- Simpler `UNION`-style sleep to probe column counts (lab):
  ```
  ' UNION SELECT SLEEP(5), NULL -- 
  ```

**Important:** The delay only happens if the injected expression is syntactically valid and executed by the DB engine. Mismatched columns/types or blocking security controls can prevent execution.

---

## Example lab-safe checks (conceptual)
- Determine whether first character ASCII > 109 in MySQL:
  ```
  ' OR IF(ASCII(SUBSTRING((SELECT password FROM users WHERE username='admin'),1,1)) > 109, SLEEP(5), 0) -- 
  ```
- Determine password length > 16:
  ```
  ' OR IF((SELECT LENGTH(password) FROM users WHERE username='admin') > 16, SLEEP(5), 0) -- 
  ```

---

## Detection, logging and defense
- **Monitor latency patterns** per parameter: a sequence of requests that systematically add sleep on differing payloads is suspicious.
- **Rate-limit and anomaly detection:** block IPs that issue many slow-detection style queries within short window.
- **Egress and DB function controls:** restrict or disable dangerous functions (where possible) for DB users used by web apps.
- **Prepared statements & input validation:** same core mitigations as other injection classes.
- **WAF fingerprinting:** many WAFs can detect obvious `SLEEP()` patterns — but do not rely solely on WAF.

---