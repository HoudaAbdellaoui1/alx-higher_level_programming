#!/usr/bin/python3
"""POST request with letter param"""

import requests
import sys
if __name__ == '__main__':
    if len(sys.argv) == 1:
        param = ""
    else:
        param = sys.argv[1]
    r = requests.post(sys.argv[1], data={'q': param})
    try:
        response = r.json()
        if response:
            print("[{}] {}".format(response.get('id'),response.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
