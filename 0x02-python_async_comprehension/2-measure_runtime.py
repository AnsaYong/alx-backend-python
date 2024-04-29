#!/usr/bin/env python3
"""This module provides a coroutine called measure_runtime
that takes no arguments."""
import time
import asyncio
from typing import List


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    This coroutine will execute async_comprehension four times in parallel
    using asyncio.gather. It will then measure the total runtime and return it.

    Args:
        None

    Returns:
        float: The total runtime of the four async_comprehension calls.
    """
    start = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    return time.time() - start
