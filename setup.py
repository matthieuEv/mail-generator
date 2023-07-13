from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='mail-Generator',
    version='0.2.1',
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
    long_description_content_type='text/markdown'
)
