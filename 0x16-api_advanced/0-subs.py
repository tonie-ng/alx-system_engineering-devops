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
            "https://www.reddit.com/r/{}/about.json".format(subreddit),
            headers={
                "User-Agent": "Custom",
                },
            allow_redirects=False,
            )
    if res.status_code == 200:
        return res.json().get("data").get("subscribers")
    return 0
