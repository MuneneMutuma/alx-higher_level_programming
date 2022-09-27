#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/stats"""
from urllib import request

if __name__ == "__main__":
    req = request.Request("https://alx-intranet.hbtn.io/status")

    with request.urlopen(req) as response:
        page = response.read()
        print("Body response:")
        print(f"\t- type: {type(page)}")
        print(f"\t- content: {page}")
        print(f"\t- utf8 content: {page.decode('utf-8')}")
