import requests
import os
from dotenv.main import load_dotenv

load_dotenv()

URL = 'https://www.googleapis.com/customsearch/v1'

query = "dogs"

PARAMS = {
    'key': os.environ['SEARCH_API_KEY'],
    'cx':os.environ['ENGINE_ID'],
    'q': query
}

response = requests.get(url = URL, params = PARAMS)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Failed to get data: {response.status_code}")