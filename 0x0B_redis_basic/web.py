#!/usr/bin/env python3
'''
This module implements a web cache using Redis and tracks URL access counts.
Imagine Redis as the last bunker on Earth, hoarding bits of information while
the world burns. You ask for the same data over and over, and Redis,
like a weary survivalist, reminds you it already stored that info-temporarily.
'''
import redis
import requests
from typing import Callable
from functools import wraps


# Initialize Redis client
r = redis.Redis()


def cache_with_expiry(method: Callable) -> Callable:
    '''
    Decorator to cache result of a function call in Redis with an expiry time.
    Think of it as rationing your dwindling resources. You only get to keep
    that precious web content for 10 seconds, and then it's gone,
    like fresh water in a drought.
    '''
    @wraps(method)
    def wrapper(url: str) -> str:
        '''
        Tracks how many times a URL is accessed and caches the result.
        It’s like rationing supplies during the apocalypse.
        Redis reminds you how many times you've come back for the same stale
        resources, only to serve them cold from the cache,
        until it’s time to scavenge again.
        '''
        access_count_key = f"count:{url}"
        r.incr(access_count_key)

        # Check if the URL is already cached
        cached_key = f"cached:{url}"
        cached_page = r.get(cached_key)
        if cached_page:
            return cached_page.decode("utf-8")

        # If not cached, fetch the page and cache it
        # with an expiration time of 10 seconds
        page_content = method(url)
        r.setex(cached_key, 10, page_content)
        return page_content

    return wrapper


@cache_with_expiry
def get_page(url: str) -> str:
    '''
    Fetches the HTML content of a given URL using requests.
    It's like venturing into a wasteland to gather resources.
    Redis caches the page for 10 seconds, ensuring you don’t have to risk
    life and limb to retrieve the same dwindling supplies over and over.
    '''
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    url = (
        "http://slowwly.robertomurray.co.uk/delay/5000/url/"
        "http://www.example.com"
    )

    # Fetch the page for the first time
    print(get_page(url))

    # Fetch it again (should be served from cache)
    print(get_page(url))

    # Check how many times the URL was accessed
    print(f"URL accessed {r.get(f'count:{url}').decode('utf-8')} times.")
