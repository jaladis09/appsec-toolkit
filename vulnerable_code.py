import os
import sqlite3
import hashlib

SECRET_KEY = "mypassword123"
DB_PASSWORD = "admin@1234"

def login(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    user = cursor.fetchone()
    
    if user:
        hashed = hashlib.md5(password.encode()).hexdigest()
        if hashed == user[2]:
            return True
    return False

def run_command(cmd):
    os.system(cmd)

def get_user_data(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = " + user_id
    cursor.execute(query)
    return cursor.fetchall()