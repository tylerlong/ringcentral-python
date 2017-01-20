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
    def message_callback(json):
        print json

    # subscribe
    events = ['/restapi/v1.0/account/~/extension/~/message-store']
    subscription = rc.subscription(events, message_callback)
    subscription.subscribe()

    # send an SMS to tigger a notification
    data = {
        'from': { 'phoneNumber': username },
        'to': [{ 'phoneNumber': receiver }],
        'text': "hello world"
    }
    r = rc.post('/restapi/v1.0/account/~/extension/~/sms', data)

    # wait for the notification to come
    time.sleep(20)


# test_CRUD()
test_PubNub()
