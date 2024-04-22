#!/usr/bin/env python3
"""This module implements the wait_n function"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """This function takes 2 arguments and spawns wait_random n times"""
    # Create a list to store the tasks/delays
    tasks = [wait_random(max_delay) for _ in range(n)]
    # Use asyncio.gather to run the tasks concurrently
    results = await asyncio.gather(*tasks, return_exceptions=True)
    # Filter out any exceptions that may have occurred
    delays = [
        result for result in results if not isinstance(result, Exception)
        ]
    return delays
