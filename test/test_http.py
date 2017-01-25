from .test_base import BaseTestCase

class HttpTestCase(BaseTestCase):
    def test_get(self):
        r = self.rc.get('/restapi/v1.0/account/~/extension/~')
        self.assertEqual(200, r.status_code)

    def test_post(self):
        r = self.rc.post('/restapi/v1.0/account/~/extension/~/sms', {
            'to': [{'phoneNumber': self.receiver}],
            'from': {'phoneNumber': self.username},
            'text': 'Hello world'
        })
        self.assertEqual(200, r.status_code)

    def test_put(self):
        r = self.rc.get('/restapi/v1.0/account/~/extension/~/message-store', { 'direction': 'Outbound' })
        message_id = r.json()['records'][0]['id']
        r = self.rc.put('/restapi/v1.0/account/~/extension/~/message-store/{message_id}'.format(message_id = message_id),
            { 'readStatus': 'Read' })
        self.assertEqual(200, r.status_code)

    def test_delete(self):
        r = self.rc.post('/restapi/v1.0/account/~/extension/~/sms', {
            'to': [{ 'phoneNumber': self.receiver }],
            'from': { 'phoneNumber': self.username },
            'text': 'Hello world'})
        message_id = r.json()['id']
        r = self.rc.delete('/restapi/v1.0/account/~/extension/~/message-store/{message_id}'.format(message_id = message_id), { 'purge': False })
        self.assertEqual(204, r.status_code)
