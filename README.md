# ringcentral-python

[![Build status](https://api.travis-ci.org/tylerlong/ringcentral-python.svg?branch=master)](https://travis-ci.org/tylerlong/ringcentral-python)
[![Coverage Status](https://coveralls.io/repos/github/tylerlong/ringcentral-python/badge.svg?branch=master)](https://coveralls.io/github/tylerlong/ringcentral-python?branch=master)

RingCentral Python Client library

Both Python 2.x and Python 3.x are suppored.


## Installation

```
pip install ringcentral_client
```

Or install from GitHub directly:

```
pip install git+git://github.com/tylerlong/ringcentral-python.git
```


## Documentation

https://developer.ringcentral.com/api-docs/latest/index.html


## Usage


### For sandbox

```python
from ringcentral_client import RestClient, SANDBOX_SERVER

rc = RestClient(appKey, appSecret, SANDBOX_SERVER)
```

`SANDBOX_SERVER` is a string constant for `https://platform.devtest.ringcentral.com`.


### For production

```python
from ringcentral_client import RestClient, PRODUCTION_SERVER

rc = RestClient(appKey, appSecret, PRODUCTION_SERVER)
```

`PRODUCTION_SERVER` is a string constant for `https://platform.ringcentral.com`.


### Authorization

```python
r = rc.authorize(username, extension, password)
print 'authorized'

r = rc.refresh()
print 'refreshed'

r = rc.revoke()
print 'revoked'
```


### Authorization Refresh

By default, authorization is automatically refreshed 2 minutes before it expires.

**Don't forget** to call `rc.revoke()` when you are done.
Otherwise your app won't quit because there is a background timer running.

If you want to refresh it yourself, you can `rc.auto_refresh = False`.



### HTTP Requets

```python
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
```


### Subscription

```python
def message_callback(message):
    print message

# subscribe
events = ['/restapi/v1.0/account/~/extension/~/message-store']
subscription = rc.subscription(events, message_callback)
subscription.subscribe()

# refresh
# Please note that subscription auto refreshes itself
# so most likely you don't need to refresh it manually
subscription.refresh()

# revoke
# Once you no longer need this subscription, don't forget to revoke it
subscription.revoke()
```


### Send fax

```python
with open(os.path.join(os.path.dirname(__file__), 'test.png'), 'rb') as image_file:
    files = [
        ('json', ('request.json', json.dumps({ 'to': [{ 'phoneNumber': receiver }] }), 'application/json')),
        ('attachment', ('test.txt', 'Hello world', 'text/plain')),
        ('attachment', ('test.png', image_file, 'image/png')),
    ]
    r = rc.post('/restapi/v1.0/account/~/extension/~/fax', files = files)
    print r.status_code
```


### Send MMS

```python
params = {
    'to': [{'phoneNumber': receiver}],
    'from': {'phoneNumber': username},
    'text': 'Hello world'
}
with open(os.path.join(os.path.dirname(__file__), 'test.png'), 'rb') as image_file:
    files = [
        ('json', ('request.json', json.dumps(params), 'application/json')),
        ('attachment', ('test.png', image_file, 'image/png')),
    ]
    r = rc.post('/restapi/v1.0/account/~/extension/~/sms', params, files = files)
    print r.status_code
```


### Sample code for binary downloading and uploading

```python
# Upload
with open(os.path.join(os.path.dirname(__file__), 'test.png'), 'rb') as image_file:
    files = {'image': ('test.png', image_file, 'image/png')}
    r = rc.post('/restapi/v1.0/account/~/extension/~/profile-image', files = files)

# Download
r = rc.get('/restapi/v1.0/account/~/extension/~/profile-image')
# r.content is the downloaded binary
```


## More sample code

Please refer to the [test cases](https://github.com/tylerlong/ringcentral-python/tree/master/test).


## License

MIT
