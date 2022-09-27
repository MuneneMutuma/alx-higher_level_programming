#!/usr/bin/python3
"""a Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)
"""

from urllib import request, parse
import sys

if __name__ == "__main__":
    req = request.Request(sys.argv[1])
    data = parse.urlencode({"email": f"{sys.argv[2]}"}).encode()
    with request.urlopen(req, data=data) as response:
        print(response.read().decode("utf-8"))
