import requests
import json

# Define your input parameters
input_data = {
    "a": 5,  # Replace with your first number
    "b": 7   # Replace with your second number
}

# Define the endpoint for your Rhino.Compute server
compute_endpoint = "http://localhost:8081/"

# Define the path to your GHX file
ghx_path = "test2.gh"

# Create a payload for the Rhino.Compute request
payload = {
    "algorithmDefinition": {
        "Definition": ghx_path,
        "Inputs": input_data
    }
}

# Send the request to Rhino.Compute
response = requests.post(f"{compute_endpoint}/grasshopper", json=payload)

# Check if the request was successful
if response.status_code == 200:
    result = response.json()
    output_string = result["Outputs"]["result"]
    print("Sum:", output_string)
else:
    print("Error:", response.status_code, response.text)