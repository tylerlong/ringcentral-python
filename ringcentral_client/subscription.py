from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub as PubNubSDK
from pubnub.callbacks import SubscribeCallback
from Cryptodome.Cipher import AES
import base64
from threading import Timer

class PubNub(object):
    def __init__(self, rest_client, events, message_callback, status_callback = None, presence_callback = None):
        self.rc = rest_client
        self.events = events
        this = self # for inner class to access self
        class MySubscribeCallback(SubscribeCallback):
            def status(self, pubnub, status):
                status_callback and status_callback(status)
            def presence(self, pubnub, presence):
                presence_callback and presence_callback(presence)
            def message(self, pubnub, message):
                encryptionKey = base64.b64decode(this.subscription['deliveryMode']['encryptionKey'])
                aes = AES.new(encryptionKey, AES.MODE_ECB)
                json = aes.decrypt(base64.b64decode(message.message)).decode('utf-8').strip()
                message_callback(json)
        self.callback = MySubscribeCallback()
        self._subscription = None
        self._timer = None

    @property
    def subscription(self):
        return self._subscription

    @subscription.setter
    def subscription(self, value):
        self._subscription = value
        if self._timer:
            self._timer.cancel()
            self._timer = None
        if value:
            self._timer = Timer(value['expiresIn'] - 120, self.refresh)
            self._timer.daemon = True # so main thread won't wait for timer
            self._timer.start()

    def subscribe(self):
        r = self.rc.post('/restapi/v1.0/subscription', self._request_body())
        self.subscription = r.json()
        pnconfig = PNConfiguration()
        pnconfig.subscribe_key = self.subscription['deliveryMode']['subscriberKey']
        self.pubnub = PubNubSDK(pnconfig)
        self.pubnub.add_listener(self.callback)
        self.pubnub.subscribe().channels(self.subscription['deliveryMode']['address']).execute()

    def refresh(self):
        if not self.subscription:
            return
        r = self.rc.put('/restapi/v1.0/subscription/{id}'.format(id = self.subscription['id']), self._request_body())
        self.subscription = r.json()

    def revoke(self):
        if not self.subscription:
            return
        self.pubnub.unsubscribe().channels(self.subscription['deliveryMode']['address']).execute()
        self.pubnub.remove_listener(self.callback)
        self.pubnub = None
        self.rc.delete('/restapi/v1.0/subscription/{id}'.format(id = self.subscription['id']))
        self.subscription = None

    def _request_body(self):
        return {
            'deliveryMode': { 'transportType': 'PubNub', 'encryption': True },
            'eventFilters': self.events
        }
