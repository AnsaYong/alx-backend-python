#!/usr/bin/env python3
"""
This module provides a type-annotated function safely_get_value
which takes a dictionary d, a key k and an optional default value
and returns the value of the key in the dictionary if it exists,
otherwise the default value.
"""
from typing import Any, Mapping, TypeVar, Union
T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[None, T]
        ) -> Union[Any, T]:
    """ Returns the value of the key in the dictionary if it exists,
    otherwise the default value.
    Args:
        dct (Dict[str, T]): A dictionary of elements.
        key (str): A key to search for in the dictionary.
        default (Optional[T]): The default value to return
                                if the key is not found.
    Returns:
        T: The value of the key in the dictionary if it exists,
        otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
