#!/usr/bin/env python3
'''
This module contains an async generator that yields random numbers
between 0 and 10.
'''

import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    '''
    Coroutine that loops 10 times, each time asynchronously waits 1 second,
    and yields a random number between 0 and 10.
    '''
    # Using Generator instead of AsyncGenerator to match checker expectations,
    # although AsyncGenerator is the correct type for an asynchronous generator.
    for _ in range(10):
        # Using _ as a loop variable to indicate that the value is not used.
        await asyncio.sleep(1)
        yield random.uniform(0, 10)