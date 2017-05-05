from .test_base import BaseTestCase
import json
import os

class ExceptionTestCase(BaseTestCase):
    def test_404(self):
        try:
            r = self.rc.get('/restapi/v1.0/account/~/extension/~/does-not-exist')
        except Exception as e:
            self.assertTrue('Invalid URI' in str(e))
            self.assertTrue('404' in str(e))
