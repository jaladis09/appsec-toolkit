# AppSec Toolkit

> QA Automation Engineer (14 years) → Application Security Engineer
> CISSP | CC (Certified in Cybersecurity)

A hands-on security engineering portfolio built over 90 days.
Every tool, report, and pipeline here was built from scratch —
not tutorials, not copy-paste. Real tools, real targets, real findings.

---

## What I built

| Asset | Type | Description |
|-------|------|-------------|
| `header_scanner.py` | Passive recon tool | Checks 6 HTTP security headers |
| `brute_force.py` | Attack simulation | Automated credential testing vs DVWA |
| `crapi_brute_force.py` | API attack simulation | Broken auth testing vs crAPI |
| `zap_to_splunk.py` | SIEM integration | Ships ZAP findings into Splunk |
| `security.yml` | CI/CD pipeline | Semgrep SAST on every push |
| `dvwa_security_report.md` | DAST report | 4 Medium, 5 Low findings from ZAP |
| `crapi_security_report.md` | API security report | BOLA, BFLA, Broken Auth findings |
| `dvwa-login-threat-model.json` | Threat model | STRIDE — 6 threats on DVWA login flow |
| `ai-qa-project/` | AI Engineering | Claude API pipeline — AI-powered test case generation and comparison vs Jira/Rovo |

---

## SIEM Pipeline — Splunk Integration

Built a full security operations pipeline from scratch:

```
Attack tools run against targets
        ↓
Logs ship to Splunk via HTTP Event Collector (HEC)
        ↓
SPL queries correlate events across all tools
        ↓
Threshold alert fires on brute force detection
        ↓
Unified dashboard — full attack surface in one view
```

**Detection rule built:**
Brute force alert triggers when more than 5 failed logins
occur within a 60 second window — High severity.

**Data sources feeding Splunk:**
- `appsec_brute_force` — DVWA web login attacks
- `appsec_api_brute_force` — crAPI API attacks
- `appsec_zap_findings` — OWASP ZAP DAST findings

---

## Tools & Findings

### header_scanner.py
Passive recon tool that checks a target URL for missing HTTP security headers.

Tests for:
- Strict-Transport-Security (HSTS)
- X-Frame-Options
- X-Content-Type-Options
- Content-Security-Policy
- Referrer-Policy
- Permissions-Policy

```bash
python3 header_scanner.py https://example.com

[PASS]  Strict-Transport-Security
[MISS]  Content-Security-Policy — Controls resource loading
```

---

### brute_force.py
Automated credential brute force script with real-time Splunk logging.
Built and tested against DVWA at security level Low.

```bash
python3 brute_force.py

[FOUND] Username: admin Password: password
[MISS]  Username: admin Password: 123456
```

Every attempt ships to Splunk as a structured JSON event in real time.

---

### crapi_brute_force.py
API authentication brute force script targeting crAPI's identity service.
Confirms absence of rate limiting — a real-world OWASP API Security Top 10 finding.

```bash
python3 crapi_brute_force.py

[FOUND] Password: Test@1234 — Status: 200
[MISS]  Password: wrongpassword — Status: 401
```

**Finding:** crAPI allows unlimited authentication attempts with no lockout
or rate limiting — confirming Broken Authentication (OWASP API3).

---

### DVWA Security Assessment — ZAP DAST
Full DAST scan using OWASP ZAP against DVWA.

| # | Finding | Risk |
|---|---------|------|
| 1 | CSP Header Not Set | Medium |
| 2 | Directory Browsing | Medium |
| 3 | HTTP Only Site | Medium |
| 4 | Missing Anti-Clickjacking Header | Medium |
| 5 | Cookie No HttpOnly Flag | Low |
| 6 | Cookie without SameSite Attribute | Low |
| 7 | In Page Banner Information Leak | Low |
| 8 | Server Leaks Version Information | Low |
| 9 | X-Content-Type-Options Missing | Low |

Full report with remediation recommendations: `dvwa_security_report.md`

---

### crAPI Security Assessment
Manual API security testing against crAPI (Completely Ridiculous API).

| Finding | OWASP API Category |
|---------|--------------------|
| BOLA — Access other users' vehicle data | API1 — Broken Object Level Auth |
| BFLA — Access admin functions as user | API5 — Broken Function Level Auth |
| Broken Auth — No rate limiting on login | API2 — Broken Authentication |

Full report: `crapi_security_report.md`

---

### Threat Model — STRIDE
STRIDE threat model on DVWA login flow. 6 threats identified across:
- Spoofing — credential brute force
- Tampering — parameter manipulation via Burp Suite
- Repudiation — no audit logging
- Information Disclosure — credentials in GET parameters
- Denial of Service — no account lockout
- Elevation of Privilege — SQL injection to bypass auth

---

### OWASP Top 10 — Hands-on Practice

All practiced on DVWA:

**SQL Injection (A03)**
Input `%' or '0'='0` returned all 5 user records.
Fix: Parameterised queries.

**XSS Reflected (A03)**
Injected `<script>alert('XSS')</script>` — executed in browser.
Fix: Output encoding via `html.escape()`.

**XSS Stored (A03)**
Script injected into guestbook — executes for every visitor permanently.
Fix: Sanitise input and encode output before storing.

**Command Injection (A03)**
Input `127.0.0.1; whoami` — server returned `www-data`.
Fix: Never concatenate user input into system commands.

**Key principle:** All four vulnerabilities share the same root cause —
untrusted user input passed directly into an interpreter.
Frontend validation provides zero security — bypassed in seconds with Burp Suite.

---

### Burp Suite Practice
- Intercepting HTTP requests mid-flight
- Parameter tampering on DVWA brute force page
- Credentials visible in plain text in GET parameters
- Repeater for testing multiple request variations

**Finding:** DVWA sends credentials via GET request —
username and password leak into browser history, server logs, and proxy logs.

---

### CI/CD Security Pipeline
Semgrep SAST runs automatically on every push to master via GitHub Actions.
Pipeline defined in `.github/workflows/security.yml`.

---

## Stack

| Tool | Purpose |
|------|---------|
| Python 3.12 | Tool development |
| OWASP ZAP | DAST scanning |
| Burp Suite Community | Manual web testing |
| Semgrep | SAST / CI pipeline |
| Splunk Enterprise | SIEM / log analysis |
| DVWA | Web app target |
| crAPI | API security target |
| Docker | Lab environment |
| GitHub Actions | CI/CD |

---## Secure Code Review

### Tools used
- Bandit 1.9.4 — Python security scanner
- Manual code review

### What I practiced
- Manual secure code review — finding vulnerabilities by reading code
- Running Bandit against Python code
- Added Bandit to CI/CD pipeline alongside Semgrep
- Severity based pipeline — fail on High/Critical, report Medium/Low

### Vulnerabilities found in vulnerable_code.py
| # | Vulnerability | Severity | CWE | Fix |
|---|---|---|---|---|
| 1 | Hardcoded credentials | Critical | CWE-259 | Environment variables |
| 2 | SQL Injection — login() | Critical | CWE-89 | Parameterised queries |
| 3 | SQL Injection — get_user_data() | Critical | CWE-89 | Parameterised queries |
| 4 | Weak MD5 hashing | High | CWE-327 | bcrypt or Argon2 |
| 5 | Command Injection — os.system() | High | CWE-78 | subprocess shell=False |

### Key lessons
- Manual review finds logic flaws tools miss
- Tools find known patterns automatically
- Manual + automated together = best coverage
- Frontend validation provides zero security
- Always validate server side
- Pipeline should fail on Critical/High — not block on Medium/Low

##  — JWT and OAuth Security

### What I learned
- JWT structure — Header, Payload, Signature
- JWT is base64 encoded NOT encrypted
- Access token vs Refresh token
- JWT vulnerabilities — Algorithm None, weak secret, long expiry
- OAuth flow and security vulnerabilities
- State parameter prevents CSRF in OAuth

### JWT Analysis — crAPI
Decoded real JWT from crAPI using jwt.io

**Algorithm:** RS256 — asymmetric — more secure than HS256

**Payload:**
- sub: sandeepa@test.com
- role: user
- iat: issued at
- exp: expires after 7 days

**Findings:**
| # | Finding | Risk |
|---|---|---|
| 1 | JWT expires in 7 days — too long | Medium |
| 2 | MFA not enforced — mfaRequired: false | High |
| 3 | Role stored in payload | Low |

### JWT Vulnerabilities
| Attack | Description | Fix |
|---|---|---|
| Algorithm None | Server accepts unsigned tokens | Never accept alg:none |
| Weak secret | HS256 with weak key — forgeable | Use strong 256-bit secret |
| Long expiry | Stolen token works too long | Access token 15-60 mins |
| Sensitive data | Payload visible to anyone | Never store sensitive data in JWT |
| Algorithm confusion | RS256 to HS256 downgrade | Lock algorithm server side |

### OAuth Security
- Never expose tokens in URLs — leak to logs and history
- Always include state parameter — prevents CSRF
- Minimum scope — request only permissions needed
- Authorization code must be single use and short lived

## Background
- 14 years QA Automation Engineering
- CISSP certified
- CC (Certified in Cybersecurity)
- Actively transitioning into Application Security Engineering

## Connect
[LinkedIn — Sandeepa Jaladi](https://www.linkedin.com/in/sandeepa-jaladi-b4250966/)
