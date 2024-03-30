#!/usr/bin/python3
"""Display response body """

import sys
import urllib.request
import urllib.parse
if __name__ == '__main__':
    req = urllib.request.Request(sys.argv[1])
    try:
        resp = urllib.request.urlopen(req)
        print(resp.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: ', e.code)
    # print(the_page.decode('utf-8'))
