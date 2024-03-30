#!/usr/bin/python3
"""
Fetches a URL and displays its response body.

Usage: ./3-error_code.py <URL>
"""
import sys
from urllib import request, error


if __name__ == '__main__':
    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPError as e:
        print('Error code:', e.code)
