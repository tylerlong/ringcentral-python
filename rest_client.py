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
        data = {
            'username': username,
            'extension': extension,
            'password': password,
            'grant_type': 'password'
        }
        r = self.post('/restapi/oauth/token', data = data)
        self.token = r.json()

    def get(self, endpoint, params = None):
        return self._request('GET', endpoint, params)

    def post(self, endpoint, json = None, params = None, data = None):
        return self._request('POST', endpoint, params, json, data)

    def put(self, endpoint, json = None, params = None, data = None):
        return self._request('PUT', endpoint, params, json, data)

    def delete(self, endpoint, params = None):
        return self._request('DELETE', endpoint, params)

    def _autorization_header(self):
        if self.token:
            return 'Bearer {access_token}'.format(access_token = self.token['access_token'])
        return 'Basic {basic_key}'.format(basic_key = self._basic_key())

    def _basic_key(self):
        return base64.b64encode('{appKey}:{appSecret}'.format(appKey = self.appKey, appSecret = self.appSecret))

    def _request(self, method, endpoint, params = None, json = None, data = None):
        url = urlparse.urljoin(self.server, endpoint)
        headers = { 'Authorization': self._autorization_header() }
        return requests.request(method, url, params = params, data = data, json = json, headers = headers)
