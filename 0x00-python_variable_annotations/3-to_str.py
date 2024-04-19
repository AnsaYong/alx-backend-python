#!/usr/bin/env python3
"""
This module provides a type-annotated function to_str that takes a float n as
argument and returns the string representation of the float.
"""
from typing import Union


def to_str(n: float) -> str:
    """
    Returns the string representation of the float n.

    Args:
        n (float): the float to convert to string representation.
    
    Returns:
        str: the string representation of the float n.
    """
    return str(n)
