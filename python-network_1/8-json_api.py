#!/usr/bin/python3
"""Sends POST with letter param and parses JSON"""
import requests
import sys

q = "" if len(sys.argv) < 2 else sys.argv[1]
r = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})

try:
    json_data = r.json()
    if json_data:
        print("[{}] {}".format(json_data.get("id"), json_data.get("name")))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
