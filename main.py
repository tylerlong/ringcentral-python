from rest_client import RestClient
from env import appKey, appSecret, server, username, extension, password

rc = RestClient(appKey, appSecret, server)
rc.authorize(username, extension, password)

r = rc.get('/restapi/v1.0/dictionary/country/46')
print r.text
