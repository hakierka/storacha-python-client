import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from dotenv import load_dotenv
from storacha_client import StorachaClient

# Load environment variables from .env
load_dotenv()

# Fetch environment variables
X_AUTH_SECRET = os.getenv("X_AUTH_SECRET")
AUTHORIZATION_TOKEN = os.getenv("AUTHORIZATION_TOKEN")

# Check if environment variables are loaded correctly
if not X_AUTH_SECRET or not AUTHORIZATION_TOKEN:
    raise ValueError("Missing X_AUTH_SECRET or AUTHORIZATION_TOKEN")

# Initialize the Storacha Client
client = StorachaClient()

# Example CID and file size for testing
cid = "bafybeiapg57lfsxpz75qthv3tcys5i4zsnsy3lxgtzdykpvc74enl5jdjy"  # Replace with actual CID
file_size = 12345  # Replace with actual file size in bytes
did = "did:key:z6MkvP5JSRcjenRaiNQpb51uG88z8Mbj82HK8qGmHmEPZZnh"  # Replace with your DID

# Upload the file
try:
    response = client.upload_file(cid, file_size, did)
    print(f"Upload Response: {response}")
except Exception as e:
    print(f"Error occurred: {e}")
