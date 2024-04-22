#!/usr/bin/env python3
"""This module provides a function (an asynchronous coroutine) that
waits for a fandom amount of time before returning a result.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random amount of delay between 0 and `max_delay` seconds.

    Args:
        max_delay (int): The maximum number of seconds to wait.

    Returns:
        float: The amount of time waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
