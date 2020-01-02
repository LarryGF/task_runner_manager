import requests
import os
slack_url = os.getenv('SLACK_URL')
file = os.getenv('LOG_LOCATION')
lines = os.getenv('LINES')
with open(file) as file:
    data = file.read()
    data = data.split('\n')
    message = data[-lines:].join('/n')
response = requests.post(url=slack_url, headers={'Content-type': 'application/json'}, json={'text':message})
