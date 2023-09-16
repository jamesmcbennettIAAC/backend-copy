import requests
import json

# Define your input parameters
input_data = {
    "lineType": "Polygon",
    "corridor": 1,  # Replace with your corridor value
    "levels": 2,    # Replace with your levels value
    "x": [-43.786476, 79.604578, 40.422679, -76.240781],  # Replace with your x points as a list
    "y": [36.292871, 45.09543, -46.102012, -37.299453]   # Replace with your y points as a list
}

# Define the endpoint for your Rhino.Compute server
compute_endpoint = "http://localhost:8081/"

# Define the path to your GH file (instead of .ghx)
gh_path = "FloorPlanGenerator_Combined.gh"

# Create a payload for the Rhino.Compute request
payload = {
    "algorithmDefinition": {
        "Definition": gh_path,
        "Inputs": input_data
    }
}

# Send the request to Rhino.Compute
response = requests.post(f"{compute_endpoint}/grasshopper", json=payload)

# Check if the request was successful
if response.status_code == 200:
    result = response.json()
    output_string = result["Outputs"]["output"]
    print("Output String:", output_string)
else:
    print("Error:", response.status_code, response.text)