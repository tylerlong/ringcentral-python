import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

import time
from rest_client import RestClient
from env import appKey, appSecret, server, username, extension, password, receiver

rc = RestClient(appKey, appSecret, server)
rc.authorize(username, extension, password)

def test_CRUD():
    # GET
    r = rc.get('/restapi/v1.0/account/~/extension/~')
    print r.text

    # POST
    r = rc.post('/restapi/v1.0/account/~/extension/~/sms', {
        'to': [{'phoneNumber': receiver}],
        'from': {'phoneNumber': username},
        'text': 'Hello world'})
    print r.text

    # PUT
    r = rc.get('/restapi/v1.0/account/~/extension/~/message-store', { 'direction': 'Outbound' })
    message_id = r.json()['records'][0]['id']
    r = rc.put('/restapi/v1.0/account/~/extension/~/message-store/{message_id}'.format(message_id = message_id),
        { 'readStatus': 'Read' })
    print r.text

    # DELETE
    r = rc.post('/restapi/v1.0/account/~/extension/~/sms', {
        'to': [{ 'phoneNumber': receiver }],
        'from': { 'phoneNumber': username },
        'text': 'Hello world'})
    message_id = r.json()['id']
    r = rc.delete('/restapi/v1.0/account/~/extension/~/message-store/{message_id}'.format(message_id = message_id), { 'purge': False })
    print r.status_code

def test_PubNub():
    from pubnub.callbacks import SubscribeCallback

    class MySubscribeCallback(SubscribeCallback):
        def status(self, pubnub, status):
            print status

        def presence(self, pubnub, presence):
            print presence

        def message(self, pubnub, message):
            print message

    events = ['/restapi/v1.0/account/~/extension/~/message-store']
    subscription = rc.subscription(events, MySubscribeCallback)
    subscription.subscribe()

    data = {
        'from': { 'phoneNumber': username },
        'to': [{ 'phoneNumber': receiver }],
        'text': "hello world"
    }
    r = rc.post('/restapi/v1.0/account/~/extension/~/sms', data)
    print r.status_code

    time.sleep(30) # wait for PubNub notifications


# test_CRUD()
test_PubNub()
