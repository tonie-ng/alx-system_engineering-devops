#!/usr/bin/python3
"""
queries the Reddit API
"""
import requests


def top_ten(subreddit):
    """
    Gets the first 10 hot posts
    - If not a valid subreddit, print None.
    """
    req = requests.get(
            f"https://www.reddit.com/r/{subreddit}/about.json",
            headers={
                "User-Agent": "Mozilla/10.0/API"
                },
            allow_redirects=False,
            params={"limit": 10},
            )

    if req.status_code == 200:
        for get_data in req.json().get("data").get("children"):
            info = get_data.get("data")
            title = info.get("title")
            print(title)
    else:
        print(None)
