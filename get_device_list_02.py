import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from post_to_get_token_function import get_token

def my_main():
    requests.packages.urllib3.disable_warnings()
    token = get_token()

    url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"

    payload={}
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'X-Auth-Token': token
            }

    #response01 = requests.request("GET", url, headers=headers, data=payload, verify=False)
    my_resp= requests.get(url, headers=headers,verify=False)
    
    #print ("All devices count: ",json.dumps(my_resp.json(), indent=4))
    #print ("All devices count: ",json.dumps(response01.json()["response"], indent=4))
    device_list = json.dumps(my_resp.json(), indent = 2)
    print(device_list)

    if my_resp.ok:
      for device in my_resp.json()["response"]:
        print(f"ID: {device['id']} IP: {device['managementIpAddress']}")

    else:
      print(f"Device collection failed with code {my_resp.status_code}")
      print(f"Failure body: {my_resp.text}")

my_main()