#!/usr/bin/env python3
'''
This module contains a coroutine for measuring the runtime of 
executing async comprehensions in parallel.
'''


import asyncio
import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    '''
    Coroutine that executes async_comprehension four times in parallel using
    asyncio.gather and measures the total runtime.
    '''
    # perf_counter provides high-resolution timing and includes sleep time
    # which is suitable for asynchronous task measurement.
    start_time = time.perf_counter()

    # Execute four async comprehensions in parallel
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    total_time = time.perf_counter() - start_time
    return total_time
