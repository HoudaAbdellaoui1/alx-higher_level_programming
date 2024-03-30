#!/usr/bin/python3
"""POST Request with email param"""

import sys
import urllib.request
import urllib.parse
if __name__ == '__main__':
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
    print(the_page.decode('utf-8'))
