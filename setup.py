from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='mail-Generator',
    version='0.2.2',
    packages=find_packages(),
    install_requires=[
        'mailslurp-client',
    ],
    entry_points={
        'console_scripts': [
            'mail-generator = Mail_Generator.main:main'
        ]
    },
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/matthieuEv/mail-generator',
    description='A Python package that provides an easy-to-use interface for creating and managing email addresses'
)
