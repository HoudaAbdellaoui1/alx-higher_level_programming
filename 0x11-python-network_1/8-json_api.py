#!/usr/bin/python3
"""POST request with letter param"""

import requests
import sys
if __name__ == '__main__':
    param = sys.argv[1] if len(sys.argv) > 1 else ""
    url = 'http://0.0.0.0:5000/search_user'
    r = requests.post(url, data={'q': param})
    try:
        res = r.json()
        if res:
            print("[{}] {}".format(res.get('id'), res.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
