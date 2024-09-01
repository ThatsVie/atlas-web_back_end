#!/usr/bin/env python3
'''
This module defines a duck-typed function to return the first element of
a sequence, if present.
'''
from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    '''Return the first element of a sequence, if it exists.
    If it doesnt exist return None.'''
    if lst:
        return lst[0]
    else:
        return None
