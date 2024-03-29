#!/bin/bash
# send a POST request with specific data to trigger the desired response
curl -sL -X PUT "0.0.0.0:5000/catch_me" -d "user_id=98" -H "Content-Type: application/x-www-form-urlencoded"
