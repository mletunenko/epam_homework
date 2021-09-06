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
    fib_seq_last_but_one = 0
    fib_seq_last = 1
    if fib_seq_last_but_one < data[0]:
        while fib_seq_last < data[0]:
            fib_seq_last_but_one, fib_seq_last = \
                fib_seq_last, fib_seq_last + fib_seq_last_but_one
    elif fib_seq_last_but_one > data[0]:
        return False
    # Now we are sure that data[0] <= fib_seq_last
    first_zero_check = data[0] == 0  # need to skip first 0 from "data"
    for value in data:
        if first_zero_check:
            first_zero_check = False
            continue
        else:
            if fib_seq_last != value:
                return False
            fib_seq_last_but_one, fib_seq_last = \
                fib_seq_last, fib_seq_last + fib_seq_last_but_one
    return True
