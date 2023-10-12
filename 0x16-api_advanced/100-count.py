#!/usr/bin/python3
""" Defines a recursive function that queries the Reddit API, parses the title
    of all hot articles, and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces.
"""
import requests
import re


def add_title(hot_list, posts):
    """ Adds item into a list """
    if len(posts) == 0:
        return
    hot_list.append(posts[0]['data']['title'])
    posts.pop(0)
    add_title(hot_list, posts)


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """Queries the Reddit API, parses the title of all hot articles, and prints
       a sorted count of given keywords (case-insensitive, delimited by spaces
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59'
    }
    params = {
              'after': after,
              'count': count,
              'limit': 100
              }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        results = data.get("data")
        after = results.get("after")
        count += results.get("dist")
        for i in results.get("children"):
            title = i.get("data").get("title").lower().split()
            for word in word_list:
                if word.lower() in title:
                    times = len([t for t in title if t == word.lower()])
                    if instances.get(word) is None:
                        instances[word] = times
                    else:
                        instances[word] += times

        if after is None:
            if len(instances) == 0:
                print("")
                return
            instances = sorted(instances.items(),
                               key=lambda kv: (-kv[1],
                                               kv[0]))
            [print("{}: {}".format(k, v)) for k, v in instances]
        else:
            count_words(subreddit, word_list, instances, after, count)
    else:
        print("")
