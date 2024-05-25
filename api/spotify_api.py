from dotenv import load_dotenv
import os
import base64
from requests import post
import json

load_dotenv()

class SpotifyAuth:
    def __init__(self):
        self.client_id = os.getenv("CLIENT_ID")
        self.client_secret = os.getenv("CLIENT_SECRET")
        self.token_url = "https://accounts.spotify.com/api/token"
        self.token = None

    def get_token(self):
        auth_string = f"{self.client_id}:{self.client_secret}"
        auth_bytes = auth_string.encode("utf-8")
        auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

        headers = {
            "Authorization": "Basic " + auth_base64,
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {"grant_type": "client_credentials"}
        result = post(self.token_url, headers=headers, data=data)
        json_result = json.loads(result.content)
        self.token = json_result.get("access_token")
        return self.token

    def get_auth_header(self):
        if not self.token:
            self.get_token()
        return {"Authorization": "Bearer " + self.token}
