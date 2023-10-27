import requests

# Replace with the actual Substance ID
sid = input("Substance ID:").strip()

url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/sid/{sid}/cids/JSON"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    cids = data.get('InformationList', {}).get('Information', [{}])[0].get('CID', [])
    print(f"Substance ID: {sid}, Compound IDs: {cids}")
else:
    print(f"Failed to retrieve compound IDs for substance ID {sid}: {response.status_code}")
