# Storacha Python Client

This Python client allows developers to easily upload files to Storacha using CIDs from IPFS. The client integrates with Storacha's UCAN bridge and automates the upload process.

## Features
- Upload files to Storacha via UCAN bridge.
- Uses **IPFS CIDs** to reference files.
- Integrates easily into any Python project.

## Requirements
- **Python 3.x**
- **pip** (Python package manager)

## Installation

1. Clone this repository or download the source files.
2. Install the required Python packages by running:

   ```
   pip install requests python-dotenv

3. Create a .env file in the project root and provide the following:

    ```
    X_AUTH_SECRET=your-base64-encoded-secret
    AUTHORIZATION_TOKEN=your-base64-encoded-delegation-token

Replace your-base64-encoded-secret and your-base64-encoded-delegation-token with actual values provided by Storacha or generated via UCAN delegation.

## Usage
1. Ensure your file is already uploaded to IPFS and that you have its CID (Content Identifier).

2. Open storacha_client.py and replace the CID and file size with the correct values for your file:

   ```
   cid = 'your-ipfs-cid'  # Replace with actual CID
   file_size = 12345  # Replace with actual file size in bytes

3. Run the script:

    ```
    python3 storacha_client.py

4. The client will upload the file to Storacha and print the upload status and the URL.


## Example
    ```
    python3 storacha_client.py

Expected output if the upload is successful:

    ```
    Storacha UCAN bridge status: upload
    Upload URL: https://your-upload-url.com

