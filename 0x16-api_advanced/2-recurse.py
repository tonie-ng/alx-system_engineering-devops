#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    response = requests.get(
            f"https://www.reddit.com/r/{subreddit}/about.json",
            headers={
                "User-Agent": "Mozilla/10.0/API"
                },
            params={
                "after": after,
                "count": count,
                "limit": 100
                },
            allow_redirects=False,
            )

    if response.status_code != 200:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
