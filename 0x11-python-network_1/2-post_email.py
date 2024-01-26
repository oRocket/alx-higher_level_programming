#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys

if len(sys.argv) == 3:
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    request = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(request) as response:
        content = response.read().decode('utf-8')
        print(content)
else:
    print("Usage: ./2-post_email.py <URL> <email>")
