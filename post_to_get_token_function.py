import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning



def get_token():
	requests.packages.urllib3.disable_warnings()
	url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"

	payload={}
	headers = {
  			'Content-Type': 'application/json',
  			#'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
			}
	auth_rize = ("devnetuser", "Cisco123!")	
	response = requests.request("POST", url, headers=headers, data=payload, auth=auth_rize, verify=False)
	#print(response.text)
	#Printing Key-value "Token" as shown on API docs for dna center
	token = response.json()["Token"]
	#This returns the token to be used
	return token




#print(get_token())

