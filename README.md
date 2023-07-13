<p align="center">
  <a href="https://pypi.org/project/mail-Generator/" target="_blank">
    <img src="https://github.com/matthieuEv/mail-generator/blob/main/logo.png?raw=true" alt="Logo" width="300">
  </a>
</p>



# Mail-generator

![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/matthieuEv/mail-generator/python-publish.yml?style=for-the-badge&color=%230a41a8)
![Static Badge](https://img.shields.io/badge/Mail--Generator%20on%20PyPI-230a41a8?style=for-the-badge&color=%230a41a8&link=https%3A%2F%2Fpypi.org%2Fproject%2Fmail-Generator%2F)



## Description
`Mail-Generator` is a Python package that provides an easy-to-use interface for creating and managing  email addresses using the [MailSlurp API](https://www.mailslurp.com/index.html). With `Mail-Generator`, you can quickly create new email addresses, read emails from an inbox, and more. 
## Installation
```bash
pip install mail-generator
```

## Usage
```python
# Import the MailGenerator class
from mail_generator import MailGenerator
# Create a MailGenerator object with your MailSlurp API key
client = MailGenerator(<api_key>)
```
You can find your MailSlurp API key [here](https://app.mailslurp.com/sign-up/).

## Features
### Create an email address
```python
email_id = client.create_email() #  Returns the ID of the email address created.
print(email_id + "@mailslurp.com")
```

### Get emails from an inbox
```python
emails = client.get_email_data(email_id) # Returns a list of emails in the inbox.
```
Example:
```
[
    {
        'id': 'adde245b-fa00-48cd-8a31-77f42737006e',
        'domain_id': None,
        'subject': 'Test',
        'to': ['example@mailslurp.com'],
        '_from': 'example@email.com',
        'bcc': [],
        'cc': [],
        'created_at': datetime.datetime(2023, 7, 13, 11, 28, 7, tzinfo=tzutc()),
        'read': True,
        'attachments': [],
        'body': '<div dir="ltr">Hello World<br></div>\r\n'
    }, 
    {
        'id': 'ede7bb4f-8a47-4631-9ca1-78389a55cced',
        'domain_id': None,
        'subject': 'Hi there',
        'to': ['example@mailslurp.com'],
        '_from': 'example@email.com',
        'bcc': [],
        'cc': [],
        'created_at': datetime.datetime(2023, 7, 13, 11, 29, 33, 473000, tzinfo=tzutc()),
        'read': True,
        'attachments': ['1689251504-9e7166b2-b96c-44cd-8e2a-95500df5c0ac'],
        'body': '<div dir="ltr">This is also a hello world<br></div>\r\n'
    }
]
```
