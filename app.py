from flask import Flask

app = Flask(__name__)

@app.route('/')
def home() -> str:
    """
Route for the home page.

Returns:
    str: A greeting message 'Hello World'.
"""
    return 'Hello World'

@app.route('/register')
def register() -> str:
    """
    Handles the registration process.
    Returns:
        str: A confirmation message indicating the registration status.
    """

    return 'Register'

@app.route('/login')
def login() -> str:
    return 'Login'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
