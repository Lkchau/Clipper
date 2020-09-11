import os
import twitch
import requests
import sys
import json
from dotenv import load_dotenv


load_dotenv()
TWITCH_CLIENT_ID = os.getenv('TWITCH_CLIENT_ID')
BASE_URL = os.getenv('TWITCH_URL')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
HEADERS = {'Client-ID': TWITCH_CLIENT_ID, 'Authorization': ACCESS_TOKEN}
INDENT = 2

def get_response(query):
    url = BASE_URL + query
    response = requests.get(url, headers = HEADERS)
    return response

def print_response(response):
    response_json = response.json()
    print_response = json.dumps(response_json, indent= INDENT)
    print(print_response)

# get the current live stream info, given a username
def get_user_streams_query(user_login):
  return 'streams?user_login={0}'.format(user_login)

def get_user_query(user_login):
  return 'users?login={0}'.format(user_login)

def get_user_videos_query(user_id):
  return 'videos?user_id={0}&first=50'.format(user_id)

def get_clips_query(user_id):
  return 'clips?broadcaster_id={0}&first=5'.format(user_id)