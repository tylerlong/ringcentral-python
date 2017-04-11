from .test_base import BaseTestCase
import json
import os

class MmsTestCase(BaseTestCase):
    def test_send_mms(self):
        params = {
            'to': [{'phoneNumber': self.receiver}],
            'from': {'phoneNumber': self.username},
            'text': 'Hello world'
        }
        with open(os.path.join(os.path.dirname(__file__), 'test.png'), 'rb') as image_file:
            files = [
                ('json', ('request.json', json.dumps(params), 'application/json')),
                ('attachment', ('test.png', image_file, 'image/png')),
            ]
            r = self.rc.post('/restapi/v1.0/account/~/extension/~/sms', params, files = files)
            self.assertEqual(200, r.status_code)
