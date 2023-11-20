import requests

# Define new data to create
new_data = {
    "name": "Survival",
}

# The API endpoint to communicate with
url_post = "http://127.0.0.1:8000/tags/"

# A POST request to tthe API
post_response = requests.post(url_post, json=new_data)

# Print the response
post_response_json = post_response.json()
print(post_response_json)
