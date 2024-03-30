#!/usr/bin/python3
"""POST Credentials to get github id"""

import requests
import sys
if __name__ == '__main__':
    username = sys.argv[1]
    pwd = sys.argv[2]
    url = 'https://api.github.com/users'
    payload = {'USERNAME': username}
    headers = {'Authorization' : ('Bearer {}'.format(pwd))}
    r = requests.get(url, params= payload, headers=headers)
    print(r.json())
    print(r.json()[0].get('id'))
