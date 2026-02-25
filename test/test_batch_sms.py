import json
import os

from .test_base import BaseTestCase

class BatchSMSTestCase(BaseTestCase):
    def test_send_batch_sms(self):
        params = {
            "from": {"phoneNumber": self.sender},
            "text": "Hello world",
            "messages": [
              { "to": [ { "phoneNumber": self.receiver } ] },
            ]
        }
        with open(
            os.path.join(os.path.dirname(__file__), "test.png"), "rb"
        ) as image_file:
            files = [
                ("metadata", ("request.json", json.dumps(params), "application/json")),
                ("whatever2", ("test.png", image_file, "image/png")),
            ]
            r = self.rc.post(
                "/restapi/v2/accounts/~/extensions/~/sms/batches", params, files=files
            )
            self.assertEqual(201, r.status_code)
