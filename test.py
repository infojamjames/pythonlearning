import json
import requests

# The URL of the API endpoint
url = 'https://api.coincap.io/v2/assets'

# Sending a GET request to the URL
response = requests.get(url)

# Checking if the request was successful
if response.status_code == 200:
    # Parsing the JSON response
    data = response.json()
       # Define the filename where you want to store the data
    filename = 'assets.json'
    
    # Write the JSON data to a file
    with open(filename, 'w') as f:
        json.dump(data, f)

    print(filename + ' created')
else:
    print(f"Failed to retrieve data: {response.status_code}")
