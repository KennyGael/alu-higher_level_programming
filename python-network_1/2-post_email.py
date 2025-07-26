#!/usr/bin/python3
"""Sends POST request with email param and displays response"""
import urllib.request
import urllib.parse
import sys

url = sys.argv[1]
value = {'email': sys.argv[2]}
data = urllib.parse.urlencode(value).encode('ascii')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    print(response.read().decode('utf-8'))
