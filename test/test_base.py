import os
import time
import unittest

from dotenv import find_dotenv, load_dotenv

from ringcentral_client import RestClient

load_dotenv(find_dotenv())


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.clientId = os.environ.get("RINGCENTRAL_CLIENT_ID")
        self.clientSecret = os.environ.get("RINGCENTRAL_CLIENT_SECRET")
        self.server = os.environ.get("RINGCENTRAL_SERVER_URL")
        self.jwtToken = os.environ.get("RINGCENTRAL_JWT_TOKEN")
        self.sender = os.environ.get("RINGCENTRAL_SENDER")
        self.receiver = os.environ.get("RINGCENTRAL_RECEIVER")
        self.rc = RestClient(self.clientId, self.clientSecret, self.server)
        self.rc.authorize(self.jwtToken)

    def tearDown(self):
        self.rc.revoke()
        time.sleep(12)
