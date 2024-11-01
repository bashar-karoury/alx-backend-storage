#!/usr/bin/env python3
"""
Implementing an expiring web cache and tracker
"""
import redis
from typing import Union, Callable
from functools import wraps
import requests


def cache_url(method: Callable) -> Callable:
    """ decorator to count calles for passed method"""

    @wraps(method)
    def wrapper(url):
        local_redis = redis.Redis()
        result = method(url)
        # Increment the count or create it with expiration
        if not local_redis.exists(f'count:{url}'):  # Check if the key exists
            # Set the key with expiration
            local_redis.set(f'count:{url}', 1, ex=10)
        else:
            local_redis.incr(f'count:{url}')  # Increment if it already exists
        return result
    return wrapper


@cache_url
def get_page(url: str) -> str:
    """ uses the requests module to obtain the HTML content of
        a particular URL and returns it.
    """
    result = requests.get(url)
    return result.text


# local_redis = redis.Redis()
# url = 'https://slowwly.robertomurray.co.uk/'
# print(get_page(url))


# print(local_redis.get(f'count:{url}'))
# print(local_redis.ttl(f'count:{url}'))
