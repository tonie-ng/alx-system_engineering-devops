#!/usr/bin/python3
"""
returns the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Sends a rrequest to the Reddit api
    Returns: 0 if no valuid subreddit
    """
    res = requests.get(
            f"https://www.reddit.com/r/{subreddit}/about.json",
            headers={
                "User-Agent": "Mozilla/5.0",
                },
            allow_redirects=False,
            )
    if res.status_code == 200:
        return res.json().get("data").get("subscribers")
    return 0
