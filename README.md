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



## Background
- 14 years QA Automation Engineering
- CISSP certified
- CC (Certified in Cybersecurity)
- Transitioning into Application Security

## Connect
https://www.linkedin.com/in/sandeepa-jaladi-b4250966/