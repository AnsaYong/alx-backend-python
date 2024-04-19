#!/usr/bin/env python3
"""This module provides a type-annotated function to_kv that takes a string k
and an int OR float v as arguments and returns a tuple.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple containing the string k and the square of the number v.

    Args:
        k (str): the string to return.
        v (int OR float): the number to square.

    Returns:
        Tuple[str, float]: the string k and the square of the number v.
    """
    return (k, v * v)
