import os
from dotenv import load_dotenv
from storacha_client import StorachaClient

# Load environment variables from .env
load_dotenv()

# Fetch environment variables
X_AUTH_SECRET = os.getenv("X_AUTH_SECRET")
AUTHORIZATION_TOKEN = os.getenv("AUTHORIZATION_TOKEN")

# Check that the environment variables are loaded
if not X_AUTH_SECRET or not AUTHORIZATION_TOKEN:
    raise ValueError("Missing X_AUTH_SECRET or AUTHORIZATION_TOKEN")

# Initialize StorachaClient
client = StorachaClient(x_auth_secret=X_AUTH_SECRET, authorization_token=AUTHORIZATION_TOKEN)

# Print headers for debugging purposes
print("Headers:", client.headers)

# Example CID and file size for testing
cid = "bafybeiapg57lfsxpz75qthv3tcys5i4zsnsy3lxgtzdykpvc74enl5jdjy"  # Replace with actual IPFS CID
file_size = 12288  # Replace with the actual file size
did = "did:key:your-did"  # Replace with your DID

try:
    # Attempt to upload the file
    response = client.upload_file(cid, file_size, did)
    print(f"Upload successful: {response}")
except Exception as e:
    print(f"Error occurred: {e}")
