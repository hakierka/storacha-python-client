import os
import requests

class StorachaClient:
    def __init__(self, x_auth_secret=None, authorization_token=None):
        # Initialize headers with the passed tokens or environment variables
        self.headers = {
            'X-Auth-Secret': x_auth_secret or os.getenv("X_AUTH_SECRET"),
            'Authorization': f'Bearer {authorization_token or os.getenv("AUTHORIZATION_TOKEN")}'
        }
        
        if not self.headers['X-Auth-Secret'] or not self.headers['Authorization']:
            raise ValueError("X-Auth-Secret or Authorization token missing.")
        
        self.base_url = 'https://up.storacha.network/bridge'
        
        # Print headers for debugging purposes
        print("X_AUTH_SECRET:", self.headers['X-Auth-Secret'])
        print("Authorization:", self.headers['Authorization'])

    def upload_file(self, cid, file_size, did):
        # Define the payload
        data = {
            "tasks": [
                [
                    "store/add", 
                    did,  # User's DID
                    {"link": {"/": cid}, "size": file_size}
                ]
            ]
        }

        # Send the request
        response = requests.post(self.base_url, headers=self.headers, json=data)

        # Check for errors
        if response.status_code != 200:
            raise Exception(f"API Request failed with status code {response.status_code}: {response.text}")

        return response.json()
