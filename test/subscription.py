import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../ringcentral_client'))

import time
from rest_client import RestClient
from env import appKey, appSecret, server, username, extension, password, receiver

rc = RestClient(appKey, appSecret, server)
rc.authorize(username, extension, password)

def test_PubNub():
    def message_callback(message):
        print message

    # subscribe
    events = ['/restapi/v1.0/account/~/extension/~/message-store']
    subscription = rc.subscription(events, message_callback)
    subscription.subscribe()

    # send an SMS to tigger a notification
    data = {
        'from': { 'phoneNumber': username },
        'to': [{ 'phoneNumber': receiver }],
        'text': 'hello world'
    }
    r = rc.post('/restapi/v1.0/account/~/extension/~/sms', data)

    # wait for the notification to come
    time.sleep(20)

test_PubNub()
