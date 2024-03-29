#!/bin/bash
# send request and extract status code
curl -s -o /dev/null -w "%{http_code}" "$1"
