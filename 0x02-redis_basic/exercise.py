#!/usr/bin/env python3
"""
This module provides a class to store data in a Redis cache.
"""
from typing import Callable, Optional, Union
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
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the data in the Redis cache.

        Args:
            data: The data to store.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float]:
        """
        Retrieve the data from the Redis cache.

        Args:
            key: The key of the data to retrieve.
            fn: An optional function to apply to the data.
        """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        Retrieve the data from the Redis cache as a string.

        Args:
            key: The key of the data to retrieve.
        """
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """
        Retrieve the data from the Redis cache as an integer.

        Args:
            key: The key of the data to retrieve.
        """
        return self.get(key, int)
