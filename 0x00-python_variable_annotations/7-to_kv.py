#!/usr/bin/env python3
"""
Function to_kv that takes a string k
and an int OR float v as arguments and returns a tuple:
    first element of the tuple is the string k
    second element is the square of the int/float v
    and should be annotated as a float.
"""


import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """returns a tuple."""
    return (k, float(v * v))
