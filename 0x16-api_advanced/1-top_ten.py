#!/usr/bin/python3
"""
Using Reddit API
"""

from requests import get


def top_ten(subreddit):
    """
    A function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    url = 'https://reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    response = get(url, headers=headers)
    results = response.json()

    try:
        data = results.get('data').get('children')
        for datii in data:
            print(datii.get('data').get('title'))
    except Exception:
        print("None")
