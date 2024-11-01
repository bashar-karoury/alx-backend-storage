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
        local_redis.incr(f"count:{url}")
        cached_html = local_redis.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')
        html = method(url)
        local_redis.setex(f"cached:{url}", 10, html)
        return html
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
# local_redis.delete(f'count:{url}')
# local_redis.delete(f'cache:{url}')
# for _ in range(20):
#     get_page(url)
#     import time
#     time.sleep(2)
#     # print(local_redis.get(f'count:{url}'))
#     # print(local_redis.ttl(f'cache:{url}'))
