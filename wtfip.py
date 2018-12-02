#!/usr/local/bin/python3

import json, requests, sys

url = 'https://wtfismyip.com/json'
r = None

try:
    r = requests.get(url)
except requests.ConnectionError:
    # Fail elegantly if the server can't be reached
    print('Connection failed, check your internet connection.')
    sys.exit(1)

ip = json.loads(r.content)

print(ip['YourFuckingIPAddress'])
