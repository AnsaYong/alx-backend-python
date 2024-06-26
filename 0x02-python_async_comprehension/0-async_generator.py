#!/usr/bin/env python3
"""
This module provides a coroutine called async_generator that takes
no arguments.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    This coroutine takes no input. It loops 10 times, waiting 1 sec after
    each loop and then generates a random number between 0 and 10.

    Args:
        None

    Returns:
        A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


if __name__ == "__main__":
    asyncio.run(async_generator())
