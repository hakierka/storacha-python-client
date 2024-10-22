def handle_api_errors(response):
    """Handle any errors returned by the API."""
    if response.status_code != 200:
        raise Exception(f"API Request failed with status code {response.status_code}: {response.text}")
