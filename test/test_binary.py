from test_base import BaseTestCase
import json
import os

class BinaryTestCase(BaseTestCase):
    def test_download_profile(self):
        r = self.rc.get('/restapi/v1.0/account/~/extension/~/profile-image')
        self.assertEqual(200, r.status_code)
        self.assertGreater(len(r.content), 0)

    def test_upload_profile_image(self):
        files = {'image': ('report.xls', open('report.xls', 'rb'), 'image/png', {'Expires': '0'})}
        r = self.rc.post('/restapi/v1.0/account/~/extension/~/profile-image', files = files)


if __name__ == '__main__':
    import unittest
    unittest.main()
