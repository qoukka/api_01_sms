import time
import os
from dotenv import load_dotenv 
import requests
from twilio.rest import Client

load_dotenv()

def get_status(user_id):
    params = {
        'user_ids': user_id,
        'access_token': os.getenv('vk_token'),
        'fields': 'online',
        'v': '5.92'
    }
    online_status = requests.post("https://api.vk.com/method/users.get", params=params)
    return online_status.json()["response"][0]["online"]


def sms_sender(sms_text):
    auth_token = os.getenv('auth_token')
    account_sid = os.getenv('account_sid')
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                              body=sms_text,
                              from_=os.getenv('NUMBER_FROM'),
                              to=os.getenv('NUMBER_TO')
                          )
    return message.sid


if __name__ == "__main__":
    vk_id = input("Введите id ")
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!\nHi, this is Big Brother, I know you are online now')
            break
        time.sleep(5)
