#!/usr/bin/env python3
"""
This module provides a type-annotated function sum_list that takes
a list input_list of floats as argument and returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of the floats in input_list.

    Args:
        input_list (list): the list of floats to sum.

    Returns:
        float: the sum of the floats in input_list.
    """
    return sum(input_list)
