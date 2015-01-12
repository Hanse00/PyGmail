import json
import requests
import time
import sys
import logging

POST_URL = "https://accounts.google.com/o/oauth2/device/code"
TOKEN_URL = "https://accounts.google.com/o/oauth2/token"
SCOPE = "profile https://www.googleapis.com/auth/plus.me"
GRANT_TYPE = "http://oauth.net/grant_type/device/1.0"
PEOPLE_API = "https://www.googleapis.com/plus/v1/people/me"

#logging.basicConfig()
#logging.getLogger().setLevel(logging.DEBUG)
#requests_log = logging.getLogger("requests.packages.urllib3")
#requests_log.setLevel(logging.DEBUG)
#requests_log.propagate = True

f = open("client_secret.json", "r")
client_secret_file = json.load(f)
f.close()

client_id =client_secret_file['installed']['client_id']
client_secret = client_secret_file['installed']['client_secret']

print "Client ID: " + client_id
print "Client Secret: " + client_secret

headers = {'Content-Type': 'application/x-www-form-urlencoded'}
payload = {'client_id': client_id, "scope": SCOPE}
response = requests.post(POST_URL, data=payload, headers=headers)

response_json = json.loads(response.text)

verification_url = response_json['verification_url']
user_code = response_json['user_code']

print "Verification URL: " + verification_url
print "User code: " + user_code

poll_time = 0
sleep = response_json['interval']
expiration_window = response_json['expires_in']
device_code = response_json['device_code']

payload2 = {'client_id': client_id, 'client_secret': client_secret, 'code': device_code, 'grant_type': GRANT_TYPE}
while poll_time <= expiration_window:
    print "Wait time: " + str(poll_time) + " seconds."
    response2 = requests.post(TOKEN_URL, data=payload2, headers=headers)
    response_json2 = json.loads(response2.text)
    if (not "error" in response_json2):
        break
    print json.loads(response2.text)
    poll_time += sleep
    time.sleep(sleep)
else:
    print "Login timed out"
    sys.exit(0)

print response_json2['access_token']

header3 = {"Authorization": "Bearer " + response_json2['access_token']}
response3 = requests.get(PEOPLE_API, headers=header3)

print response3.text

response_json3 = json.loads(response3.text)
print response_json3

name = response_json3['displayName']

print "Welcome " + name + "!"
