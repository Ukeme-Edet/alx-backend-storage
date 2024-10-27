#!/usr/bin/env python3
"""
This module provides a class to store data in a Redis cache.
"""
from typing import Union
import uuid
import redis


class Cache:
    """
    A class to store data in a Redis cache.
    """

    def __init__(self) -> None:
        """
        Initialize the Redis connection.
        """
        self._redis = redis.Redis()

    def store(self, data: Union[str, bytes, int, float]) -> None:
        """
        Store the data in the Redis cache.

        Args:
            data: The data to store.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
