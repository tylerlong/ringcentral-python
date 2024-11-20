# ringcentral-python

RingCentral Python Client library

Only Python 3.x is supported.

## Getting help and support

If you are having difficulty using this SDK, or working with the RingCentral API, please visit our [developer community forums](https://community.ringcentral.com/spaces/144/) for help and to get quick answers to your questions. If you wish to contact the RingCentral Developer Support team directly, please [submit a help ticket](https://developers.ringcentral.com/support/create-case) from our developer website.

## Installation

```
pip install ringcentral_client
```

## Documentation

https://developer.ringcentral.com/api-docs/latest/index.html

## Usage

### For sandbox

```python
from ringcentral_client import RestClient, SANDBOX_SERVER

rc = RestClient(clientId, clientSecret, SANDBOX_SERVER)
```

`SANDBOX_SERVER` is a string constant for `https://platform.devtest.ringcentral.com`.

### For production

```python
from ringcentral_client import RestClient, PRODUCTION_SERVER

rc = RestClient(clientId, clientSecret, PRODUCTION_SERVER)
```

`PRODUCTION_SERVER` is a string constant for `https://platform.ringcentral.com`.

### Authorization

```python
r = rc.authorize(jwtToken)
print('authorized')

r = rc.refresh()
print('refreshed')

r = rc.revoke()
print('revoked')
```

### Authorization Refresh

If you want the SDK to refresh authorization automatically, you can `rc.auto_refresh = True`.

If you do so, authorization is refreshed 2 minutes before it expires.
**Don't forget** to call `rc.revoke()` when you are done. Otherwise your app won't quit because there is a background timer running.

### HTTP Requests

```python
# GET
r = rc.get('/restapi/v1.0/account/~/extension/~')
print(r.text)

# POST
r = rc.post('/restapi/v1.0/account/~/extension/~/sms', {
    'to': [{'phoneNumber': receiver}],
    'from': {'phoneNumber': sender},
    'text': 'Hello world'})
print(r.text)

# PUT
r = rc.get('/restapi/v1.0/account/~/extension/~/message-store', { 'direction': 'Outbound' })
message_id = r.json()['records'][0]['id']
r = rc.put('/restapi/v1.0/account/~/extension/~/message-store/{message_id}'.format(message_id = message_id),
    { 'readStatus': 'Read' })
print(r.text)

# DELETE
r = rc.post('/restapi/v1.0/account/~/extension/~/sms', {
    'to': [{ 'phoneNumber': receiver }],
    'from': { 'phoneNumber': sender },
    'text': 'Hello world'})
message_id = r.json()['id']
r = rc.delete('/restapi/v1.0/account/~/extension/~/message-store/{message_id}'.format(message_id = message_id), { 'purge': False })
print(r.status_code)
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
    print(r.status_code)
```

### Send MMS

```python
params = {
    'to': [{'phoneNumber': receiver}],
    'from': {'phoneNumber': sender},
    'text': 'Hello world'
}
with open(os.path.join(os.path.dirname(__file__), 'test.png'), 'rb') as image_file:
    files = [
        ('json', ('request.json', json.dumps(params), 'application/json')),
        ('attachment', ('test.png', image_file, 'image/png')),
    ]
    r = rc.post('/restapi/v1.0/account/~/extension/~/sms', params, files = files)
    print(r.status_code)
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

## Authorization Code Flow (3-legged authorization flow)

Please read the official documentation if you don't already know what is [Authorization Code Flow](http://ringcentral-api-docs.readthedocs.io/en/latest/oauth/#authorization-code-flow).

### Step 1: build the authorize uri

```python
uri = rc.authorize_uri('http://example.com/callback', 'state')
```

### Step 2: redirect user to `uri`

User will be prompted to login RingCentral and authorize your app.

If everything goes well, user will be redirect to `http://example.com/callback?code=<auth_code>`.

### Step 3: extract auth_code

`http://example.com/callback?code=<auth_code>`

Extract `auth_code` from redirected url.

### Step 4: authorize

```python
rc.authorize(auth_code = auth_code, redirect_uri = 'http://example.com/callback')
```

## More sample code

Please refer to the [test cases](https://github.com/tylerlong/ringcentral-python/tree/master/test).

## Add access token to URL

For example, for voicemail MP3, you will get a content URL like the following in extension/message-store response:

```
https://media.ringcentral.com/restapi/v1.0/account/1111/extension/2222/message-store/3333/content/4444
```

You can add access token to the URL:

```
https://media.ringcentral.com/restapi/v1.0/account/1111/extension/2222/message-store/3333/content/4444?access_token=<theAccessToken>
```

This is mostly for embedding into sites like Glip temporarily or for sending to VoiceBase, etc.

## License

MIT
