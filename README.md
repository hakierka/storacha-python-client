# Storacha Python Client

A Python client for interacting with Storacha decentralized storage. This client allows users to easily integrate Storacha into their Python applications and perform operations such as file uploads using UCAN delegation.

## Features
- Upload files to Storacha using CIDs from IPFS.
- Environment-based configuration for security and flexibility.

## Installation

1. Install the client using pip:
    > pip install git+https://github.com/hakierka/storacha-python-client.git
2. Set up environment variables in a .env file:
    > X_AUTH_SECRET=your-base64-encoded-secret
    > 
    > AUTHORIZATION_TOKEN=your-base64-encoded-token
3. Use the client in your Python code:
    > from storacha_client.storacha_client import StorachaClient
    > 
    > client = StorachaClient()
    > 
    > response = client.upload_file('your-ipfs-cid', 12345, 'your-did')
    > 
    > print(response)
