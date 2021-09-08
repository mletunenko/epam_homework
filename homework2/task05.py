"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.
Write a function that accept any iterable of unique values and then
it behaves as range function:
import string
assert = custom_range(string.ascii_lowercase, 'g') ==
['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') ==
['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) ==
['p', 'n', 'l', 'j', 'h']
"""


def custom_range(iterable, arg1, arg2=None, step=1):
    if arg2 is None:
        start = 0
        stop = iterable.index(arg1)
    else:
        start = iterable.index(arg1)
        stop = iterable.index(arg2)
    result = []
    for elem in range(start, stop, step):
        result.append(iterable[elem])
    return result
