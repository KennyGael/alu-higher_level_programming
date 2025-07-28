#!/bin/bash
# Sends GET request to the URL with custom header
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
