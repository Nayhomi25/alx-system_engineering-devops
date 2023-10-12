#!/usr/bin/python3
""" Defines recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit
"""
import requests


def add_title(hot_list, posts):
    """ Adds item into a list """
    if len(posts) == 0:
        return
    hot_list.append(posts[0]['data']['title'])
    posts.pop(0)
    add_title(hot_list, posts)


def recurse(subreddit, hot_list=[], after="", count=0):
    """Queries the Reddit API and returns a list containing the titles of all
       hot articles for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59'
    }
    params = {'after': after,
              'count': count,
              'limit': 100
              }
    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        count += data.get('data').get('dist')
        add_title(hot_list, data['data']['children'])
        if not data['data']['after']:
            return hot_list
        else:
            return recurse(subreddit,
                           hot_list,
                           data['data']['after'],
                           count)
    else:
        return None
