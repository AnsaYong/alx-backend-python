#!/usr/bin/env python3
"""This module implements the task_wait_n function
which creates a task for the wait_random coroutine.
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """This function is similar to wait_n but uses task_wait_random.

    Args:
        n (int): Number of times to call task_wait_random.
        max_delay (int): Maximum delay for each task.

    Returns:
        List[float]: List of delays.
    """
    # Create a list to store the tasks/delays
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    # Use asyncio.gather to run the tasks concurrently
    results = await asyncio.gather(*tasks, return_exceptions=True)
    # Filter out any exceptions that may have occurred
    delays_with_indices = [
        (i, result) for i, result in enumerate(results)
        if not isinstance(result, Exception)
    ]

    # Initialize variables to track processed indices and delays
    processed_indices = set()
    delays = []

    # Find the minimum delay in each iteration until all delays are processed
    while len(processed_indices) < len(delays_with_indices):
        min_delay = float('inf')
        min_index = None
        for i, delay in delays_with_indices:
            if i not in processed_indices and delay < min_delay:
                min_delay = delay
                min_index = i
        delays.append(min_delay)
        processed_indices.add(min_index)

    return delays
