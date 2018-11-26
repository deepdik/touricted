from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# SCOPES = 'https://www.googleapis.com/auth/gmail.compose'

"""Send an email message from the user's account.
"""
import base64
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mimetypes
import os

from apiclient import errors


class send_email:
    def __init__(self,service):
        self.service = service

    def SendMessage(self, user_id, message):

        try:
            message = (self.service.users().messages().send(userId=user_id, body=message).execute())
            print( 'Message Id: %s' % message['id'])
            return message
        except errors.HttpError as error:
            print('An error occurred: %s' % error)


    def CreateMessage(self,sender, to, subject, message_text):
        message = MIMEText(message_text,'html')
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        
        return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

    def CreateMessageWithAttachment(self,sender, to, subject, message_text, file_dir,filename):

      message = MIMEMultipart()
      message['to'] = to
      message['from'] = sender
      message['subject'] = subject


      msg = MIMEText(message_text)
      message.attach(msg)

      path = os.path.join(file_dir, filename)
      content_type, encoding = mimetypes.guess_type(path)

      if content_type is None or encoding is not None:
        content_type = 'application/octet-stream'
      main_type, sub_type = content_type.split('/', 1)
      if main_type == 'text':
        fp = open(path, 'rb')
        msg = MIMEText(fp.read(), _subtype=sub_type)
        fp.close()
      elif main_type == 'image':
        fp = open(path, 'rb')
        msg = MIMEImage(fp.read(), _subtype=sub_type)
        fp.close()
      elif main_type == 'audio':
        fp = open(path, 'rb')
        msg = MIMEAudio(fp.read(), _subtype=sub_type)
        fp.close()
      else:
        fp = open(path, 'rb')
        msg = MIMEBase(main_type, sub_type)
        msg.set_payload(fp.read())
        fp.close()

      msg.add_header('Content-Disposition', 'attachment', filename=filename)
      message.attach(msg)

      return {'raw': base64.urlsafe_b64encode(message.as_bytes().decode())}
