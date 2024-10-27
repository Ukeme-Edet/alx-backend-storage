#!/usr/bin/env python3
"""
Web module
"""
import requests
import redis
from functools import wraps
from typing import Callable

r = redis.Redis()


def cache_with_expiry(expiry: int):
    """
    Cache with expiry decorator

    Args:
        expiry (int): expiry time in seconds

    Returns:
        Callable: decorator
    """

    def decorator(func: Callable):
        @wraps(func)
        def wrapper(url: str) -> str:
            cached_content = r.get(url)
            if cached_content:
                r.incr(f"count:{url}")
                return cached_content.decode("utf-8")
            content = func(url)
            r.setex(url, expiry, content)
            r.incr(f"count:{url}")
            return content

        return wrapper

    return decorator


@cache_with_expiry(10)
def get_page(url: str) -> str:
    """
    Get page

    Args:
        url (str): url

    Returns:
        str: page content
    """
    response = requests.get(url)
    return response.text
