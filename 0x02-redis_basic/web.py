#!/usr/bin/env python3
"""
web.py - Get Page with Caching
"""
import redis
import requests
import time
from functools import wraps

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
        def wrapper(*args, **kwargs):
            key = f"cache:{func.__name__}:{args}"
            result = redis_client.get(key)
            if result is None:
                result = func(*args, **kwargs)
                redis_client.setex(key, expiration_time, result)
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

# Example usage
if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/1000/url/https://www.example.com"
    for i in range(5):
        content = get_page(url)
        print(f"Access {i + 1}: {content}")

    access_count = redis_client.get(f"count:{url}")
    print(f"Number of accesses for {url}: {int(access_count)}")
