import sqlite3
import os

DATABASE_FILE = 'users.db'

def initialize_db():
    if not os.path.exists(DATABASE_FILE):
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                profile_image BLOB
            )
        ''')
        conn.commit()
        conn.close()

def add_user(username, password, profile_image_path=None):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    with open(profile_image_path, 'rb') as file:
        profile_image = file.read() if profile_image_path else None
    cursor.execute('''
        INSERT INTO users (username, password, profile_image)
        VALUES (?, ?, ?)
    ''', (username, password, profile_image))
    conn.commit()
    conn.close()

def get_user(username):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, username, profile_image FROM users WHERE username = ?
    ''', (username,))
    user = cursor.fetchone()
    conn.close()
    return user

def update_user(username, password=None, profile_image_path=None):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    if password:
        cursor.execute('''
            UPDATE users SET password = ? WHERE username = ?
        ''', (password, username))
    if profile_image_path:
        with open(profile_image_path, 'rb') as file:
            profile_image = file.read()
        cursor.execute('''
            UPDATE users SET profile_image = ? WHERE username = ?
        ''', (profile_image, username))
    conn.commit()
    conn.close()

def delete_user(username):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM users WHERE username = ?
    ''', (username,))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    initialize_db()