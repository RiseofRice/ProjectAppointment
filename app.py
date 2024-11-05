from flask import Flask, request, render_template
import requests
from hashlib import sha256
import databasemanager
import os

app = Flask(__name__)

@app.route('/')
def home() -> str:
    """
Route for the home page.

Returns:
    str: A greeting message 'Hello World'.
"""
    return render_template("home.html")

@app.route('/registerpage')
def registerpage() -> str:
    """
    Handles the registration process.
    Returns:
        str: A confirmation message indicating the registration status.
    """
    return render_template("registerpage.html")

@app.route('/register', methods=['POST'])
def register() -> str:
    """
    Handles the registration process.
    Returns:
        str: A confirmation message indicating the registration status.
    """
    username = request.form['username']
    password = request.form['password']
    print(username)
    print(password)
    databasemanager.insert_user(username, sha256(password.encode()).hexdigest())

    return f'Registered {username} {sha256(password.encode()).hexdigest()}'

    

@app.route('/login')
def login() -> str:
    return 'Login'

if __name__ == '__main__':
    if not os.path.exists('database.sqlite'):
        with open('database.db', 'w', encoding='utf-8') as f:
            databasemanager.create_table()
    app.run(host="0.0.0.0", port=8080, debug=True)
