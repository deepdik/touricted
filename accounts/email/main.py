from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from . import test
# If modifying these scopes, delete the file token.json.
SCOPES = 'https://mail.google.com/'
store = file.Storage('token.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('gmail', 'v1', http=creds.authorize(Http()))

"""Get a list of Labels from the user's mailbox.
"""
"""Send an email message from the user's account.
"""

class SendEmail():
    def send_email_varification_mail(to,subject,message):
        sendInst = test.send_email(service)
        message = sendInst.CreateMessage("dk5f95@gmail.com",to, subject, message)       
        sendInst.SendMessage("me", message)




