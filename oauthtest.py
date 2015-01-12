import json

f = open("client_secret.json", "r")
client_secret = json.load(f)
f.close()

print "Client ID: " + client_secret['installed']['client_id']
print "Client Secret: " + client_secret['installed']['client_secret']
