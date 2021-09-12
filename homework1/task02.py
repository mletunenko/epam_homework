"""
Given a cell with "it's a fib sequence" from slideshow,
please write function "check_fib", which accepts a Sequence of integers, and
returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    if data[0] != 0:
        return False
    fib_seq_last_but_one = 0
    fib_seq_last = 1
    for value in data[1:]:
        if fib_seq_last != value:
            return False
        fib_seq_last_but_one, fib_seq_last = \
            fib_seq_last, fib_seq_last + fib_seq_last_but_one
    return True
