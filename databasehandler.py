import sqlite3
import os

# Enable check_same_thread=False to allow sharing the connection across threads
database = sqlite3.connect('database.sqlite', check_same_thread=False)
cursor = database.cursor()

def create_table():
    """
    Creates a table named 'users' in the database if it does not already exist.
    The 'users' table contains the following columns:
    - username: TEXT
    - password: TEXT
    - profilepic: TEXT
    This function commits the changes to the database after creating the table.
    """

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, profilepic TEXT)''')
    database.commit()

def insert_user(username, password):
    create_table()
    """
    Inserts a new user into the users table in the database.
    Args:
        username (str): The username of the new user.
        password (str): The password of the new user.
    Returns:
        None
    """
    cursor.execute('''INSERT INTO users (username, password) VALUES (?, ?)''', (username, password))
    database.commit()

def add_profilepic(username, profilepic):
    """
    Adds a profile picture to the user in the users table in the database.
    Args:
        username (str): The username of the user.
        profilepic (str): The profile picture of the user.
    Returns:
        None
    """
    cursor.execute('''UPDATE users SET profilepic = ? WHERE username = ?''', (profilepic, username))
    database.commit()

def fetch_user(username):
    """
    Fetches the details of a user from the users table in the database.
    Args:
        username (str): The username of the user.
    Returns:
        tuple: A tuple containing the username, password, and profilepic of the user.
    """
    cursor.execute('''SELECT * FROM users WHERE username = ?''', (username,))
    return cursor.fetchone()

def update_password(username, new_password):
    """
    Updates the password of a user in the users table in the database.
    Args:
        username (str): The username of the user.
        new_password (str): The new password of the user.
    Returns:
        None
    """
    cursor.execute('''UPDATE users SET password = ? WHERE username = ?''', (new_password, username))
    database.commit()

def delete_user(username):
    """
    Deletes a user from the users table in the database.
    Args:
        username (str): The username of the user.
    Returns:
        None
    """
    cursor.execute('''DELETE FROM users WHERE username = ?''', (username,))
    database.commit()

