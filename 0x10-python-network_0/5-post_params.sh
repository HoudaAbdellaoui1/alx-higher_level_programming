#!/bin/bash
# send POST request with variables and get response body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
