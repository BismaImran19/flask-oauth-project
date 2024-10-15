from flask import Flask, redirect, request, session, url_for
import requests
from config import Config

app = Flask(__name__)
app.secret_key = 'random_secret_key'

# Route to redirect the user to GitHub's OAuth page
@app.route('/')
def home():
    return '<a href="/login">Login with GitHub</a>'

# Step 1: Redirect user to GitHub OAuth page
@app.route('/login')
def login():
    github_auth_url = Config.AUTHORIZE_URL
    client_id = Config.CLIENT_ID
    redirect_uri = Config.REDIRECT_URI
    return redirect(f'{github_auth_url}?client_id={client_id}&redirect_uri={redirect_uri}')

# Step 2: GitHub redirects back to this route with a code
@app.route('/callback')
def callback():
    code = request.args.get('code')
    if code:
        token = exchange_code_for_token(code)
        if token:
            user_info = get_user_info(token)
            return f"Hello, {user_info['login']}! You have logged in successfully."
    return "Login failed!"

# Step 3: Exchange code for an access token
def exchange_code_for_token(code):
    token_url = Config.TOKEN_URL
    client_id = Config.CLIENT_ID
    client_secret = Config.CLIENT_SECRET
    redirect_uri = Config.REDIRECT_URI
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'code': code,
        'redirect_uri': redirect_uri
    }
    headers = {'Accept': 'application/json'}
    response = requests.post(token_url, data=data, headers=headers)
    token_data = response.json()
    return token_data.get('access_token')

# Step 4: Fetch user info using the access token
def get_user_info(token):
    headers = {'Authorization': f'token {token}'}
    response = requests.get(Config.USER_API_URL, headers=headers)
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)
