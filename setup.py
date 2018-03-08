from setuptools import setup, find_packages

setup(
    name='ringcentral_client',
    version='0.4.0',
    description='Python Client for RingCentral API',
    author='Tyler Long',
    author_email='tyler.liu@ringcentral.com',
    url='https://github.com/tylerlong/ringcentral-python',
    packages=find_packages(exclude=('test*',)),
    license='MIT',
    install_requires=[
        'requests>=2.18.4',
        'pubnub>=4.0.13',
        'pycrypto>=2.6.1',
    ],
)
