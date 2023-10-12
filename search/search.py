import requests
import os
from dotenv.main import load_dotenv

load_dotenv()

URL = 'https://www.googleapis.com/customsearch/v1'

query = input("Enter Google search query: ")

PARAMS = {
    'key': os.environ['SEARCH_API_KEY'],
    'cx':os.environ['ENGINE_ID'],
    'q': query
}

response = requests.get(url = URL, params = PARAMS)

if response.status_code == 200:

    resp_json = response.json()

    if 'items' in resp_json:
        # Extract the URLs
        urls = [item.get('link', 'No URL found') for item in resp_json['items']]

        print("Search results for '" + query + "'")
        for url in urls:
            print(url)
    else:
        print("No items found in the API response.")
else:
    print(f"Failed to get data: {response.status_code}")