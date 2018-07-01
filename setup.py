import os
import setuptools


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setuptools.setup(
    name="GBWeb-server-application",
    version="0.0.0",
    author="Gregory Barron",
    author_email="gbarron09@gmail.com",
    description="This is essentially Greg's resume...",
    license="MIT",
    #keywords="example documentation tutorial",
    #url="localhost:5000",
    install_requires=[
        "tornado==5.0.2",
        "pymongo==3.7.0",
        "mongoengine==0.15.0",
        "bcrypt==3.1.4"
    ],
    packages=[],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "License :: Public Domain",
    ],
)
