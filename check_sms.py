from twilio.rest import Client
import os
from dotenv import load_dotenv 
load_dotenv()

auth_token = os.getenv('auth_token')
account_sid = os.getenv('account_sid')
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hi there!',
                              from_='+18583485215',
                              to='+79057808650'
                          )

print(message.sid)
