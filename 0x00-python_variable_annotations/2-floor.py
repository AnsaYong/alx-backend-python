#!/usr/bin/env python3
"""This module provides a type-annotated function which takes
a float n as argument and returns the floor of the float.
"""
import math


def floor(n: float) -> int:
    """Type-annotated function floor which takes a float n as argument
    and returns the floor of the float.

    Args:
        n (float): a float number

    Returns:
        int: the floor of the float number
    """
    return math.floor(n)
