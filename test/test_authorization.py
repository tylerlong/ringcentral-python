from test_base import BaseTestCase

class AuthorizationTestCase(BaseTestCase):
    def test_authorize_uri(self):
        url = self.rc.authorize_uri('http://baidu.com', 'state')
        self.assertEqual(url, 'https://platform.devtest.ringcentral.com/restapi/oauth/authorize?state=state&redirect_uri=http%3A%2F%2Fbaidu.com&response_type=code&client_id=' + self.appKey)

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


if __name__ == '__main__':
    import unittest
    unittest.main()
