# Goal : Extract information from 
# GUI : Users > User Roles > "Client Name" > Session Options
# REST : /api/v1/configuration/users/user-roles/

import requests
import logging 
import json
import os

# Variable
Path_to_Auth = "/api/v1/auth"
Path_to_user_roles = "/api/v1/configuration/users/user-roles/"
Local_File_session_options = "/var/www/html/networkdashboard/pcs/session-options.html"


headers = {'content-type': 'application/json'}

Hostname = input("Hostname : ")
username = input("Username : ")
password = input("password : ")

# Functions 
def get_session_timeouts(client,path):
    s = requests.get('https://'+Hostname+path+'/general/session-options', auth=(api_key, ''))
    sd = s.json()
    htmldata = "<tr><td>" + client + "</td><td>" + sd['idle-timeout'] + "</td><td>" + sd['max-timeout'] + "</td><td>" + sd['reminder-time']
    f = open(Local_File_session_options, 'a')
    f.write(str(htmldata))
    f.close()
   
try:
    os.remove(Local_File_session_options)
except OSError:
    pass

# Get the Authentication API_KEY 
r = requests.get('https://'+Hostname+Path_to_Auth, auth=(username, password), headers=headers)
d = r.json()
api_key = (d['api_key'])

# Open file to add Start HTML tags 
f = open(Local_File_session_options, 'a')
HTMLHead = """<html>
<head>
 <title>PCS Session Timeouts</title>
</head>
<body>
<table border="1">"""
f.write(HTMLHead)
HTMLHeading = "<tr><th>Client</th><th>idle-timeout</th><th>max-timeout</th><th>reminder-timeout</th></tr>"
f.write(HTMLHeading)
f.close()

rr = requests.get('https://vpn.evenue.net/api/v1/configuration/users/user-roles', auth=(api_key, ''))
data = rr.json()

for k1 in data:
    data1 = data[k1]
    for k2 in data1:
        get_session_timeouts(k2['name'],k2['href'])

f = open(Local_File_session_options, 'a')
HTMLTail = """</table>
</body></html>"""
f.write(HTMLTail)
f.close()
