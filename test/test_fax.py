from test_base import BaseTestCase
import json
import os

class FaxTestCase(BaseTestCase):
    def test_send_fax(self):
        files = [
            ('json', ('request.json', json.dumps({ 'to': [{ 'phoneNumber': self.receiver }] }), 'application/json')),
            ('attachment', ('test.txt', 'Hello world', 'text/plain')),
            ('attachment', ('test.png', open(os.path.join(os.path.dirname(__file__), 'test.png'), 'rb'), 'image/png')),
        ]
        r = self.rc.post('/restapi/v1.0/account/~/extension/~/fax', files = files)
        self.assertEqual(200, r.status_code)


if __name__ == '__main__':
    import unittest
    unittest.main()
