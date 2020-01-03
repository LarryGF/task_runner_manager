#!/usr/bin/env python3
import requests
import os
slack_url = os.getenv('SLACK_URL')
devops_url = os.getenv('SLACK_DEVOPS')
logs = os.getenv('LOG_LOCATION')
# lines = int(os.getenv('LINES'))
lines = 5
with open(logs) as file:
    data = file.read()
    data = data.split('\n')
    message = '\n'.join(data[-lines:])
attachments = [
    {
        "pretext": logs,
        "title": "Log contents",
        "text": message,
        "color": "#7CD197"
    }
]
response = requests.post(url=slack_url, headers={
                         'Content-type': 'application/json'}, json={'attachments': attachments})
response2 = requests.post(url=devops_url, headers={
    'Content-type': 'application/json'}, json={'attachments': attachments})
