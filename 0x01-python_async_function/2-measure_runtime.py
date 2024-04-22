#!/usr/bin/env python3
"""This module implements the measure_time function
which measures the total execution time for wait_n
"""
import asyncio
import time
import sys
from typing import Callable


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for wait_n
    and returns total_time/n

    Args:
        n (int): number of times to spawn wait_random
        max_delay (int): maximum delay

    Returns:
        float: total_time/n
    """
    start_time = time.time()
    await wait_n(n, max_delay)
    total_time = time.time() - start_time
    return total_time / n


async def main():
    if len(sys.argv) != 3:
        print("Usage: ./2-main.py <n> <max_delay>")
        sys.exit(1)
    result = await measure_time(int(sys.argv[1]), int(sys.argv[2]))
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
