from setuptools import setup
from setuptools import find_packages

classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    ]

setup(
    name="internet-connection",
    version="0.0.1",
    description="Library to monitor internet connection state, when last online/offline, read external IP address, etc",
    keywords=["internet connection", "connection state", "online", "offline", "uptime", "downtime", "internal ip", "external ip", "public ip"],
    long_description=open("README.md").read(),
    author="Dennis Lee",
    author_email="wylee2000@gmail.com",
    url="https://github.com/dennislwy/internet-connection-python",
    classifiers=classifiers,
    packages=find_packages(exclude=['tests']),
    license="MIT"
)