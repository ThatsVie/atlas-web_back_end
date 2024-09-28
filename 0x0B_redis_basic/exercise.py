#!/usr/bin/env python3
'''
This module provides a Cache class that interacts with Redis
to store and retrieve data.
It's like a pug hiding its toys in a sea of life's meaningless chaos
Redis is the pug's secret vault amidst the void.
'''
import redis
import uuid
from typing import Union


class Cache:
    '''
    Cache class that interacts with Redis, like storing away the things that
    make sense in a world that doesn't.
    '''

    def __init__(self):
        '''
        Initialize the Redis client and flush the database.
        You know that feeling when you clear your mind after an
        existential crisis, only to prepare for another one?
        That's flushdb. Wipe it all away and start again,
        like a pug waking up each day ready for belly rubs despite everything.
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        Store data in Redis and return the generated key.
        It's like trying to keep track of all the things
        that don't really matter, but you're giving them names anyway.
        Just like a pug hiding its bones in random spots, Redis gives each
        piece of data a unique name, as if that makes life more organized.
        '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
