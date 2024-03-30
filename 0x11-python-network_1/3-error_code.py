#!/usr/bin/python3
"""
Fetches a URL and displays its response body.

Usage: fetch_url.py <URL>
"""
import sys
import urllib.request
import urllib.parse
if __name__ == '__main__':
    try:
        with urllib.request.Request(sys.argv[1]) as req:
            resp = urllib.request.urlopen(req).read()
            print(resp.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
