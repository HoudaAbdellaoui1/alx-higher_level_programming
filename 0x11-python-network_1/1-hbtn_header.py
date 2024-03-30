#!/usr/bin/python3
"""Fetch and display header value"""

import sys
import urllib.request
if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as response:
        the_page = response
    print(dict(the_page.headers).get('X-Request-Id'))
