#!/usr/bin/env python3
'''
This module has a coroutine wait_n that runs wait_random multiple times
and returns a sorted list of delays.
'''

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Runs wait_random n times with a maximum delay of max_delay
    and returns the delays in ascending order.
    '''
    # list of tasks to run concurrently
    tasks = [wait_random(max_delay) for _ in range(n)]
    
    # gather results as they complete
    delays = [await task for task in asyncio.as_completed(tasks)]
    
    return delays
