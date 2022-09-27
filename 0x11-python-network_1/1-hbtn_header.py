#!/usr/bin/python3
"""sends a request to url given and prints header parameter X-Request-Id"""

import urllib.request
import sys

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        print(response.headers["X-Request-Id"])
