import base64

def load_delegation_token(filepath):
    """Load the binary delegation token and base64 encode it."""
    with open(filepath, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

def validate_response(response):
    """Check the HTTP response status and raise exceptions for errors."""
    if not response.ok:
        raise Exception(f"Request failed with status code {response.status_code}: {response.text}")
