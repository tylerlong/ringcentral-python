import os
from dotenv import load_dotenv, find_dotenv
import unittest
import sys
import time
from ringcentral_client import RestClient

load_dotenv(find_dotenv())

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.production = os.environ.get('production') == 'true'
        self.clientId = os.environ.get('clientId')
        self.clientSecret = os.environ.get('clientSecret')
        self.server = os.environ.get('server')
        self.username = os.environ.get('username')
        self.extension = os.environ.get('extension')
        self.password = os.environ.get('password')
        self.receiver = os.environ.get('receiver')
        self.rc = RestClient(self.clientId, self.clientSecret, self.server)
        self.rc.authorize(self.username, self.extension, self.password)

    def tearDown(self):
        self.rc.revoke()
        time.sleep(12)
