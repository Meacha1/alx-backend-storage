#!/usr/bin/env python3
"""
Cache module
"""
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps

class Cache:
    """
    Cache class to store data in Redis
    """

    def __init__(self) -> None:
        """
        Initializes the Cache instance with a Redis client
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the input data in Redis using a random key

        Args:
            data (Union[str, bytes, int, float]): The data to be stored

        Returns:
            str: The random key used for storing the data
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[[bytes], Union[str, int, float]]] = None) -> Union[str, int, float, bytes]:
        """
        Retrieves data from Redis using the provided key and applies the optional conversion function (fn).

        Args:
            key (str): The key used to retrieve the data from Redis.
            fn (Optional[Callable[[bytes], Union[str, int, float]]]): An optional conversion function to apply to the retrieved data.

        Returns:
            Union[str, int, float, bytes]: The retrieved data, optionally converted by the conversion function (fn).
        """
        data = self._redis.get(key)
        if data is None:
            return data
        return fn(data) if fn else data

    def get_str(self, key: str) -> Union[str, None]:
        """
        Retrieves data from Redis using the provided key and converts it to a UTF-8 string.

        Args:
            key (str): The key used to retrieve the data from Redis.

        Returns:
            Union[str, None]: The retrieved data as a UTF-8 string or None if the key does not exist.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """
        Retrieves data from Redis using the provided key and converts it to an integer.

        Args:
            key (str): The key used to retrieve the data from Redis.

        Returns:
            Union[int, None]: The retrieved data as an integer or None if the key does not exist.
        """
        return self.get(key, fn=int)

def count_calls(method: Callable) -> Callable:
    """
    Decorator to count how many times a method is called.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The decorated method.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

# Decorate the Cache.store method with count_calls
Cache.store = count_calls(Cache.store)
