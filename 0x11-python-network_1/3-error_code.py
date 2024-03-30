#!/usr/bin/python3
"""Display response body """

import sys
import urllib.request
import urllib.parse
if __name__ == '__main__':
    req = urllib.request.Request(sys.argv[1])
    try:
        urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read())
    # print(the_page.decode('utf-8'))
