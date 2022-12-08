#!/usr/bin/env python

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json
import sys
def get_token():
	"""
	Gets an access token from Cisco DNA Center. Returns the token
	string if successful: False otherwise.
	"""
	requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
	# Declare useful local variables to simplify request process
	api_path = "https://sandboxdnac.cisco.com/dna"
	auth = ("devnetuser", "Cisco123!")
	headers = {"Content-Type": "application/json"}

	#Issue HTTP POST request to the proper URL to request a token
	#r = requests.post(post_uri, auth=(username, password), verify=False)
       # return r.json()["Token"]
	auth_resp = requests.post(
		f"{api_path}/system/api/v1/auth/token", auth=auth, headers=headers, verify = False
	)

	# If successful, print token. Else, raise HTTPError with details
	auth_resp.raise_for_status()
	token = auth_resp.json() ["Token"]
	return token


def main ():
	"""
	Execution begins here.
	"""

	token = get_token()
	print(token)

if __name__=="__main__":
	main()
