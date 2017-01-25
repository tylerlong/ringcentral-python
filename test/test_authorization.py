from .test_base import BaseTestCase

class AuthorizationTestCase(BaseTestCase):
    def test_authorize_uri(self):
        url = self.rc.authorize_uri('http://baidu.com', 'state')
        self.assertIn(self.server, url)
        self.assertIn('/restapi/oauth/authorize?', url)
        self.assertIn('client_id=' + self.appKey, url)
        self.assertIn('state=state', url)
        self.assertIn('redirect_uri=http%3A%2F%2Fbaidu.com', url)
        self.assertIn('response_type=code', url)

    def test_refresh(self):
        self.rc.refresh()
        r = self.rc.get('/restapi/v1.0/dictionary/country/46')
        self.assertEqual(200, r.status_code)

    def test_authorize(self):
        self.rc.token = None
        self.rc.authorize(self.username, self.extension, self.password)
        r = self.rc.get('/restapi/v1.0/dictionary/country/46')
        self.assertEqual(200, r.status_code)

    def test_revoke(self):
        self.rc.revoke()
        self.assertEqual(None, self.rc.token)
