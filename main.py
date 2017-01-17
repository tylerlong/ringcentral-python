from rest_client import RestClient
from env import appKey, appSecret, server, username, extension, password, receiver

def test():
    rc = RestClient(appKey, appSecret, server)
    rc.authorize(username, extension, password)

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

test()
