#!/usr/bin/env python3
'''
This module contains the LIFOCache class, a caching system
that inherits from the BaseCaching parent class. It uses the
LIFO (Last In, First Out) caching algorithm.
'''
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    ''' LIFOCache defines a caching system with a LIFO eviction policy.
    '''

    def __init__(self):
        '''
        Calls the parent class' init method and initializes
        a list to keep track of the order of insertion.
        '''
        super().__init__()
        self.stack = []

    def put(self, key, item):
        ''' Add an item to the cache.
        If key or item is None this method does nothing.
        If the number of items in the cache exceeds MAX_ITEMS,
        the last item added is discarded following LIFO.
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.stack.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Remove the most recently added item
                last_key = self.stack.pop(-2)
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

    def get(self, key):
        ''' Retrieve an item by key from the cache.
        If key is None or doesn't exist in the cache, it returns None.
        '''
        return self.cache_data.get(key, None)
