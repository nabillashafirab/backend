import requests

# The API endpoint to communicate with
url_post = "http://127.0.0.1:8000/classes/"

try:
    # Make a GET request
    r = requests.get('https://aceship.github.io/AN-EN-Tags/json/tl-type.json')
    r.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
    
    # Decode JSON content
    response = r.json()

    # Post data
    for i in response:
        new_data = {
            "name": i["type_en"]
        }
        
        # A POST request to the API
        post_response = requests.post(url_post, json=new_data)
        
        # Print the response from the POST request
        post_response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        post_response_json = post_response.json()
        print(post_response_json)

except requests.exceptions.HTTPError as errh:
    print("HTTP Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print("Something went wrong:", err)
except requests.exceptions.JSONDecodeError as json_err:
    print("JSON Decode Error:", json_err)
    print("Response content:", r.text)  # Print the actual content for further inspection


