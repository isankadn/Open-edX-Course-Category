import os

from setuptools import find_packages, setup


setup(
    name='course-category',
    version='1.0',
    description='Open edX - Course category assignments',
    packages=['course_category'],
    install_requires=[
        'Django',
    ],
)