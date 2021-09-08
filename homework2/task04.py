"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.
def func(a, b):
    return (a ** b) ** 2
cache_func = cache(func)
some = 100, 200
val_1 = cache_func(*some)
val_2 = cache_func(*some)
assert val_1 is val_2
"""
from typing import Callable


def cache(func: Callable) -> Callable:
    # Create a cache storage dict
    cache_dict = {}

    def wrapper(*args):
        # Check if func with args already was called
        if args not in cache_dict:
            # Create a new dict key and value if not
            cache_dict[args] = func(*args)
        # Return value from storage dict
        return cache_dict[args]

    return wrapper
