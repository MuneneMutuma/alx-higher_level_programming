#!/bin/bash
# a Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -sfL -X POST -d @"$2" --header "Content-Type: application/json" "$1"
