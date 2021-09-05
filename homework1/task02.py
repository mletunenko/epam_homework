"""
Given a cell with "it's a fib sequence" from slideshow,
please write function "check_fib", which accepts a Sequence of integers, and
returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    # Check if "data" is empty
    if not data:
        return False
    # Grow fib sec till meet first value of "data"
    gen = [0, 1]
    if gen[0] < data[0]:
        while gen[-1] < data[0]:
            gen.append(gen[-2] + gen[-1])
    elif gen[0] > data[0]:
        return False
    # Now we are sure that sec[0] <= gen[-1]
    first_zero_check = data[0] == 0  # need to skip first 0 from "data"
    for v in data:
        if first_zero_check:
            first_zero_check = False
            continue
        else:
            if gen[-1] != v:
                return False
            gen.append(gen[-2] + gen[-1])
    return True
