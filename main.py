import mailslurp_client
import os
from dotenv import load_dotenv # pip install python-dotenv
import json
import base64

load_dotenv()
api_key = os.getenv('API_KEY')

configuration = mailslurp_client.Configuration()
configuration.api_key['x-api-key'] = api_key


configuration = mailslurp_client.Configuration()
configuration.api_key['x-api-key'] = api_key

def createEmail() -> str:
    """
    Create an email address using the MailSlurp API.

    Returns only the ID of the email address.
    
    (<id-email-address>@mailslurp.com)
    """
    with mailslurp_client.ApiClient(configuration) as api_client:
        try:
            inbox_controller = mailslurp_client.InboxControllerApi(api_client)
            inbox = inbox_controller.create_inbox()
            return str(inbox.id)
        except mailslurp_client.ApiException as e:
            error_body = json.loads(e.body)
            error_message = error_body.get('message')
            return(error_message)

def getEmailData(inbox_id):
    """
    Get the data of the emails in the inbox.

    Returns a list of dictionaries, each dictionary contains the following keys:
    - id            (str)
    - domain_id     (str)
    - subject       (str)
    - to            (list)
    - _from         (str)
    - bcc           (list)
    - cc            (list)
    - created_at    (datetime)
    - read          (boolean)
    - attachments   (list)
    - body          (HTML)
    """

    emailList = []
    with mailslurp_client.ApiClient(configuration) as api_client:
        inbox_controller = mailslurp_client.InboxControllerApi(api_client)
        email_controller = mailslurp_client.EmailControllerApi(api_client)
        emails = inbox_controller.get_emails(inbox_id=inbox_id)
        for email in emails:
            email_details = email_controller.get_email(email.id)
            emailDict = email.to_dict()
            emailDict['body'] = email_details.body
            emailList.append(emailDict)
        return emailList




if __name__ == '__main__':
    # id = createEmail()
    # print(id+"@mailslurp.com")
    # input("Press Enter to continue...")
    for element in getEmailData("70db6f58-2ff6-4b31-b461-2e84bd1f6f81"):
        print(element,'\n\n\n')
