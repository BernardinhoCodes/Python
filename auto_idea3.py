# Open Youtube when selected Youtuber Upload new content
# by bernardinho.codes

import urllib, json
from selenium import webdriver
import time


def grab_new_video():
    api_key = "whatever your api key is get it here: https://console.developers.google.com"
    channel_id = "UC-bFgwL_kFKLZA60AiB-CCQ"

    standard_video_url = 'https://www.youtube.com/watch?v='
    standard_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    url = standard_search_url + 'key={}&channelId={}&part=snippet,id&order=data&maxResults=1'.format(api_key,
                                                                                                     channel_id)
    inp = urllib.urloppen(url)
    resp = json.load(inp)

    vidID = resp['items'][0]['id']['videoId']

    video_exists = False
    with open('videoid.json', 'r') as json_file:
        data = json.load(json_file)
        if data['videoId'] != vidID:
            local_driver = webdriver.Firefox()
            local_driver.get(standard_video_url + vidID)
            video_exists = True

    if video_exists:
        with open('videoid.json', 'w') as json_file:
            data = {'videoId': vidID}
            json.dump(data, json_file)


try:
    while True:
        grab_new_video()
        time.sleep(10)
except KeyboardInterrupt:
    print('stopping')
