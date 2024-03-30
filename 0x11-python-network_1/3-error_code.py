#!/usr/bin/python3
"""
Fetches a URL and displays its response body.

Usage: ./3-error_code.py <URL>
"""
import sys
import urllib.request


if __name__ == '__main__':
    try:
        with urllib.request.Request(sys.argv[1]) as req:
            resp = urllib.request.urlopen(req).read()
            print(resp.decode('UTF-8'))
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
