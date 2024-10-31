#!/usr/bin/env python3
"""
Cache Class Wrapper of Redis
"""
import redis
from typing import Union
import uuid


class Cache:
    """ Class to set and get data from redis server"""

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> Union[str, None]:
        """ stores data in Redis using random generated key and return
            the key """
        key = str(uuid.uuid4())
        result = self._redis.set(key, data)
        if result:
            return key
        else:
            return None
