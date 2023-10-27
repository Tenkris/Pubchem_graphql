# import requests

# # Replace with the actual AID of the bioassay you are interested in
# aid = '214920'
# # add try catch  on fetch data

# # Fetch the assay data from PubChem
# response = requests.get(f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/{aid}/json")

# # Check if the request was successful
# if response.status_code == 200:
#     assay_data = response.json() 
#     print(assay_data)
#     # Navigate through the JSON response to find the active compounds
#     # The exact path may vary depending on the assay data structure
#     for result in assay_data.get('PC_AssayResults', []):
#         if result.get('activity_outcome') == 'Active':
#             print("Active Compound ID:", result.get('sid'))
# else:
#     print(f"Failed to retrieve assay results: {response.status_code}")



import requests
import json

# Define the Assay ID and the URL
aid = int(input("Enter the AID: "))

# url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/{aid}/JSON"

# # Make a GET request to the URL
# response = requests.get(url)

# if response.status_code == 200:
#     # Parse the JSON response
#     assay_data = response.json()
    
#     # Print the entire JSON response
#     print(json.dumps(assay_data, indent=5))
# else:
#     print(f"Failed to retrieve assay results: {response.status_code}")

import requests

# Define the Assay ID and the URL

url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/{aid}/JSON"

# Make a GET request to the URL
response = requests.get(url)

if response.status_code == 200:
    # Parse the JSON response
    assay_data = response.json()
    # print(assay_data)
    # Navigate through the JSON response to extract the relevant data
    # Adjust the keys and paths to match the actual structure of the returned data
    #print(json.dumps(assay_data, indent=4))
    # Iterate over the results and print the Substance ID and Activity Outcome
    #get all key of assay_data
    #print(assay_data['PC_AssaySubmit'])
    print("______________________________ch____________________________")
    print(json.dumps(assay_data['PC_AssaySubmit']['data'] , indent=4))
        
else:
    print(f"Failed to retrieve assay results: {response.status_code}")
