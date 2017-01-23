import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../ringcentral_client'))

from rest_client import RestClient
from env import appKey, appSecret, server, username, extension, password, receiver

rc = RestClient(appKey, appSecret, server)

r = rc.authorize(username, extension, password)
print r.status_code
print 'authorized'

r = rc.refresh()
print r.status_code
print 'refreshed'

r = rc.revoke()
print r.status_code
print 'revoked'

print rc.authorize_uri('http://baidu.com', 'state')
