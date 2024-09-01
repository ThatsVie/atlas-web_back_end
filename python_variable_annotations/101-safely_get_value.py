#!/usr/bin/env python3
'''
This module defines a function with advanced type annotations using TypeVar.
'''
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    '''Return the value from the dictionary if the key exists.
    If it doesnt exist return the default.'''
    if key in dct:
        return dct[key]
    else:
        return default
