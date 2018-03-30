# Ref: https://medium.com/ringcentral-developers/updating-ringcentral-user-extension-greetings-using-the-rest-api-and-ruby-db325022c6ee

from .test_base import BaseTestCase
import json
import os

class MultipartMixedTestCase(BaseTestCase):
    def test_update_greeting_audio(self):
        r = self.rc.get('/restapi/v1.0/account/~/extension/~/answering-rule')
        self.assertEqual(200, r.status_code)
        answering_rule_id = r.json()['records'][-1]['id']
        # answering_rule_id = 'business-hours-rule'
        # self.rc.debug = True
        with open(os.path.join(os.path.dirname(__file__), 'test.mp3'), 'rb') as audio_file:
            files = [
                ('json', ('request.json', json.dumps({ 'type': 'Voicemail', 'answeringRule': { 'id': answering_rule_id } }), 'application/json')),
                ('binary', ('test.mp3', audio_file, 'audio/mpeg')),
            ]
            r = self.rc.post('/restapi/v1.0/account/~/extension/~/greeting', files = files, multipart_mixed = True)
            self.assertEqual(200, r.status_code)
