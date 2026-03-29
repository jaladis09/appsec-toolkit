# AppSec Toolkit

Security tools built during my transition from
QA Automation Engineer to Application Security Engineer.

## Tools

### header_scanner.py
Checks a target URL for missing HTTP security headers.

Tests for:
- Strict-Transport-Security (HSTS)
- X-Frame-Options
- X-Content-Type-Options
- Content-Security-Policy
- Referrer-Policy
- Permissions-Policy

**Usage:**
python3 header_scanner.py https://example.com

**Example output:**
  [PASS]  Strict-Transport-Security
  [MISS]  Content-Security-Policy — Controls resource loading

### brute_force.py
Automated login brute force script for testing weak credentials.
Tests multiple username and password combinations against a target login page.
Built and tested against DVWA (Damn Vulnerable Web Application).

**Usage:**
python3 brute_force.py

**Example output:**
  [FOUND] Username: admin Password: password
  [MISS]  Username: admin Password: 123456

### CI/CD Security Pipeline
Automated Semgrep SAST scan triggered on every push to GitHub.
Scans all code for security vulnerabilities automatically.
Built with GitHub Actions — runs on every push to master branch.

### dvwa_security_report.md
Professional security assessment report from OWASP ZAP 
DAST scan against DVWA.
- 4 Medium findings
- Content Security Policy (CSP) Header Not Set
- Directory Browsing enabled
- HTTP Only Site — no HTTPS
- Missing Anti-Clickjacking Header
- 5 Low findings
- Cookie No HttpOnly Flag
- Cookie without SameSite Attribute
- In Page Banner Information Leak
- Server Leaks Version Information
- X-Content-Type-Options Header Missing
- Full remediation recommendations

#  Burp Suite web application testing

### Tools used
- Burp Suite Community Edition
- DVWA (Damn Vulnerable Web Application)

### What I practiced
- Setting up Burp Suite proxy using built-in browser
- Intercepting HTTP requests mid-flight
- Parameter tampering — modifying GET request credentials
- Using HTTP History to review all intercepted traffic
- Using Repeater to test multiple request variations

### Key findings
- DVWA Brute Force page sends credentials via GET request
- Username and password visible in plain text in URL
- No server-side validation — parameters can be modified mid-flight
- Credentials leak in browser history, server logs, and proxy logs



## OWASP Top 10 hands-on

### Vulnerabilities practiced on DVWA

### SQL Injection — OWASP A03
- Injected malicious SQL into User ID field
- Input: %' or '0'='0 returned all 5 user records
- Fix: Parameterised queries — never concatenate user input into SQL

### XSS Reflected — OWASP A03
- Injected <script>alert('XSS')</script> into name field
- Script executed in browser proving vulnerability
- Fix: Output encoding — html.escape() converts < > to safe characters

### XSS Stored — OWASP A03
- Injected script into guestbook message field
- Script saved in database — executes for every visitor
- More dangerous than Reflected — permanent and affects all users
- Fix: Sanitise input and encode output before storing

### Command Injection — OWASP A03
- Injected 127.0.0.1; whoami into ping field
- Server executed both commands — revealed www-data username
- Fix: Never concatenate user input into system commands
- Use subprocess list format in Python

### Key security principle
All three vulnerabilities share the same root cause —
untrusted user input passed directly into an interpreter.
Fix: Never trust user input — always validate server side.
Frontend validation provides zero security — 
can be bypassed using Burp Suite.

## Background
- 14 years QA Automation Engineering
- CISSP certified
- CC (Certified in Cybersecurity)
- Transitioning into Application Security

## Connect
https://www.linkedin.com/in/sandeepa-jaladi-b4250966/