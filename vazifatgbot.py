# https://core.telegram.org/bots/api#sendmessage
import requests
token = "8791160751:AAFAxS-vflirjyAzgIdVay1jEdICSRfv3_E"
method = 'forwardMessage'
response = requests.post(
        url=f'https://api.telegram.org/bot{token}/{method}',
        data={'chat_id': 6667845769, 'from_chat_id':7813037554, 'message_id':2}
    ).json()
print(response)

token = 8791160751:'AAFAxS-vflirjyAzgIdVay1jEdICSRfv3_E'
method = 'copyMessage'
response = requests.post(
        url=f'https://api.telegram.org/bot{token}/{method}',
        data={'chat_id': 392330197, 'from_chat_id': , 'message_id': }
    ).json()
print(response)


token = "8791160751:AAFAxS-vflirjyAzgIdVay1jEdICSRfv3_E"
url = f'https://telegram.org{token}/sendPhoto'
photo_path = r'C:\Users\user\Downloads\bird.jpg'

with open(photo_path, 'rb') as photo_file:
    payload = {
        'chat_id': 6667845769,
        'caption': 'I like Birds'
    }
    files = {
        'photo': photo_file
    }

    response = requests.post(url, data=payload, files=files).json()
print(response)


token = "8791160751:AAFAxS-vflirjyAzgIdVay1jEdICSRfv3_E"
method = 'sendLocation'
response = requests.post(
        url=f'https://api.telegram.org/bot{token}/{method}',
        data={'chat_id': 6667845769, 'latitude':41.40522104012209 , 'longatitude':60.49919723566515 }
    ).json()
print(response)
