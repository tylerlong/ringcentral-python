## Setup

```
pip install -Ur requirements.txt
```

## How to test

Create `.env` file using `.env.sample` as template.

Run `python -m unittest discover`

Run a specific test case: `python -m unittest test.test_authorization.AuthorizationTestCase`

## Release new version

Update version number in `setup.py`

Create `~/.pypirc` with the following content:

```
[distutils]
index-servers = pypi

[pypi]
repository = https://upload.pypi.org/legacy/
username = username
password = password
```

```
python -m build
twine upload dist/*
```

Ref: https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html

below is the **old** way(not work any more):

```
python3 setup.py sdist upload
```
