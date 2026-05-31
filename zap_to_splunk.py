import requests
from datetime import datetime

# --- Splunk HEC config ---
SPLUNK_URL = "https://localhost:8088/services/collector/event"
SPLUNK_TOKEN = "06558f03-251e-43ed-b7b4-44699e9e10fb"

def send_to_splunk(finding):
    event = {
        "event": {
            "tool": "zap_dast",
            "target": "http://localhost",
            "finding": finding["name"],
            "risk": finding["risk"],
            "description": finding["description"],
            "recommendation": finding["recommendation"],
            "scan_date": "2026-03-01",
            "timestamp": datetime.utcnow().isoformat()
        },
        "sourcetype": "appsec_zap_findings",
        "index": "main"
    }
    try:
        requests.post(
            SPLUNK_URL,
            headers={"Authorization": f"Splunk {SPLUNK_TOKEN}"},
            json=event,
            verify=False
        )
        print(f"[SENT] {finding['risk']:6} — {finding['name']}")
    except Exception as e:
        print(f"[SPLUNK ERROR] {e}")

findings = [
    {"name": "CSP Header Not Set", "risk": "Medium", "description": "Application does not implement Content Security Policy header leaving it vulnerable to XSS attacks.", "recommendation": "Implement strict Content-Security-Policy header restricting script sources to trusted domains."},
    {"name": "Directory Browsing", "risk": "Medium", "description": "Web server exposes directory listings revealing sensitive files and server structure.", "recommendation": "Set Options -Indexes in Apache configuration."},
    {"name": "HTTP Only Site", "risk": "Medium", "description": "Application transmits data over unencrypted HTTP exposing credentials and session cookies to interception.", "recommendation": "Implement HTTPS with valid SSL certificate and add Strict-Transport-Security header."},
    {"name": "Missing Anti-Clickjacking Header", "risk": "Medium", "description": "Missing X-Frame-Options header leaves users vulnerable to clickjacking attacks.", "recommendation": "Add X-Frame-Options: SAMEORIGIN to all responses."},
    {"name": "Cookie No HttpOnly Flag", "risk": "Low", "description": "Session cookie missing HttpOnly flag allows JavaScript to read cookie value enabling theft via XSS.", "recommendation": "Set HttpOnly flag on all session cookies."},
    {"name": "Cookie without SameSite Attribute", "risk": "Low", "description": "Missing SameSite attribute leaves cookies vulnerable to CSRF attacks.", "recommendation": "Set SameSite=Strict on all session cookies."},
    {"name": "In Page Banner Information Leak", "risk": "Low", "description": "Server reveals software versions in page content assisting attackers in identifying vulnerabilities.", "recommendation": "Configure Apache to suppress version information."},
    {"name": "Server Leaks Version Information", "risk": "Low", "description": "Server HTTP header reveals Apache version and operating system details.", "recommendation": "Set ServerTokens Prod in Apache configuration."},
    {"name": "X-Content-Type-Options Missing", "risk": "Low", "description": "Missing header allows browser MIME sniffing enabling execution of malicious files.", "recommendation": "Add X-Content-Type-Options: nosniff header."}
]

print(f"\nShipping {len(findings)} ZAP findings to Splunk...\n")
for finding in findings:
    send_to_splunk(finding)
print(f"\nDone — {len(findings)} findings sent.")