from storacha_client.storacha_client import StorachaClient

client = StorachaClient()

# Example CID and file size
cid = 'bafybeiapg57lfsxpz75qthv3tcys5i4zsnsy3lxgtzdykpvc74enl5jdjy'  # Replace with your own CID
file_size = 12345  # Replace with actual file size
did = 'did:key:z6MkvP5JSRcjenRaiNQpb51uG88z8Mbj82HK8qGmHmEPZZnh'  # Replace with your DID

# Upload the file
response = client.upload_file(cid, file_size, did)
print(f"Upload Response: {response}")
