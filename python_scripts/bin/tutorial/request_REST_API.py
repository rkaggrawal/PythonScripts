#!/usr/bin/python

import requests

ro = requests.get('https://developer.github.com/v3/activity/events/')

print ro.url
# print ro.text
# print ro.json

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)