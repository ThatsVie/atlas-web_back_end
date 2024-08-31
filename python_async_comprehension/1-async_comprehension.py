#!/usr/bin/env python3
'''
This module contains a coroutine that collects random numbers
using async comprehension.
'''

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    Coroutine that collects 10 random numbers from async_generator
    using async comprehension and returns them as a list.
    '''
    return [num async for num in async_generator()]
