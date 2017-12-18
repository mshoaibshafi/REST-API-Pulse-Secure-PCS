# worked and got the api key

import requests
import logging
import json

try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client
http_client.HTTPConnection.debuglevel = 1

headers = {'content-type': 'application/json'}

# Variable
Path-to-Auth = /api/vi/auth/
Path-to-user-roles = /api/v1/configuration/users/user-roles/

# Test 
hostname = input("Hostname :")
username = input("Username :")
password = input("password")

try:
    r = requests.get('https://'hostname+Path-to-Auth, auth=(username, password), headers=headers)
except requests.exceptions.ConnectionError:
    r.status_code = "Connection refused"

print ("\n--- Status Code")
print (r.status_code)
print ("\n--- text")
print (r.text)
print ("\n--- Desired Text")
print (r.text[12:56])
print ("\n--- Headers")
print (r.headers)
print ("\n--- JSON response")
print (r.json())
d = r.json()
print ("\n--- d")
api_key = (d['api_key'])
print (api_key)
print (r.content)


rr = requests.get('https://'hostname+Path-to-user-roles, auth=(api_key, ''))
data = rr.json()
length = len(data)
print ("\n--- length", length)

for key in data:
    print (key, 'equal to', data[key])
    data1 = data[key]
    for key1 in data1:
        print (key1, 'equal to', data1[key1])
        rrr = requests.get('https://'+hostname+data1[key1], auth=(api_key, ''))
        data2 = rrr.json()
        for key2 in data2:
            print (key2, 'equal to', data2[key2])
