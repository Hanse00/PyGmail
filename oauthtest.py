import json
from subprocess import call

POST_URL = "https://accounts.google.com/o/oauth2/device/code"
SCOPE = "profile"

f = open("client_secret.json", "r")
client_secret_file = json.load(f)
f.close()

client_id =client_secret_file['installed']['client_id']
client_secret = client_secret_file['installed']['client_secret']

print "Client ID: " + client_id
print "Client Secret: " + client_secret

response = call("curl -d \"client_id=" + client_id + "&scope=" + SCOPE + "\" " + POST_URL)
print response
