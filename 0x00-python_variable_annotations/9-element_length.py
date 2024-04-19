#!/usr/bin/env python3
"""
This module provides a type-annotated function element_length that takes
a list input_list of strings as argument and returns a list of integers.
"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of integers representing the lengths of the strings in
    input_list.

    Args:
        input_list (List[str]): the list of strings to return the lengths of.

    Returns:
        List[int]: a list of integers representing the lengths of the strings
        in input_list.
    """
    return [len(i) for i in lst]
