import json
import requests

# The URL of the API endpoint
url = 'https://api.coincap.io/v2/assets/bitcoin/history?interval=d1'

# Sending a GET request to the URL
response = requests.get(url)

# Checking if the request was successful
if response.status_code == 200:
    # Parsing the JSON response
    r = response.json()
       # Define the filename where you want to store the data
    filename = 'bitcoin.json'
    
    # Write the JSON data to a file
    with open(filename, 'w') as f:
        json.dump(r, f)
    print(filename + ' created')
else:
    print(f"Failed to retrieve data: {response.status_code}")

x = []
y = []




for item in r['data']:
    x.append(item["priceUsd"]) 
    y.append(item["date"]) 

print(x)
print(y)
