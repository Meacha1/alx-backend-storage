#!/usr/bin/env python3
'''
Web Tools Module - Caching and Request Tracking Utilities
'''
import redis
import requests

# Create a Redis client
redis_client = redis.Redis()

def get_page(url: str) -> str:
    """
    Fetches the HTML content of a particular URL and returns it.

    Args:
        url (str): The URL to fetch the HTML content from.

    Returns:
        str: The HTML content of the URL.
    """
    # Check if the result is already cached
    result = redis_client.get(f'cache:{url}')
    if result:
        return result.decode('utf-8')

    # Fetch the data if not cached, and store it in Redis with an expiration time of 10 seconds
    response = requests.get(url)
    result = response.text
    redis_client.setex(f'cache:{url}', 10, result)

    # Increment the number of requests made to the URL
    redis_client.incr(f'count:{url}')

    return result

# Example usage
if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/1000/url/https://www.example.com"
    for i in range(5):
        content = get_page(url)
        print(f"Access {i + 1}: {content}")

    access_count = redis_client.get(f"count:{url}")
    print(f"Number of accesses for {url}: {int(access_count)}")
