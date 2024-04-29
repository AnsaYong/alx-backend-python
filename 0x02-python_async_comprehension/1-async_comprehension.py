#!/usr/bin/env python3
"""
This module provides an asyn module that retreives a list of random floats.
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    This coroutine takes no arguments. It will collect 10 random numbers
    using an async comprehension over async_generator, then return the 10
    random numbers.

    Args:
        None

    Returns:
        List[float]: A list of 10 random numbers between 0 and 10.
    """
    return [i async for i in async_generator()]
