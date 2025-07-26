#!/usr/bin/python3
"""Displays value of X-Request-Id from response header using requests"""
import requests
import sys

r = requests.get(sys.argv[1])
print(r.headers.get("X-Request-Id"))
