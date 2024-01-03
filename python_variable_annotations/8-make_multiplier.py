#!/usr/bin/env python3
"""Module that type-annotated function make_multiplier that takes
a float multiplier as argument and returns
a function that multiplies a float by multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function that takes a float multiplier as argument
    and returns a function that multiplies a float by multiplier."""
    def multiplier(x: float) -> float:
        """Function that create multiplier"""
        return x * multiplier
    return make_multiplier
