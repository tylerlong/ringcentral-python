from .test_base import BaseTestCase
import time
import json
import os
from ringcentral_client import PubNub

class SubscriptionTestCase(BaseTestCase):
    def setUp(self):
        super(SubscriptionTestCase, self).setUp()
        # subscribe
        events = [
            '/restapi/v1.0/account/~/extension/~/message-store',
        ]
        self.subscription = PubNub(self.rc, events, self.message_callback)
        self.subscription.subscribe()

    def message_callback(self, message):
        self.count += 1

    def test_pubnub_sms(self):
        self.count = 0

        # refresh
        # call refresh manually shouldn't break anything
        self.subscription.refresh()

        # send an SMS to tigger a notification
        data = {
            'from': { 'phoneNumber': self.username },
            'to': [{ 'phoneNumber': self.receiver }],
            'text': 'hello world'
        }
        self.rc.post('/restapi/v1.0/account/~/extension/~/sms', data)

        # wait for the notification to come
        time.sleep(20)
        self.assertGreater(self.count, 0)

    def test_pubnub_fax(self):
        self.count = 0

        # send an fax to tigger a notification
        with open(os.path.join(os.path.dirname(__file__), 'test.png'), 'rb') as image_file:
            files = [
                ('json', ('request.json', json.dumps({ 'to': [{ 'phoneNumber': self.receiver }] }), 'application/json')),
                ('attachment', ('test.txt', 'Hello world', 'text/plain')),
                ('attachment', ('test.png', image_file, 'image/png')),
            ]
            self.rc.post('/restapi/v1.0/account/~/extension/~/fax', files = files)

        # wait for the notification to come
        time.sleep(40)
        self.assertGreater(self.count, 0)

    def tearDown(self):
        self.subscription.revoke()
        super(SubscriptionTestCase, self).tearDown()
