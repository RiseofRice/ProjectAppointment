from flask import Flask, request, render_template

import requests
from hashlib import sha256
import databasehandler
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
    databasehandler.insert_user(username, sha256(password.encode()).hexdigest())

    return f'Registered {username} {sha256(password.encode()).hexdigest()}'

    

@app.route('/login', methods=['POST'])
def login():
    username = request.form["username"]
    password = request.form["password"]
    print(username)
    print(password)
    user_details = databasehandler.fetch_user(username)
    if user_details:
        print(user_details[1])
        print(sha256(password.encode()).hexdigest())
        if user_details[1] == sha256(password.encode()).hexdigest():
            return render_template("dashboard.html")
        else:
            return 'Incorrect password'
    else:
        return 'User does not exist'
if __name__ == '__main__':
    if not os.path.exists('database.sqlite'):
        with open('database.db', 'w', encoding='utf-8') as f:
            databasehandler.create_table()
    app.run(host="0.0.0.0", port=5000, debug=True)
