#!/usr/bin/env python3
'''
This module contains the LRUCache class, a caching system
that inherits from the BaseCaching parent class. It uses the
LRU (Least Recently Used) caching algorithm.
'''
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    ''' LRUCache defines a caching system with an LRU eviction policy.
    '''

    def __init__(self):
        '''
        Calls the parent class' init method and initializes
        an ordered list to keep track of the usage order.
        '''
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        ''' Add an item to the cache.
        If key or item is None this method does nothing.
        If the number of items in the cache exceeds MAX_ITEMS,
        the least recently used item is discarded following LRU.
        '''
        if key is not None and item is not None:
            # If the key already exists update the item and move key to the end
            if key in self.cache_data:
                self.usage_order.remove(key)
            self.cache_data[key] = item
            self.usage_order.append(key)

            # If cache exceeds the max size remove the LRU item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                lru_key = self.usage_order.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

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
