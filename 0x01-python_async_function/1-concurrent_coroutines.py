#!/usr/bin/env python3
"""This module implements the wait_n function
which takes 2 arguments and returns a list of delays.
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """This function takes 2 arguments and spawns wait_random n times

    Args:
        n (int): number of times to spawn wait_random
        max_delay (int): maximum delay

    Returns:
        list[float]: list of delays
    """
    # Create a list to store the tasks/delays
    tasks = [wait_random(max_delay) for _ in range(n)]
    # Use asyncio.gather to run the tasks concurrently
    results = await asyncio.gather(*tasks, return_exceptions=True)
    # Filter out any exceptions that may have occurred
    delays_with_indices = [
        (i, result) for i, result in enumerate(results)
        if not isinstance(result, Exception)
        ]

    # Initialize variables to track processed indices and delays
    processed_indices = set()
    sorted_delays = []

    # Find the minimum delay in each iteration until all delays are processed
    while len(processed_indices) < len(delays_with_indices):
        min_delay = float('inf')
        min_index = None
        for i, delay in delays_with_indices:
            if i not in processed_indices and delay < min_delay:
                min_delay = delay
                min_index = i
        sorted_delays.append(min_delay)
        processed_indices.add(min_index)

    return sorted_delays
