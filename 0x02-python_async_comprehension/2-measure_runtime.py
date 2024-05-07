#!/usr/bin/env python3
"""
Python module that measures runtime.
"""

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime should measure the total runtime and return it.
    function execute async_comprehension 4 times.
    Arguments:
        no arguments
    Return:
        nothing
    """
    t_start = time.perf_counter()
    task = [async_comprehension() for i in range(4)]
    await asyncio.gather(*task)
    t_end = time.perf_counter()
    return (t_end - t_start)
