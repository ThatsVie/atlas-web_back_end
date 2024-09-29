#!/usr/bin/env python3
"""
Main file for Task 4
"""
Cache = __import__('exercise').Cache
replay = __import__('exercise').replay

cache = Cache()

cache.store("foo")
cache.store("bar")
cache.store(42)

# Replay the history of the store method
replay(cache.store)
