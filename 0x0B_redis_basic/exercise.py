#!/usr/bin/env python3
'''
This module provides a Cache class that interacts with Redis
to store and retrieve data.
It's like a pug hiding its toys in a sea of life's meaningless chaos
Redis is the pug's secret vault amidst the void.
'''
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    '''
    Cache class for storing and retrieving data in Redis.
    Like organizing your chaotic thoughts, but in byte form.
    '''

    def __init__(self):
        '''
        Initialize the Redis client and flush the database.
        Basically, we’re clearing out all of yesterday's nonsense,
        so today’s nonsense can take its place.
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        Store data in Redis with a unique key.
        Think of it like giving a name to every random thought
        or piece of data, so you can find it later (hopefully).
        '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Optional[Union[str, bytes, int, float]]:
        '''
        Retrieve data from Redis, possibly transforming it.
        Redis returns byte strings for everything, like that friend who always
        speaks in riddles. If you want something more useful, apply the fn to
        decode it. If the key doesn't exist, Redis just shrugs.
        '''
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        '''
        Retrieve a string from Redis.
        Translates Redis byte-speak into human-readable words.
        '''
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        '''
        Retrieve an integer from Redis.
        Converts byte-gibberish into a number, like turning
        chaotic data into something you can count on.
        '''
        return self.get(key, int)
