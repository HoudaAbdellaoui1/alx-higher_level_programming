#!/usr/bin/python3
"""Fetches and prints the 10 most recent commits of a repository."""

import requests
import sys
if __name__ == '__main__':
    repository = sys.argv[1]
    owner = sys.argv[2]

    url =  f'https://api.github.com/repos/{owner}/{repository}/commits'
    params = {'per_page': 10, 'page' : 1 }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        for c in response.json():
            sha = c['sha']
            author = c['commit']['author']['name']
            print(f'{sha}: {author}')
    else:
        print('Failed to fetch commits. Status code:', response.status_code)
