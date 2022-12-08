import requests
import json
import sys

url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"

payload={}
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'X-Auth-Token': "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MGVjNGU0ZjRjYTdmOTIyMmM4MmRhNjYiLCJhdXRoU291cmNlIjoiaW5$"
}

response01 = requests.request("GET", url, headers=headers, data=payload, verify=False)
print ("All devices count: ",json.dumps(response01.json()["response"], indent=4))

#print(response.text)
