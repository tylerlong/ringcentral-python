# ringcentral-python

RingCentral Python Client library


## Setup

```
pip install -Ur requirements.txt
```


## How to test

Create `.env` file with the following content:

```
production=false
server=https://platform.devtest.ringcentral.com
appKey=appKey
appSecret=appSecret
username=username
extension=extension
password=password
receiver=number-to-receiver-sms
```

Run `python test/index.py`



## todo

- release to pip
- use a real testing framework
- ci and testing coverage
- auto refresh pubnub
- add a sample for fax sending
- add a sample for binary downloading
