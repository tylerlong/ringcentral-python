## Setup

```
pip install -Ur requirements.txt
```


## How to test

Create `.env` file with the following content:

```
production=false
server=https://platform.devtest.ringcentral.com
clientId=clientId
clientSecret=clientSecret
username=username
extension=extension
password=password
receiver=number-to-receiver-sms
```

Run `python -m unittest discover`

Run a specific test case: `python -m unittest test.test_authorization.AuthorizationTestCase`


## Release new version

Update version number in setup.py

Create `~/.pypirc` with the following content:

```
[distutils]
index-servers = pypi

[pypi]
repository = https://pypi.python.org/pypi
username = username
password = password
```

```
python3 setup.py sdist upload
```
