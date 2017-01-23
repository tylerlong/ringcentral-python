import os
from dotenv import load_dotenv, find_dotenv
import unittest
import sys
import time

load_dotenv(find_dotenv())

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../ringcentral_client'))
from rest_client import RestClient


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.production = os.environ.get('production') == 'true'
        self.appKey = os.environ.get('appKey')
        self.appSecret = os.environ.get('appSecret')
        self.server = os.environ.get('server')
        self.username = os.environ.get('username')
        self.extension = os.environ.get('extension')
        self.password = os.environ.get('password')
        self.receiver = os.environ.get('receiver')
        self.rc = RestClient(self.appKey, self.appSecret, self.server)
        self.rc.authorize(self.username, self.extension, self.password)

    def tearDown(self):
        self.rc.revoke()
        time.sleep(10)
