from .test_base import BaseTestCase

class MeetingsTestCase(BaseTestCase):
    def test_get_meetings_list(self):
        r = self.rc.get('/restapi/v1.0/account/~/extension/~/meeting')
        self.assertEqual(200, r.status_code)
