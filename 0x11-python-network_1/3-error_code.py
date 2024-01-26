#!/usr/bin/python3
import urllib.request
import urllib.error
import sys

if len(sys.argv) == 2:
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            print(content)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
else:
    print("Usage: ./3-error_code.py <URL>")
