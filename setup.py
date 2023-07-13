from setuptools import setup, find_packages

setup(
    name='Mail-Generator',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'mailslurp-client',
        'python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            'mail-generator = Mail_Generator.main:main'
        ]
    }
)
