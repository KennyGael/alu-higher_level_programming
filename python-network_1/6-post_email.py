#!/usr/bin/python3
"""Sends POST request with email using requests"""
import requests
import sys

data = {'email': sys.argv[2]}
r = requests.post(sys.argv[1], data=data)
print(r.text)
