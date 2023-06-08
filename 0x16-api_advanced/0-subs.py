#!/usr/bin/python3
"""
 This module contains function that queries Reddit API
 and returns the number of subscriber
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    Args:
        subreddit: The name of the subreddit.

    Returns:
        The number of subscribers, or 0 if the subreddit is invalid.
  """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Alx-Reddit/1.0"}  # custom header

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            subscribers = data["data"]["subscribers"]
            return subscribers
        except KeyError:
            print("Key Doesnot exist in JSON")
            return 0
    else:
        return 0
