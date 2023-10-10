#!/usr/bin/python3
"""Task 2: Recurse it!"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """Queries the Reddit API and returns all hot posts
    of the subreddit"""

    info = requests.get("https://www.reddit.com/r/{}/hot.json"
                        .format(subreddit),
                        params={"count": count, "after": after},
                        headers={"User-Agent": "My-User-Agent"},
                        allow_redirects=False)

    if info.status_code >= 400:
        return None

    hot_articles = hot_list + [child.get("data").get("title")
                               for child in info.json()
                               .get("data")
                               .get("children")]

    if not info.json().get("data").get("after"):
        return hot_articles

    return recurse(subreddit, hot_articles, info.json().get(
        "data").get("count"), info.json().get("data").get("after"))
