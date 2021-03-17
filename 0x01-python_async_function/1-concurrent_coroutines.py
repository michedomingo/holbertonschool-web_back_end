#!/usr/bin/env python3
"""
Define wait_n function
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns list of delays in ascending order
    """
    delays = []
    for _ in range(n):
        delays.append(asyncio.create_task(wait_random(max_delay)))
    return [await delay for delay in asyncio.as_completed(delays)]
