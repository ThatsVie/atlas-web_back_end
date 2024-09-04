#!/usr/bin/env python3
'''
This module contains a helper function to calculate the start and end index
for pagination given the page number and page size.
'''

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    Calculate the start and end index for pagination.
    '''
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
