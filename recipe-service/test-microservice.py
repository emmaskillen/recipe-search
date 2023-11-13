import requests

# Define the URL of your microservice endpoint
microservice_url = "http://localhost:8003"

# Define your variable
search_param = '{"cuisine":"italian"}'

# Create a dictionary of parameters (variables) to include in the request
params = {"param": search_param}

# Make a GET request with parameters
response = requests.get(microservice_url, params=params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    print("Received data:", data)
else:
    # Print an error message if the request was not successful
    print(f"Error: {response.status_code} - {response.text}")


