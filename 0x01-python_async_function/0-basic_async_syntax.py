#!/usr/bin/env python3
"""
Define wait_random function
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait up to max_delay seconds then returns length of delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
