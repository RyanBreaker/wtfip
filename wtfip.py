#!/usr/local/bin/python3

import json, requests, sys

url = 'https://wtfismyip.com/json'
response = None

try:
    response = requests.get(url)
except requests.ConnectionError:
    # Fail elegantly if the server can't be reached
    print('Connection failed, check your internet connection.')
    sys.exit(1)

ip = json.loads(response.content)

print(ip['YourFuckingIPAddress'])
