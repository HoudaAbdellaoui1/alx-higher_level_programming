#!/usr/bin/python3
"""Fetch alx intranet resource"""

import urllib.request
req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
   the_page = response.read()