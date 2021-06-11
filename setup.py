from setuptools import setup, find_packages

import os
import re
from os.path import abspath, dirname, join
from shutil import rmtree

setup(
    name='robotframework_practitest_listener',
    version='0.1.0',
    packages=['robotframework_practitest_listener'],
    url='',
    license='MIT',
    author='Dmitry Oguz',
    author_email='doguz2509@gmail.com',
    description='Listener allow upload robotFW execution into Practitest'
)


current_dir = dirname(abspath(__file__))


def read_file(file_name):
    """Read the given file.
    :param file_name: Name of the file to be read
    :return:      Output of the given file
    """
    with open(os.path.join(os.path.dirname(__file__), file_name)) as sr:
        return sr.read()


rmtree('dist', True)

setup(
    name='robotframework_practitest_listener',
    version='0.1.0',
    packages=find_packages(exclude=['venv']),
    package_data={'': []},
    url='',
    license='MIT',
    author='Dmitry Oguz',
    author_email='doguz2509@gmail.com',
    description='Listener allow upload robotFW execution into Practitest',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    install_requires=read_file('requirements.txt'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Robot Framework",
        "Framework :: Robot Framework :: Library",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha"
    ]
)
