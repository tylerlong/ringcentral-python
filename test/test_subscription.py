from test_base import BaseTestCase
import time

class SubscriptionTestCase(BaseTestCase):
    def message_callback(self, message):
        self.count += 1

    def test_pubnub(self):
        self.count = 0

        # subscribe
        events = ['/restapi/v1.0/account/~/extension/~/message-store']
        subscription = self.rc.subscription(events, self.message_callback)
        subscription.subscribe()

        # send an SMS to tigger a notification
        data = {
            'from': { 'phoneNumber': self.username },
            'to': [{ 'phoneNumber': self.receiver }],
            'text': 'hello world'
        }
        r = self.rc.post('/restapi/v1.0/account/~/extension/~/sms', data)

        # wait for the notification to come
        time.sleep(20)
        subscription.revoke()
        self.assertGreater(self.count, 0)


if __name__ == '__main__':
    import unittest
    unittest.main()
