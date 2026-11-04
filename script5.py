# Save remote tf state to the file.
import os
import json
import requests
file = 'terraform.tfstate'
response = requests.get('https://terraform.cloud.com/api/v1/states/{id}', auth=('', ''), verify=False)
trans = response.json()
fo = open(file, 'w')
json.dump(trans,fo,indent=4)
fo.close()