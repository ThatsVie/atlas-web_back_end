#!/usr/bin/env python3
'''
This module provides a Cache class that interacts with Redis
to store and retrieve data. It also keeps count of method calls.
Redis is like a cosmic accountant, tracking every call like it’s
preparing for the next apocalypse or tallying pug snacks.
'''
import redis
import uuid
import functools
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    '''
    Decorator that counts how many times a method is called using Redis.
    Imagine counting how many times you've ignored the news about rising
    sea levels. Redis does this for your method calls, one existential dread
    at a time.
    '''
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        '''
        Wrapper function that increments the count each time
        the decorated method is called. Redis tracks it all like
        keeping tabs on how many ice caps we have left or how many times
        your pug asks for dinner.
        '''
        key = method.__qualname__  # Use the method's qualified name as the key
        self._redis.incr(key)  # Incrementing count for this method in Redis
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    '''
    Cache class for storing and retrieving data in Redis.
    Now it also tracks how many times its methods are called.
    Think of it like counting the inevitable whether it’s climate change
    or how many belly rubs your pug demands.
    '''

    def __init__(self):
        '''
        Initialize the Redis client and flush the database.
        Basically wiping everything clean like deleting the record
        of all those carbon emissions, so we can pretend everything’s fine.
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        Store data in Redis with a unique key and count how many times
        this method has been called.
        Like storing away little pieces of hope, except Redis never
        forgets how many you've tried to hide.
        '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Optional[Union[str, bytes, int, float]]:
        '''
        Retrieve data from Redis, possibly transforming it.
        Redis gives everything back in bytes, like handing you
        a confusing climate report. You’ll need to decode it if you
        want it to make sense.
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
        Translates Redis bytespeak into human-readable form, kind of like
        turning scientific data into something we can understand.
        '''
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        '''
        Retrieve an integer from Redis.
        Converts byte gibberish into something countable, like measuring
        the sea level rise except Redis makes it easier to ignore.
        '''
        return self.get(key, int)
