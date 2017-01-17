from dotenv import load_dotenv, find_dotenv
import os
from rest_client import RestClient

load_dotenv(find_dotenv())

rc = RestClient(os.environ.get('appKey'), os.environ.get('appSecret'), os.environ.get('server'))
rc.authorize(os.environ.get('username'), os.environ.get('extension'), os.environ.get('password'))

r = rc.get('/restapi/v1.0/dictionary/country/46')
print r.text
