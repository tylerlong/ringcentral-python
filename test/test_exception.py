from .test_base import BaseTestCase
import json
import os

class ExceptionTestCase(BaseTestCase):
    def test_404(self):
        try:
            self.rc.get('/restapi/v1.0/account/~/extension/~/does-not-exist')
        except Exception as e:
            self.assertTrue('Resource not found' in str(e))
            self.assertTrue('404' in str(e))
