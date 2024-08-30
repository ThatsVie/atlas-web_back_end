#!/usr/bin/env python3
'''
This module contains function measure_time that measures the average
runtime of the wait_n coroutine.
'''

import asyncio
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    Measures the total execution time for wait_n(n, max_delay) and
    returns the average time per call.
    '''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time

    return total_time / n
