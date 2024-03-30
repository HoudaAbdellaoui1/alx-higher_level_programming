#!/usr/bin/python3
"""Fetch alx intranet resource"""

if __name__ == '__main__':
    import urllib.request
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        the_page = response.read()
    print("""Body response:
            - type : {}
            - content : {}
            - utf8 content : {}"""
          .format(type(the_page), the_page, the_page.decode('utf-8')))
