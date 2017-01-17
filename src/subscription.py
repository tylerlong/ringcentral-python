from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

class Subscription(object):
    def __init__(self, rest_client, events, callback):
        self.rc = rest_client
        self.events = events
        self.callback = callback()

    def subscribe(self):
        r = self.rc.post('/restapi/v1.0/subscription', self._request_body())
        self.subscription = r.json()
        pnconfig = PNConfiguration()
        pnconfig.subscribe_key = self.subscription['deliveryMode']['subscriberKey']
        pnconfig.publish_key = ''
        self.pubnub = PubNub(pnconfig)
        self.pubnub.add_listener(self.callback)
        self.pubnub.subscribe().channels(self.subscription['deliveryMode']['address']).execute()

    def refresh(self):
        if not self.subscription:
            return
        r = self.rc.post('/restapi/v1.0/subscription', self._request_body())
        self.subscription = r.json()

    def revoke(self):
        self.pubnub.remove_listener(self.callback)
        self.rc.delete('/restapi/v1.0/subscription/{id}'.format(id = self.subscription['id']))
        self.subscription = None

    def _request_body(self):
        return {
            'deliveryMode': { 'transportType': 'PubNub', 'encryption': True },
            'eventFilters': self.events
        }
