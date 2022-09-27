#!/usr/bin/python3
"""sends request and handles http errors"""

import urllib.request
from urllib.error import HTTPError
import sys

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])

    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as err:
        print(f"Error code: {err.code}")
