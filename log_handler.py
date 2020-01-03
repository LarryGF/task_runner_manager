#!/usr/bin/env python3
import requests
import os
slack_url = os.getenv('SLACK_URL')
file = os.getenv('LOG_LOCATION')
lines = int(os.getenv('LINES'))
with open(file) as file:
    data = file.read()
    data = data.split('\n')
    message = '\n'.join(data[-lines:])
attachments = [
    {
        "pretext": file,
        "title": "Log contents",
        # "title_link": "https://groove.hq/path/to/ticket/1943",
        "text": message,
        "color": "#7CD197"
    }
]
response = requests.post(url=slack_url, headers={
                         'Content-type': 'application/json'}, json={'attachments': attachments})
