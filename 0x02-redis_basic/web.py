#!/usr/bin/env python3
'''
Web Tools Module - Caching and Request Tracking Utilities
'''

import redis
import requests
from functools import wraps
from typing import Callable


# Redis instance for caching and tracking
redis_client = redis.Redis()

def cache_response(method: Callable) -> Callable:
    '''
    Caches the output of fetched data and tracks the number of requests made to a URL.
    '''
    @wraps(method)
    def wrapper(url) -> str:
        '''
        Wrapper function for caching the output and tracking the request.
        '''
        # Increment the number of requests made to the URL
        redis_client.incr(f'count:{url}')

        # Check if the result is already cached
        result = redis_client.get(f'result:{url}')
        if result:
            return result.decode('utf-8')

        # Fetch the data if not cached, and store it in Redis with an expiration time of 10 seconds
        result = method(url)
        redis_client.set(f'count:{url}', 0)
        redis_client.setex(f'result:{url}', 10, result)

        return result

    return wrapper


@cache_response
def get_page(url: str) -> str:
    '''
    Fetches the content of a URL and returns it, caching the response and tracking the request count.
    '''
    return requests.get(url).text
