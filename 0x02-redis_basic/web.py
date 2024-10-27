#!/usr/bin/env python3
"""
This module provides a function to fetch and cache web pages using Redis.

Functions:
    get_page(url: str) -> str:
        Fetches the content of the given URL. If the content is cached in\
            Redis, it returns the cached content. Otherwise, it fetches the\
                content from the web, caches it in Redis for 10 seconds, and\
                    then returns it.
"""
import redis
import requests

cache = redis.Redis()


def get_page(url: str) -> str:
    """
    Fetches the content of a given URL, utilizing a cache to store and\
        retrieve the content.

    If the content of the URL is found in the cache, it is returned directly.\
        Otherwise, the content is fetched from the URL, stored in the cache\
            with an expiration time of 10 seconds, and then returned.

    Args:
        url (str): The URL of the page to fetch.

    Returns:
        str: The content of the page.
    """
    res = cache.get(url)
    if res:
        return res.decode("utf-8")
    res = requests.get(url).text
    print("Fetched")
    cache.setex(url, 10, res)
    return res
