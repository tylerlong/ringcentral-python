import json
import os

from .test_base import BaseTestCase


class MmsTestCase(BaseTestCase):
    def test_send_mms(self):
        params = {
            "to": [{"phoneNumber": self.receiver}],
            "from": {"phoneNumber": self.sender},
            "text": "Hello world",
        }
        with open(
            os.path.join(os.path.dirname(__file__), "test.png"), "rb"
        ) as image_file:
            files = [
                ("whatever1", ("request.json", json.dumps(params), "application/json")),
                ("whatever2", ("test.png", image_file, "image/png")),
            ]
            r = self.rc.post(
                "/restapi/v1.0/account/~/extension/~/sms", params, files=files
            )
            self.assertEqual(200, r.status_code)
