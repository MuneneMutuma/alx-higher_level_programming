#!/usr/bin/env bash
#takes in URL sends a request to that url, and displays the size of the body of the response

curl -so /dev/null 0.0.0.0:5000 -w '%{size_download}\n'
