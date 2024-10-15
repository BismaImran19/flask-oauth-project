import os

class Config:

    CLIENT_ID = os.getenv('GITHUB_CLIENT_ID', 'Ov23liGefw9BZtqCcx8X')  # Correct way
    CLIENT_SECRET = os.getenv('GITHUB_CLIENT_SECRET', '26b6e5ff162b53a73bc796371259a352da3eb5d3')  # Correct way
    AUTHORIZE_URL = "https://github.com/login/oauth/authorize"
    TOKEN_URL = "https://github.com/login/oauth/access_token"
    USER_API_URL = "https://api.github.com/user"
    REDIRECT_URI = "http://localhost:5000/callback"
