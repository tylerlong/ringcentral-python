from rest_client import RestClient

rc = RestClient('appKey', 'appSecret', 'server')
rc.authorize('username', '', 'password')
