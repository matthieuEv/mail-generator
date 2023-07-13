import mailslurp_client
import os
from dotenv import load_dotenv
import json

class MailGenerator:
    def __init__(self, api_key: str):
        if api_key is None:
            raise ValueError("API_KEY not found in .env file. Please create a .env file with the API_KEY variable.")

        self.configuration = mailslurp_client.Configuration()
        self.configuration.api_key['x-api-key'] = api_key

    def create_email(self) -> str:
        """
        Create an email address using the MailSlurp API.

        Returns only the ID of the email address.

        (<id-email-address>@mailslurp.com)
        """
        with mailslurp_client.ApiClient(self.configuration) as api_client:
            try:
                inbox_controller = mailslurp_client.InboxControllerApi(api_client)
                inbox = inbox_controller.create_inbox()
                return str(inbox.id)
            except mailslurp_client.ApiException as e:
                error_body = json.loads(e.body)
                error_message = error_body.get('message')
                return error_message

    def get_email_data(self, inbox_id) -> list:
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

        email_list = []
        with mailslurp_client.ApiClient(self.configuration) as api_client:
            inbox_controller = mailslurp_client.InboxControllerApi(api_client)
            email_controller = mailslurp_client.EmailControllerApi(api_client)
            emails = inbox_controller.get_emails(inbox_id=inbox_id)
            for email in emails:
                email_details = email_controller.get_email(email.id)
                email_dict = email.to_dict()
                email_dict['body'] = email_details.body
                email_list.append(email_dict)
            return email_list


if __name__ == '__main__':
    load_dotenv()
    api_key = os.getenv('API_KEY')
    client = MailGenerator(api_key)
    # id = client.create_email()
    # print(id + "@mailslurp.com")
    # input("Press Enter to continue...")
    print(client.get_email_data("70db6f58-2ff6-4b31-b461-2e84bd1f6f81"))
