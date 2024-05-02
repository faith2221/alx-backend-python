#!/usr/bin/env python3
"""
Function sum_mixed_list which takes a list mxd_lst of integers.
"""


import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """returns their sum as a float."""
    return float(sum(mxd_lst))
