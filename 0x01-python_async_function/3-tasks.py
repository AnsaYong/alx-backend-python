#!/usr/bin/env python3
"""This module implements the task_wait_random function
which creates a task for the wait_random coroutine.
"""
import asyncio
from typing import Callable


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create a task for the wait_random coroutine with the given max_delay.

    Args:
        max_delay (int): The maximum delay for wait_random.

    Returns:
        asyncio.Task: A task for the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
