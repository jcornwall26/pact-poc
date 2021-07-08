import requests

def repositories():
    """Fetch a user object by user_name from the server."""
    uri = 'http://localhost:1234/v1/repositories/'
    return requests.get(uri).json()