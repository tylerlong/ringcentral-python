import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

production = os.environ.get('production') == 'true'
appKey = os.environ.get('appKey')
appSecret = os.environ.get('appSecret')
server = os.environ.get('server')
username = os.environ.get('username')
extension = os.environ.get('extension')
password = os.environ.get('password')
receiver = os.environ.get('receiver')
