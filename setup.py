from setuptools import setup, find_packages

setup(
    name='ringcentral_client',
    version='0.7.0',
    description='Python Client for RingCentral API',
    author='Tyler Liu',
    author_email='tyler.liu@ringcentral.com',
    url='https://github.com/tylerlong/ringcentral-python',
    packages=find_packages(exclude=('test*',)),
    license='MIT',
    install_requires=[
        'requests>=2.28.2',
    ],
)
