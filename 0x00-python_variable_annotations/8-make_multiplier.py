#!/usr/bin/env python3
"""This module provides a type-annotated function make_multiplier that takes a
float multiplier as argument and returns a function that multiplies a float by
multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by multiplier.

    Args:
        multiplier (float): the number to multiply by.

    Returns:
        Callable[[float], float]: a function that multiplies a float by
        multiplier.
    """
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
