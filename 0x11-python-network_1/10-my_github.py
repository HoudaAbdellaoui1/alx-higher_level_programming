#!/usr/bin/python3
"""POST Credentials to get github id"""

import requests
import sys
if __name__ == '__main__':
    username = sys.argv[1]
    # username = 'HoudaAbdellaoui1'
    pwd = sys.argv[2]
    # pwd = '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'
    url = '  https://api.github.com/users'
    payload = {'USERNAME': username}
    headers = {'Authorization' : ('Bearer {}'.format(pwd))}
    r = requests.get(url, params= payload, headers=headers)
    print(r.json()[0].get('id'))
