# from twitchAPI.twitch import Twitch
# from twitchAPI.webhook import TwitchWebHook
# from dotenv import load_dotenv
# import os
# from uuid import UUID
# from pprint import pprint


# load_dotenv()
# TWITCH_CLIENT_ID = os.getenv('TWITCH_CLIENT_ID')
# TWITCH_SECRET = os.getenv('TWITCH_SECRET')

# twitch = Twitch(TWITCH_CLIENT_ID, TWITCH_SECRET)
# twitch.authenticate_app([])
# # BASE_URL = os.getenv('TWITCH_URL')
# hook = TwitchWebHook("  ", TWITCH_CLIENT_ID, 8080)
# hook.authenticate(twitch.get_app_token())

# def callback_user_changed(uuid: UUID, data: dict) -> None:
#     print(f'Callback for UUID {str(uuid)}')
#     pprint(data)

# success, sub_uuid = hook.subscribe_user_changed(user_id, callback_user_changed)
# hook.start()

import requests
import json
import os
from dotenv import load_dotenv
from flask import request
from flask import Flask

CLIENT_ID = os.getenv('TWITCH_CLIENT_ID')
OAUTH_TOKEN = os.getenv('ACCESS_TOKEN')
MY_SECRET = os.getenv('TWITCH_SECRET')

app = Flask(__name__)

@app.route('/my_webhook/<user_id>')
def my_webhook(user_id):
    # check_secret(request) # sha256 of your secret and content-length
    print(user_id)
    data = request.get_json()['data']
    if len(data) > 0:
       your_bot.user_is_live(data)
    else:
       your_bot.user_is_offline(data)
    return 'OK'

def subscribe_to_webhook(user_id):
    endpoint = 'https://api.twitch.tv/helix/webhooks/hub'
    topic = 'https://api.twitch.tv/helix/streams'
    my_headers = {
        'Client-ID': CLIENT_ID,
        'Authorization': f'Bearer {OAUTH_TOKEN}'
    }
    payload = {
        'hub.callback': f'http://my_server.url/my_webhook/{user_id}',
        'hub.mode': 'subscribe',
        'hub.topic': f'{topic}?user_id={user_id}',
        'hub.lease_seconds': 864000,
        'hub.secret': MY_SECRET
    }
    response = requests.post(endpoint, headers=my_headers, data=json.dumps(payload))
    return response.ok

# import web

# urls = ('/.*', 'hooks')

# app = web.application(urls, globals())


# class hooks:

#     def POST(self):
#         data = web.data()
#         print("")
#         print('DATA RECEIVED:')
#         print(data)
#         print("")

#         return 'OK'

#     def GET(self):
#         try:
#             data = web.input()
#             data = data['hub.challenge']
#             print("Hub challenge: ", data)
#             return data
#         except KeyError:
#             return web.BadRequest


if __name__ == '__main__':
    app.run()