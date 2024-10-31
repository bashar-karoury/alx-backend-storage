#!/usr/bin/env python3
"""
Cache Class Wrapper of Redis
"""
import redis
from typing import Union, Callable
import uuid


class Cache:
    """ Class to set and get data from redis server"""

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ stores data in Redis using random generated key and return
            the key """
        key = str(uuid.uuid4())
        result = self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Union[Callable, None]) -> str:
        """ gets data from Redis using provided function to parse 
            the result return
        """

        result = self._redis.get(key)
        if fn:
            return fn(result)
        else:
            return result

    def get_str(self, key: str) -> str:
        """ get value of key from Redis and encode it into string"""
        return self.get(key, str)

    def get_int(self, key: str) -> str:
        """ get value of key from Redis and encode it into int"""
        return self.get(key, int)
