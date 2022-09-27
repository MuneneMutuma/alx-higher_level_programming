#!/usr/bin/python3
"""sends post request and prints response body"""

import urllib.request as request
import urllib.parse as parse
import sys

if __name__ == "__main__":
    req = request.Request(sys.argv[1])
    data = parse.urlencode({"email": f"{sys.argv[2]}"}).encode()
    with request.urlopen(req, data=data) as response:
        print(response.read().decode("utf-8"))
