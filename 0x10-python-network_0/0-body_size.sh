#!/bin/bash
# Display response body size
curl -s "$1" | wc -c
