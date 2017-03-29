from .test_base import BaseTestCase

class MeetingsTestCase(BaseTestCase):
    def test_get_meetings_list(self):
        try:
            self.rc.get('/restapi/v1.0/account/~/extension/~/meeting')
        except Exception as e:
            self.assertTrue('permission required' in str(e))
            self.assertTrue('403' in str(e))
