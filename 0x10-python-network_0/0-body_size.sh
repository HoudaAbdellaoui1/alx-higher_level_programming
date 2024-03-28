#!/bin/bash
# Display response body size
echo $(curl -sI "$1" | grep -i '^Content-Length:' | awk '{print $2}')