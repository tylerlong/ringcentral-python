from test_base import BaseTestCase
import time

class SubscriptionTestCase(BaseTestCase):
    def message_callback(self, message):
        self.count += 1

    def test_pubnub(self):
        self.count = 0

        # subscribe
        events = ['/restapi/v1.0/account/~/extension/~/message-store']
        self.subscription = self.rc.subscription(events, self.message_callback)
        self.subscription.subscribe()

        # refresh
        # call refresh manually shouldn't break anything
        self.subscription.refresh()

        # send an SMS to tigger a notification
        data = {
            'from': { 'phoneNumber': self.username },
            'to': [{ 'phoneNumber': self.receiver }],
            'text': 'hello world'
        }
        r = self.rc.post('/restapi/v1.0/account/~/extension/~/sms', data)

        # wait for the notification to come
        time.sleep(20)
        self.assertGreater(self.count, 0)

    def tearDown(self):
        self.subscription.revoke()
        super(SubscriptionTestCase, self).tearDown()


if __name__ == '__main__':
    import unittest
    unittest.main()
