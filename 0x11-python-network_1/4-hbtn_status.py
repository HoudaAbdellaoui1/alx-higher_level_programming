#!/usr/bin/python3
"""Fetch resource using requests package"""

import requests
if __name__ == '__main__':
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print("""Body response:
            - type : {}
            - content : {}"""
          .format(type(r), r.content))
