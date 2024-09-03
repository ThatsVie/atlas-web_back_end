#!/usr/bin/env python3
'''
This module contains the FIFOCache class, a caching system
that inherits from the BaseCaching parent class. It uses the
FIFO (First In, First Out) caching algorithm.
'''
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    ''' FIFOCache defines a caching system with a FIFO eviction policy.
    '''

    def __init__(self):
        '''
        Calls the parent class' init method and initializes
        an order list to keep track of the insertion order.
        '''
        super().__init__()
        self.order = []

    def put(self, key, item):
        ''' Add an item to the cache.
        If key or item is None this method does nothing.
        If the number of items in the cache exceeds MAX_ITEMS
        the first item added is discarded following FIFO.
        '''
        if key is not None and item is not None:
            if key not in self.cache_data:
                self.order.append(key)
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = self.order.pop(0)
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")

    def get(self, key):
        ''' Retrieve an item by key from the cache.
        If key is None or doesn't exist in the cache, returns None.
        '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
