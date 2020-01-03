#!/usr/bin/env python3
import requests
import os
slack_url = os.getenv('SLACK_URL')
file = os.getenv('LOG_LOCATION')
lines = int(os.getenv('LINES'))
with open(file) as file:
    data = file.read()
    data = data.split('\n')
    message = '/n'.join(data[-lines:])
response = requests.post(url=slack_url, headers={
                         'Content-type': 'application/json'}, json={'text': message})
