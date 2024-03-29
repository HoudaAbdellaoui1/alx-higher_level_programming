#!/bin/bash
# send POST request with file contents in the body and get response body
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
