#!/usr/bin/env python3
"""
Cache module
"""
import redis
import uuid
from typing import Union

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
