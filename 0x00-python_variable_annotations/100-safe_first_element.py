#!/usr/bin/env python3
"""
This module provides a type-annotated function safe_first_element.
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Returns the first element of a sequence if it exists, otherwise None.

    Args:
        lst (Sequence[Any]): A sequence of elements.

    Returns:
        Union[Sequence[Any], None]: The first element of the sequence
        if it exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
