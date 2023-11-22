import requests
from name_converter import NameConvert

# The API endpoint to communicate with
url_post = "http://127.0.0.1:8000/operators/"

# Make a GET request
r = requests.get('https://aceship.github.io/AN-EN-Tags/json/gamedata/en_US/gamedata/excel/character_table.json')
r.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

# Decode JSON content
response = r.json()

for key, value in response.items():
    # Define new data to create
    new_data = {
        "class_name": NameConvert(value["profession"]),
        "tags": list(map(NameConvert, value['tagList'])),
        "name": value['name'],
        "rarity": value['rarity']+1
    }
    
    # A POST request to tthe API
    post_response = requests.post(url_post, json=new_data)

    # Print the response
    post_response_json = post_response.json()
    print(post_response_json)
