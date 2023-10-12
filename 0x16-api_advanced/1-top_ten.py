#!/usr/bin/python3
"""script for parsing web data from an api
"""
import json
import requests
import sys


def top_ten(subreddit):
    """api call to reddit to get the number of subscribers
    """
    base_url = 'https://www.reddit.com/r/'
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59'
    }
    # grab info about all users
    url = base_url + '{}/top/.json?count=10'.format(subreddit)
    response = requests.get(url, headers=headers)
    resp = json.loads(response.text)

    try:
        # grab the info about the users' tasks
        data = resp.get('data')
        children = data.get('children')
    except Exception as ex:
        print('None')
    if children is None or data is None or len(children) < 1:
        print('None')

    for i, post_dict in enumerate(children):
        if i == 10:
            break
        print(post_dict.get('data').get('title'))
