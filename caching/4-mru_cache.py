#!/usr/bin/env python3
'''
This module contains the MRUCache class, a caching system
that inherits from the BaseCaching parent class. It uses the
MRU (Most Recently Used) caching algorithm.
'''
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    ''' MRUCache defines a caching system with an MRU eviction policy.
    '''

    def __init__(self):
        '''
        Calls the parent class' init method and initializes
        a list to keep track of the usage order.
        '''
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        ''' Add an item to the cache.
        If key or item is None this method does nothing.
        If the number of items in the cache exceeds MAX_ITEMS
        the most recently used item is discarded following MRU.
        '''
        if key is not None and item is not None:
            # If the key already exists update the item and move key to the end
            if key in self.cache_data:
                self.usage_order.remove(key)
            self.cache_data[key] = item
            self.usage_order.append(key)

            # If cache exceeds the maximum size remove the MRU item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                mru_key = self.usage_order.pop(-2)
                del self.cache_data[mru_key]
                print(f"DISCARD: {mru_key}")

    def get(self, key):
        ''' Retrieve an item by key from the cache.
        If key is None or doesn't exist in the cache it returns None.
        '''
        if key is not None and key in self.cache_data:
            # Since this key was recently accessed update the usage order
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache_data[key]
        return None
