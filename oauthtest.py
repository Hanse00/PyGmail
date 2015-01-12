import json
import requests

POST_URL = "https://accounts.google.com/o/oauth2/device/code"
SCOPE = "profile"

f = open("client_secret.json", "r")
client_secret_file = json.load(f)
f.close()

client_id =client_secret_file['installed']['client_id']
client_secret = client_secret_file['installed']['client_secret']

print "Client ID: " + client_id
print "Client Secret: " + client_secret

payload = {'client_id': client_id, "scope": SCOPE}
response = requests.post(POST_URL, params=payload)

response_json = json.loads(response.text)

verification_url = response_json['verification_url']
user_code = response_json['user_code']

print "Verification URL: " + verification_url
print "User code: " + user_code
