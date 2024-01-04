#!/usr/bin/env python3
"""Module that take the code from wait_n and alter it into
a new function task_wait_n"""
import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Function that should return the list of all the delays (float values).
    The list of the delays should be in ascending order without using sort()
    because of concurrency. SAME AS 1 TASK"""
    task = []
    for i in range(n):
        task.append(task_wait_random(max_delay))

    delay = await asyncio.gather(*task)

    return sorted(delay)
