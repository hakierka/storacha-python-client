import os
import requests
from src.config import Config
from src.utils import load_delegation_token, validate_response

class StorachaClient:
    def __init__(self):
        Config.validate()
        self.headers = {
            'X-Auth-Secret': Config.X_AUTH_SECRET,
            'Authorization': Config.AUTHORIZATION_TOKEN
        }
        self.upload_url = Config.UPLOAD_URL

    def upload_file(self, file_path, cid, file_size):
        """Upload a file using UCAN bridge."""
        data = {
            "tasks": [
                [
                    "store/add",
                    "did:key:your-did",
                    {"link": {"/": cid}, "size": file_size}
                ]
            ]
        }
        
        # Step 1: Make the initial POST request
        response = requests.post(self.upload_url, headers=self.headers, json=data)
        validate_response(response)
        
        upload_info = response.json()
        upload_url = upload_info[0]['p']['out']['ok']['url']
        status = upload_info[0]['p']['out']['ok']['status']

        # Step 2: If status is 'upload', upload the file using PUT request
        if status == 'upload':
            with open(file_path, 'rb') as file_data:
                put_response = requests.put(upload_url, headers=self.headers, data=file_data)
                validate_response(put_response)
            print("File uploaded successfully!")
        else:
            raise Exception("Upload status not set to 'upload'")

# Usage Example
if __name__ == "__main__":
    client = StorachaClient()
    file_path = "path/to/hen.jpeg"
    cid = "bafybeiapg57lfsxpz75qthv3tcys5i4zsnsy3lxgtzdykpvc74enl5jdjy"  # Replace with the CID from IPFS
    file_size = 13312  # Replace with the actual file size of hen.jpeg in bytes
    client.upload_file(file_path, cid, file_size)
