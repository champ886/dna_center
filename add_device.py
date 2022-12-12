import time
import requests
from post_to_get_token_function import get_token
import json

def main ():

    token = get_token
    url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"
    headers = {
        "Content-Type":"application/json",
        "X-Auth-Token": token
    }

    new_device_diction = {
        "ipAdress": ["192.168.0.2.1"],
        "snmpVersion": "v2",
        "snmpRWCommunity": "readwrite",
        "snmpROCommunity": "readonly",
        "snmpRetry": "1",
        "snmpTimeout": "60",
        "cliTransport": "ssh",
        "userName": "champ",
        "password": "secret123!",
        "enablePassword": "password"
    }

    add_my_resp = requests.post(url, headers, json=new_device_diction)

    if add_my_resp.ok:

        # Wait 10 secs after server responds print
        (f"Request accepted: status code {add_my_resp.status_code}")
        time.sleep(10)

        url2 = "https://sandboxdnac.cisco.com/dna/intent/api/v1"

        task = add_my_resp.json() ["response"]["taskid"]
        task_resp = requests.get(f"{url2}/task/{task}", headers =headers
        )

        if task_resp.ok:
            task_data = task_resp.json()["response"]
            if not task_data["isError"]:
                print("New device successfully added")
            else:
                print(f"Async task error seen: {task_data['progress']}")

        else: 
            print(f"Asyn GET failed: status code {task_resp.status_code}")

    else:
        print(f"Device failed with code bla bla")