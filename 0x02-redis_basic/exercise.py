#!/usr/bin/env python3
"""
This module provides a class to store data in a Redis cache.
"""
from typing import Callable, Optional, Union
import uuid
import redis
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    A decorator that counts the number of times a method is called.

    Args:
        method: The method to count the calls for.

    Returns:
        The wrapped method.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function to count method calls.
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    A decorator that stores the history of the method calls.

    Args:
        method: The method to store the history for.

    Returns:
        The wrapped method.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function to store the method call history.
        """
        self._redis.rpush(f"{key}:inputs", str(args))
        res = method(self, *args, **kwargs)
        self._redis.rpush(f"{key}:outputs", str(res))
        return res

    return wrapper


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

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the data in the Redis cache.

        Args:
            data: The data to store.

        Returns:
            The key of the stored data
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

        Returns:
            The data from the Redis cache.
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

        Returns:
            The data from the Redis cache as a string.
        """
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """
        Retrieve the data from the Redis cache as an integer.

        Args:
            key: The key of the data to retrieve.

        Returns:
            The data from the Redis cache as an integer.
        """
        return self.get(key, int)


def replay(method: Callable) -> None:
    """
    Display the history of the method calls.

    Args:
        method: The method to display the history for.
    """
    key = method.__qualname__
    redis = method.__self__._redis
    inputs = redis.lrange(f"{key}:inputs", 0, -1)
    outputs = redis.lrange(f"{key}:outputs", 0, -1)

    print(f"{key} was called {redis.get(key).decode()} times:")

    for i, o in zip(inputs, outputs):
        print(f"{key}(*{i.decode()}) -> {o.decode()}")
