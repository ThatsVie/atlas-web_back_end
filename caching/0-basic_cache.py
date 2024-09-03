#!/usr/bin/env python3
''' Module for BasicCache class.
This module contains the BasicCache class, a simple caching system
that inherits from the BaseCaching parent class. It has no limit on
the number of items it can store in the cache.
'''
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    ''' BasicCache defines a caching system with no item limit.
    It inherits from BaseCaching.
    '''

    def put(self, key, item):
        ''' Add an item to the cache.
        If key or item is None, this method does nothing.
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        ''' Retrieve an item by key from the cache.
        If key is None or doesn't exist in the cache, returns None.
        '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
