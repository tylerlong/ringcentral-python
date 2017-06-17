from .test_base import BaseTestCase
import json
import os

class FaxTestCase(BaseTestCase):
    def test_send_fax(self):
        with open(os.path.join(os.path.dirname(__file__), 'test.png'), 'rb') as image_file:
            files = [
                ('json', ('request.json', json.dumps({ 'to': [{ 'phoneNumber': self.receiver }] }), 'application/json')),
                ('attachment', ('test.txt', 'Hello world', 'text/plain')),
                ('attachment', ('test.png', image_file, 'image/png')),
            ]
            r = self.rc.post('/restapi/v1.0/account/~/extension/~/fax', files = files)
            self.assertEqual(200, r.status_code)

    def test_list_fax(self):
        r = self.rc.get('/restapi/v1.0/account/~/extension/~/message-store', { 'messageType': "Fax", 'perPage': 1000, 'dataFrom': '2010-01-26T17:49:00.000Z' })
        self.assertEqual(200, r.status_code)
        records = r.json()['records']
        self.assertGreater(len(records), 0)
        self.assertEqual('Fax', records[0]['type'])

    def test_resend_fax(self):
        with open(os.path.join(os.path.dirname(__file__), 'test.png'), 'rb') as image_file:
            files = [
                ('json', ('request.json', json.dumps({ 'to': [{ 'phoneNumber': self.receiver }] }), 'application/json')),
                ('attachment', ('test.txt', 'Hello world', 'text/plain')),
                ('attachment', ('test.png', image_file, 'image/png')),
            ]
            r = self.rc.post('/restapi/v1.0/account/~/extension/~/fax', files = files)
            message_id = r.json()['id']

            r = self.rc.post('/restapi/v1.0/account/~/extension/~/fax', { 'originalMessageId': message_id })
            self.assertEqual(200, r.status_code)
