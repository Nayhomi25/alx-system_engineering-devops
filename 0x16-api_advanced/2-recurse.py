#!/usr/bin/python3
"""script for parsing web data from an api
"""
import json
import requests
import sys


def recurse(subreddit, hot_list=[]):
    """api call to reddit to get the number of subscribers
    """
    base_url = 'https://www.reddit.com/r/{}/top.json'.format(
        subreddit
    )
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59'
    }
    if len(hot_list) == 0:
        # grab info about all users
        url = base_url
    else:
        url = base_url + '?after={}_{}'.format(
            hot_list[-1].get('kind'),
            hot_list[-1].get('data').get('id')
        )
    response = requests.get(url, headers=headers)
    resp = json.loads(response.text)
    try:
        # grab the info about the users' tasks
        data = resp.get('data')
        children = data.get('children')
    except Exception as ex:
        return None
    if children is None or data is None or len(children) < 1:
        return hot_list
    hot_list.extend(children)
    return recurse(subreddit, hot_list)
