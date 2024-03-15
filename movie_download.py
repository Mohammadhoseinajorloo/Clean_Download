from telethon.sync import TelegramClient, events


api_id = 0
api_hash = 0 


with TelegramClient('name', api_id, api_hash) as client:
       client.send_message('me', 'Hello, myself!')
          print(client.download_profile_photo('me'))
