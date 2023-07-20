#!/usr/bin/env python3
'''
Web Tools Module - Caching and Request Tracking Utilities
'''
import redis
import requests
import time
from functools import wraps
from typing import Callable

# Create a Redis client
redis_client = redis.Redis()

def caching_decorator(expiration_time: int):
    """
    Caching decorator to cache the function results with an expiration time.

    Args:
        expiration_time (int): The time in seconds for which the result should be cached.

    Returns:
        Callable: The wrapped function that caches the results.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(url: str) -> str:
            """
            Wrapper function for caching and tracking the number of accesses.

            Args:
                url (str): The URL to fetch the HTML content from.

            Returns:
                str: The HTML content of the URL.
            """
            # Increment the number of accesses for the URL
            redis_client.incr(f'count:{url}')

            # Check if the result is already cached
            result = redis_client.get(f'result:{url}')
            if result:
                return result.decode('utf-8')

            # Fetch the HTML content if not cached, and store it in Redis with an expiration time
            result = func(url)
            redis_client.setex(f'result:{url}', expiration_time, result)

            return result
        return wrapper
    return decorator

@caching_decorator(expiration_time=10)
def get_page(url: str) -> str:
    """
    Fetches the HTML content of a particular URL and returns it.

    Args:
        url (str): The URL to fetch the HTML content from.

    Returns:
        str: The HTML content of the URL.
    """
    response = requests.get(url)
    return response.text
