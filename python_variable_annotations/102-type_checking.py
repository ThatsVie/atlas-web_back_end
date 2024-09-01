#!/usr/bin/env python3
'''
This module uses type checking with mypy to validate and apply type annotations
'''
from typing import Tuple, List


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    '''Return a list that repeats each element of the tuple a specified number of times.'''
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
