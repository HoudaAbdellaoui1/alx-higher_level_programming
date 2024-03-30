#!/usr/bin/python3
"""Display response body """

import sys
import urllib.request
import urllib.parse
if __name__ == '__main__':
    with urllib.request.Request(sys.argv[1]) as req:
        try:
            resp = urllib.request.urlopen(req).read()
            print(resp.decode('utf-8'))
        except urllib.error.HTTPError as e:
            print('Error code: ', e.code)
