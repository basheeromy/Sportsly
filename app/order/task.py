"""
Tasks from order app.
"""

from app.celery import app
import base64
import os
import google.auth
from email.message import EmailMessage
from email.mime.text import MIMEText
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

@app.task
def send_order_details(
    product,
    quantity,
    shipping_address,
    billing_address,
    user
):
    credentials_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    'sportsly-313208-9768d32de554.json')
    credentials = service_account.Credentials.from_service_account_file(
        credentials_path,
        scopes=['https://www.googleapis.com/auth/gmail.send']
    )
    #creds, _ = google.auth.default()
    try:
        service = build('gmail', 'v1', credentials=credentials)
        message = EmailMessage()

        message.set_content("This is a test email from sportsly app.")
        message['To'] = 'arunk.aru1@gmail.com'
        message['From'] = 'basheerkomassery@gmail.com'
        message['Subject'] = 'Test'

        # Encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode("utf-8")

        create_message = {
            'raw': encoded_message
        }

        # pylint: disable=E1101
        send_message = (service.users().messages().send(userId="me", body=create_message).execute())

        print(f'Message Id: {send_message["id"]}')
    except HttpError as error:
        print(f"An error occured: {error}")
        send_message = None

    return send_message

if __name__ == '__main__':
    send_order_details()
