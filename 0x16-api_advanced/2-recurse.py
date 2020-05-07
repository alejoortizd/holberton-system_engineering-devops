#!/usr/bin/python3
"""
Return the list of all hot posts
"""

import requests
from sys import argv


def recurse(subreddit, hot_list=[], after=''):
    """Function that returns the list of all hot posts"""
    if after is None:
        return []
    headers = {"User-Agent":
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                AppleWebKit/537.36 (KHTML, like Gecko)\
                Chrome/70.0.3538.77 Safari/537.36"}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if after:
        url += '?limit=100&after={}'.format(after)
    req = requests.get(url, headers=headers, allow_redirects=False)
    if str(req) != '<Response [200]>':
        return None
    else:
        rj = req.json()
        posts = rj.get('data', {}).get('children', None)
        for post in posts:
            hot_list.append(post.get('data', {}).get('title', None))
        return hot_list + recurse(subreddit, [], rj.get('data').get('after'))
