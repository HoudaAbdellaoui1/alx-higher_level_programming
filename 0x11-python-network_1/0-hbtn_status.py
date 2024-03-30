#!/usr/bin/python3
"""Fetch alx intranet resource"""

if __name__ == '__main__':
    import urllib.request
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        the_page = response.read()
    print("""Body response:\n\t- type : {}\n\t- content : {}\n\t- utf8 content : {}"""
          .format(type(the_page), the_page, the_page.decode('utf-8')))
