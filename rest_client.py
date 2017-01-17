class RestClient(object):
    def __init__(self, appKey, appSecret, server):
        self.appKey = appKey
        self.appSecret = appSecret
        self.server = server
    def authorize(self, username, extension, password):
        print('authorize')
