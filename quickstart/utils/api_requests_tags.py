import requests

# GET request
r = requests.get('https://aceship.github.io/AN-EN-Tags/json/tl-type.json')
response = r.json()
d = dict()

# Get tags name and put into new dictionary
new_data = {
    "name": "Survival",
}

# The API endpoint to communicate with
url_post = "http://127.0.0.1:8000/tags/"

# A POST request to the API
post_response = requests.post(url_post, json=new_data)

# Print the response
post_response_json = post_response.json()
print(post_response_json)
