import urlparse
import requests
import base64

class RestClient(object):
    def __init__(self, appKey, appSecret, server):
        self.appKey = appKey
        self.appSecret = appSecret
        self.server = server
        self.token = None

    def authorize(self, username, extension, password):
        url = urlparse.urljoin(self.server, '/restapi/oauth/token')
        data = {
            'username': username,
            'extension': extension,
            'password': password,
            'grant_type': 'password'
        }
        headers = {
            'Authorization': self._autorization_header()
        }
        r = requests.post(url, data = data, headers = headers)
        self.token = r.json()

    def get(self, endpoint, params = None):
        url = urlparse.urljoin(self.server, endpoint)
        headers = {
            'Authorization': self._autorization_header()
        }
        return requests.get(url, params = params, headers = headers)

    def _autorization_header(self):
        if self.token:
            return 'Bearer {access_token}'.format(access_token = self.token['access_token'])
        return 'Basic {basic_key}'.format(basic_key = self._basic_key())

    def _basic_key(self):
        return base64.b64encode('{appKey}:{appSecret}'.format(appKey = self.appKey, appSecret = self.appSecret))
