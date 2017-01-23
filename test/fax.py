import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../ringcentral_client'))

from rest_client import RestClient
from env import appKey, appSecret, server, username, extension, password, receiver
import json

rc = RestClient(appKey, appSecret, server)
rc.authorize(username, extension, password)

files = [
    ('json', ('request.json', json.dumps({ 'to': [{ 'phoneNumber': receiver }] }), 'application/json')),
    ('attachment', ('test.txt', 'Hello world', 'text/plain')),
    ('attachment', ('test.png', open(os.path.join(os.path.dirname(__file__), 'test.png'), 'rb'), 'image/png')),
]
r = rc.post('/restapi/v1.0/account/~/extension/~/fax', files = files)
print r.status_code
