#!/usr/bin/env python3
"""Import wait_random from the previous python file
that you’ve written and write an async"""

import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Function that should return the list of all the delays (float values).
    The list of the delays should be in ascending order without using sort()
    because of concurrency."""
    task = []
    for i in range(n):
        task.append(wait_random(max_delay))

    delay = await asyncio.gather(*task)

    return sorted(delay)
