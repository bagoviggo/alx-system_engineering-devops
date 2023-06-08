#!/usr/bin/python3
""" This module contains function that Queries the Reddit API
    that prints top 10 posts from reddit
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None

    Prints:
        The titles of the first 10 hot posts in the subreddit.

    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Alx-reddit/1.0"}  # Set a custom User-Agent header

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            posts = data["data"]["children"]

            for post in posts:
                title = post["data"]["title"]
                print(title)

        except KeyError:
            print("Invalid subreddit.")
    else:
        print("Invalid subreddit.")


if __name__ == "__main__":
    (top_ten(argv[1]))
