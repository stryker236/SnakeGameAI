import requests

# Define the URL of your local server
url = 'http://localhost:5000/api'  # Replace with your server endpoint

# Define the data you want to send in the POST request (in JSON format)
data = {
    'key1': 'value1',
    'key2': 'value2'
}

# Make the POST request
response = requests.post(url, json=data)

# Check the response
if response.status_code == 200:
    print('Request was successful.')
    print('Response data:', response.json())
else:
    print('Request failed with status code:', response.status_code)
