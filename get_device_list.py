import requests
import json
import pprint

url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"

payload={}
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'X-Auth-Token':"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MGVjNGU0ZjRjYTdmOTIyMmM4MmRhNjYiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVlOGU4OTZlNGQ0YWRkMDBjYTJiNjQ4ZSJdLCJ0ZW5hbnRJZCI6IjVlOGU4OTZlNGQ0YWRkMDBjYTJiNjQ4NyIsImV4cCI6MTY3MDQ4MzM3MiwiaWF0IjoxNjcwNDc5NzcyLCJqdGkiOiJhNjkxZjMxZi0yYjNlLTQxNDQtYjNkYy04NTgyMjlmZDVkMjkiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.giWV1Xce5ary8yTqd16Jn54M0pf_puKrJLO6dJ_MI8e9O-E2gsqk6UWNphm0l_EYdNewJg47AuuRApTrwCpVWYTb_L5BUkJRWuoVb6GErZX4z4uJxqU_anaZcBvfM5q1nnVA6TvSyxrAQFsmwDAEFDEXpdoJKw7kS25U-XAP2ApVAJSFqCHM7PYl5RBkgBNOC40Ftg0gHo8cdrmHH7z6SqyYbJ3_riOlcNy8yyQy4yWhtDTy_K5hwtuTM2JkJrU6g1Q-n9rOu3cokbxlvVPGe_eb-eC8kcXXmme6WQHfnlessHAtOiNpyWxGcPXRX_25nhqa-1inASUj8_CkWuuxeQ "

}

params = ""
modifier = "/count"
response = requests.request("GET", url, headers=headers, data=payload,  verify=False)
print ("All network devices: ",json.dumps(response.json()["response"], indent=4))


params = ""
modifier = ""
response = requests.request("GET", url, headers=headers, data=payload,  verify=False)



print ("All network devices: ",json.dumps(response.json()["response"], indent=4))
#print(response.json)

