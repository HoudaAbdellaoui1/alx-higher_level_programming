#!/usr/bin/python3
"""POST Credentials to get github id"""

import requests
import sys
if __name__ == '__main__':
    username = sys.argv[1]
    pwd = sys.argv[2]

    url = 'https://api.github.com/user'
    auth = requests.auth.HTTPBasicAuth(username, pwd)
    r = requests.get(url, auth=auth)
    print(r.json().get('id'))
