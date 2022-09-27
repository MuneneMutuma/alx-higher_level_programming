#!/usr/bin/python3
"""sends post request and prints response body"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    data = urllib.parse.urlencode({"email": f"{sys.argv[2]}"}).encode()
    with urllib.request.urlopen(req, data=data) as response:
        print(urllib.response.read().decode("utf-8"))
