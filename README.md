# ringcentral-python

RingCentral Python Client library


## Installation

```
pip install git+git://github.com/tylerlong/ringcentral-python.git
```

---

---

---


## Below is for maintainers of this library

### Setup

```
pip install -Ur requirements.txt
```


### How to test

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



### todo

- release to pip
- use a real testing framework
- ci and testing coverage
- add a sample for fax sending
- add a sample for binary downloading
