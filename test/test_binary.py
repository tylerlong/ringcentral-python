from .test_base import BaseTestCase
import json
import os

class BinaryTestCase(BaseTestCase):
    def test_download_profile(self):
        r = self.rc.get('/restapi/v1.0/account/~/extension/~/profile-image')
        self.assertEqual(200, r.status_code)
        self.assertGreater(len(r.content), 0)

    def test_upload_profile_image(self):
        with open(os.path.join(os.path.dirname(__file__), 'test.png'), 'rb') as image_file:
            files = {'image': ('test.png', image_file, 'image/png')}
            r = self.rc.post('/restapi/v1.0/account/~/extension/~/profile-image', files = files)
            self.assertEqual(204, r.status_code)
