#!/usr/bin/env python3
"""
This module provides a type-annotated function type_checking
which takes a variable x and returns the type of x.
"""
from typing import Union, Tuple, Any, List, Dict


def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> Tuple[Any, ...]:
    """ Returns a zoomed-in version of a 1D array.
    Args:
        lst (Tuple): A 1D array of integers.
        factor (int): The factor by which to zoom in the array.
    Returns:
        Tuple: A zoomed-in version of the array.
    """
    zoomed_in: Tuple[Any, ...] = tuple(
        item for item in lst
        for _ in range(factor)
    )
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)