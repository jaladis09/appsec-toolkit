# crAPI Security Assessment Report

# crAPI Security Assessment Report

## Executive Summary
A security assessment was conducted against crAPI 
(Completely Ridiculous API) running locally on localhost. 
The assessment identified 3 findings — 1 Critical, 2 High 
— using Burp Suite manual API security testing and custom 
Python scripts.

## Scope
- Target: http://localhost:8888
- Tools: Burp Suite Community Edition, Python scripts
- Testing type: Manual API security testing
- Date: May 2026

## Findings Summary
| # | Finding | Risk | Endpoint |
|---|---|---|---|
| 1 | Broken Object Level Authorization (BOLA) | Critical | /identity/api/v2/vehicle/{uuid}/location |
| 2 | Broken Function Level Authorization (BFLA) | High | /workshop/api/mechanic/ |
| 3 | Broken Authentication — No rate limiting | High | /identity/api/auth/login |

## Detailed Findings

### Finding 1 — BOLA (API1)
- Risk: Critical
- Endpoint: GET /identity/api/v2/vehicle/{uuid}/location
- Description: Authenticated users can access any 
vehicle's location and owner details by changing 
the vehicle UUID in the request. No server-side 
authorization check verifies the requesting user 
owns the vehicle.
- Steps to reproduce:
  1. Log in as regular user
  2. Get your vehicle UUID from dashboard
  3. Find another user's UUID from community forum
  4. Replace your UUID with theirs in the request
  5. Full location and personal details returned
- Impact: Full exposure of all users location data
and personal information including name and email
- Recommendation: Implement server-side authorization 
check — verify authenticated user owns the requested 
vehicle UUID before returning data

### Finding 2 — BFLA (API5)
- Risk: High
- Endpoint: GET /workshop/api/mechanic/
- Description: Regular authenticated user can access 
mechanic management endpoint returning all mechanic 
details including email addresses. This is an admin 
function that should not be accessible to regular users.
- Steps to reproduce:
  1. Log in as regular user
  2. Send GET request to /workshop/api/mechanic/
  3. Full list of all mechanics returned including emails
- Impact: Exposure of all mechanic personal information
- Recommendation: Implement Role Based Access Control.
Only admin or mechanic role should access this endpoint.

### Finding 3 — Broken Authentication (API2)
- Risk: High
- Endpoint: POST /identity/api/auth/login
- Description: API has no rate limiting or account 
lockout. Automated password testing using 
crapi_brute_force.py successfully found valid 
credentials after 8 attempts with no blocking.
- Steps to reproduce:
  1. Send multiple POST requests to login endpoint
  2. Try different passwords automatically
  3. No lockout or rate limiting triggered
  4. Valid credentials discovered — Test@1234
- Impact: Attacker can automate unlimited login 
attempts and crack user credentials
- Recommendation: Implement rate limiting — max 5 
attempts per minute, account lockout after 5 failed 
attempts, CAPTCHA, and MFA

## OWASP API Security Top 10 Coverage
| Category | Tested | Finding |
|---|---|---|
| API1 — BOLA | ✅ | Critical finding confirmed |
| API2 — Broken Authentication | ✅ | High finding confirmed |
| API5 — Broken Function Level Authorization | ✅ | High finding confirmed |
|
## Tools Used
- Burp Suite Community Edition — manual API testing
- Burp Suite HTTP History — request analysis
- Burp Suite Repeater — request manipulation
- crapi_brute_force.py — automated authentication testing

## Assessed By
- Name: Sandeepa Jaladi
- Date: May 2026
