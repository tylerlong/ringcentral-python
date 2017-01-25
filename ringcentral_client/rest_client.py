import urllib.parse
import requests
import base64
from .subscription import Subscription

class RestClient(object):
    def __init__(self, appKey, appSecret, server):
        self.appKey = appKey
        self.appSecret = appSecret
        self.server = server
        self.token = None

    def authorize(self, username = None, extension = None, password = None, auth_code = None, redirect_uri = None):
        if auth_code:
            data = {
                'grant_type': 'authorization_code',
                'code': auth_code,
                'redirect_uri': redirectUri,
            }
        else:
            data = {
                'grant_type': 'password',
                'username': username,
                'extension': extension,
                'password': password,
            }
        r = self.post('/restapi/oauth/token', data = data)
        self.token = r.json()
        return r

    def refresh(self):
        data = {
            'grant_type': 'refresh_token',
            'refresh_token': self.token['refresh_token'],
        }
        self.token = None
        r = self.post('/restapi/oauth/token', data = data)
        self.token = r.json()
        return r

    def revoke(self):
        if self.token == None:
            return
        data = {
            'token': self.token['access_token']
        }
        self.token = None
        return self.post('/restapi/oauth/revoke', data = data)

    def authorize_uri(self, redirect_uri, state = ''):
        url = urllib.parse.urljoin(self.server, '/restapi/oauth/authorize')
        params = {
            'response_type': 'code',
            'state': state,
            'redirect_uri': redirect_uri,
            'client_id': self.appKey
        }
        req = requests.PreparedRequest()
        req.prepare_url(url, params = params)
        return req.url

    def get(self, endpoint, params = None):
        return self._request('GET', endpoint, params)

    def post(self, endpoint, json = None, params = None, data = None, files = None):
        return self._request('POST', endpoint, params, json, data, files)

    def put(self, endpoint, json = None, params = None, data = None, files = None):
        return self._request('PUT', endpoint, params, json, data, files)

    def delete(self, endpoint, params = None):
        return self._request('DELETE', endpoint, params)

    def subscription(self, event_filters, callback):
        return Subscription(self, event_filters, callback)

    def _autorization_header(self):
        if self.token:
            return 'Bearer {access_token}'.format(access_token = self.token['access_token'])
        return 'Basic {basic_key}'.format(basic_key = self._basic_key())

    def _basic_key(self):
        return base64.b64encode('{appKey}:{appSecret}'.format(appKey = self.appKey, appSecret = self.appSecret))

    def _request(self, method, endpoint, params = None, json = None, data = None, files = None):
        url = urllib.parse.urljoin(self.server, endpoint)
        headers = { 'Authorization': self._autorization_header() }
        r = requests.request(method, url, params = params, data = data, json = json, files = files, headers = headers)
        r.raise_for_status()
        return r
