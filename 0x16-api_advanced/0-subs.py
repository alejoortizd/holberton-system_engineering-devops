#!/usr/bin/python3
"""
Return subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """Function that returns all subscribes"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    headers = {"User-Agent":
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                AppleWebKit/537.36 (KHTML, like Gecko)\
                Chrome/70.0.3538.77 Safari/537.36"}
    url = 'https://www.reddit.com/r/{}/about.json'
    req = requests.get(url.format(subreddit), headers=headers).json()
    subs = req.get("data", {}).get("subscribers", 0)
    return subs
