#!/usr/bin/env python3
""" This module provides a function that takes a list of integers and floats
    and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Returns the sum of a list of integers and floats as a float.
    
    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and floats.
        
    Returns:
        float: The sum of the list of integers and floats.
    """
    return sum(mxd_lst)
