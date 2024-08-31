#!/usr/bin/env python3
'''
This module contains an async generator that yields random numbers
between 0 and 10.
'''

import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    '''
    Coroutine that loops 10 times, each time asynchronously waits 1 second,
    and yields a random number between 0 and 10.
    '''
    for _ in range(10):
        # Using _ as a loop variable to say that the value is not used.
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
