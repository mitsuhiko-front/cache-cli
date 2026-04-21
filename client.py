
import requests

def fetch(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status()
    return response.text