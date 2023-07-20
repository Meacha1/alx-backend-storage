#!/usr/bin/env python3
"""
web.py - Get Page with Caching
"""
import requests
import redis
import time

def get_page(url: str) -> str:
    """
    Fetches the HTML content of a URL and caches the result with an expiration time of 10 seconds.

    Args:
        url (str): The URL to fetch the HTML content from.

    Returns:
        str: The HTML content of the URL.
    """
    cache_key = f"count:{url}"

    # Connect to Redis
    redis_client = redis.Redis()

    # Increment the access count for the URL
    redis_client.incr(cache_key)

    # Get the access count and set the expiration time to 10 seconds
    access_count = int(redis_client.get(cache_key) or 0)
    redis_client.expire(cache_key, 10)

    # Fetch the HTML content of the URL using requests
    response = requests.get(url)

    return f"Access Count: {access_count}, Content: {response.text}"


if __name__ == "__main__":
    # Test the get_page function with a sample URL
    url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://example.com"
    print(get_page(url))
