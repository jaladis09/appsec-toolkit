# DVWA Security Assessment Report

## Executive Summary
A security assessment was conducted against DVWA 
(Damn Vulnerable Web Application) running locally 
on localhost. The assessment identified 9 findings — 
4 Medium and 5 Low risk.

## Scope
- Target: http://localhost
- Tool: OWASP ZAP automated scan
- Date: March 2026

## Findings Summary
| # | Finding | Risk |
| 1 | CSP Header Not Set | Medium |
| 2 | Directory Browsing | Medium |
| 3 | HTTP Only Site | Medium |
| 4 | Missing Anti-Clickjacking Header | Medium |
| 5 | Cookie No HttpOnly Flag | Low |
| 6 | Cookie without SameSite Attribute | Low |
| 7 | In Page Banner Information Leak | Low |
| 8 | Server Leaks Version Information | Low |
| 9 | X-Content-Type-Options Missing | Low |

## Detailed Findings

### Finding 1 — CSP Header Not Set
- Risk: Medium
- Description: Application does not implement Content 
Security Policy header leaving it vulnerable to XSS attacks.
- Recommendation: Implement strict Content-Security-Policy 
header restricting script sources to trusted domains.

### Finding 2 — Directory Browsing
- Risk: Medium
- Description: Web server exposes directory listings 
revealing sensitive files and server structure.
- Recommendation: Set Options -Indexes in Apache configuration.

### Finding 3 — HTTP Only Site
- Risk: Medium  
- Description: Application transmits data over unencrypted 
HTTP exposing credentials and session cookies to interception.
- Recommendation: Implement HTTPS with valid SSL certificate 
and add Strict-Transport-Security header.

### Finding 4 — Missing Anti-Clickjacking Header
- Risk: Medium
- Description: Missing X-Frame-Options header leaves users 
vulnerable to clickjacking attacks.
- Recommendation: Add X-Frame-Options: SAMEORIGIN to all responses.

### Finding 5 — Cookie No HttpOnly Flag
- Risk: Low
- Description: Session cookie missing HttpOnly flag allows 
JavaScript to read cookie value enabling theft via XSS.
- Recommendation: Set HttpOnly flag on all session cookies.

### Finding 6 — Cookie without SameSite Attribute
- Risk: Low
- Description: Missing SameSite attribute leaves cookies 
vulnerable to CSRF attacks.
- Recommendation: Set SameSite=Strict on all session cookies.

### Finding 7 — In Page Banner Information Leak
- Risk: Low
- Description: Server reveals software versions in page 
content assisting attackers in identifying vulnerabilities.
- Recommendation: Configure Apache to suppress version information.

### Finding 8 — Server Leaks Version Information
- Risk: Low
- Description: Server HTTP header reveals Apache version 
and operating system details.
- Recommendation: Set ServerTokens Prod in Apache configuration.

### Finding 9 — X-Content-Type-Options Missing
- Risk: Low
- Description: Missing header allows browser MIME sniffing 
enabling execution of malicious files.
- Recommendation: Add X-Content-Type-Options: nosniff header.

## Conclusion
The assessment identified 4 Medium and 5 Low risk findings. 
Medium findings should be remediated immediately. Low findings 
should be scheduled for remediation in the next development cycle.

## Assessed By
- Name: Sandeepa Jaladi
- Date: March 2026
- Tools: OWASP ZAP, Custom header_scanner.py