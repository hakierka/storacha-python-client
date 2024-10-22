# storacha_client/storacha_client.py
import os
import requests
from .config import Config
from .utils import handle_api_errors

class StorachaClient:
    def __init__(self, x_auth_secret=None, authorization_token=None):
        # Initialize from environment variables if not provided explicitly
        self.headers = {
            'X-Auth-Secret': x_auth_secret or Config.X_AUTH_SECRET,
            'Authorization': authorization_token or Config.AUTHORIZATION_TOKEN,
        }
        self.base_url = 'https://up.storacha.network/bridge'

    def upload_file(self, cid, file_size, did):
        """Upload a file to Storacha using UCAN bridge."""
        data = {
            "tasks": [
                [
                    "store/add", 
                    did,  # User's DID
                    {"link": {"/": cid}, "size": file_size}
                ]
            ]
        }
        # Perform the API request
        response = requests.post(self.base_url, headers=self.headers, json=data)
        handle_api_errors(response)
        return response.json()

