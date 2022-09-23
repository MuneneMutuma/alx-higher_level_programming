#!/bin/bash
#takes in URL sends a request to that url, and displays the size of the body of the response
curl -so /dev/null "$1" -w '%{size_download}\n'
