#!/usr/bin/python3
""" This module contains function that Recursively queries the Reddit API
    and returns a list containing the titles of all
    hot articles for a given subreddit. 
"""

import requests

def recurse(subreddit, hot_list=None):
    """
    Recursively queries the Reddit API

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the titles of hot articles (default: None).

    Returns:
        list: A list containing the titles of all hot articles for the given subreddit.
              Returns None if no results are found or if the subreddit is invalid.

    """

    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "Alx-r/1.0"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            posts = data["data"]["children"]

            if not posts:
                return hot_list

            for post in posts:
                title = post["data"]["title"]
                hot_list.append(title)


            return recurse(subreddit, hot_list)

        except KeyError:
            return None
    else:
        return None
