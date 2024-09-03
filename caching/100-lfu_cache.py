#!/usr/bin/env python3
'''
This module contains the LFUCache class, a caching system
that inherits from the BaseCaching parent class. It uses the
LFU (Least Frequently Used) caching algorithm with LRU as a
tie-breaker.
'''
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    ''' LFUCache defines a caching system with an LFU eviction policy.
    '''

    def __init__(self):
        '''
        Calls the parent class' init method and initializes
        a dictionary to keep track of usage frequency and order.
        '''
        super().__init__()
        self.usage_frequency = {}
        self.usage_order = []

    def put(self, key, item):
        ''' Add an item to the cache.
        If key or item is None this method does nothing.
        If the number of items in the cache exceeds MAX_ITEMS
        the least frequently used item is discarded
        Uses LRU as a tie-breaker.
        '''
        if key is None or item is None:
            return

        # If the key already exists update the item and usage frequency
        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_frequency[key] += 1
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            # If the cache is full remove the LFU item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used items
                min_freq = min(self.usage_frequency.values())
                lfu_keys = [k for k in self.usage_order
                            if self.usage_frequency[k] == min_freq]

                # Discard least recently used among the least frequently used
                lfu_key = lfu_keys[0]
                del self.cache_data[lfu_key]
                del self.usage_frequency[lfu_key]
                self.usage_order.remove(lfu_key)
                print(f"DISCARD: {lfu_key}")

            # Add the new item to the cache
            self.cache_data[key] = item
            self.usage_frequency[key] = 1
            self.usage_order.append(key)

    def get(self, key):
        ''' Retrieve an item by key from the cache.
        If key is None or doesn't exist in the cache it returns None.
        '''
        if key is None or key not in self.cache_data:
            return None

        # Since this key was recently accessed, update the usage order
        # and frequency
        self.usage_frequency[key] += 1
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
