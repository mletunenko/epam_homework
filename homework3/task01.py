"""In previous homework task 4, you wrote a cache function that remembers
other function output value. Modify it to be a parametrized decorator. Would
give out cached value up to times number only."""

from typing import Callable


def cache(times) -> Callable:
    # create cache dict
    cache_dict = {}

    def super_wrapper(func):

        def wrapper(*args):
            # getting result
            if args in cache_dict:
                # get result if it exists
                result = cache_dict[args][0]
            else:
                # get result for new key
                result = func(*args)
                # save result in cache
                cache_dict[args] = [result, 0]

            # update cache counter
            cache_dict[args][1] += 1
            if cache_dict[args][1] == times:
                del cache_dict[args]

            return result

        return wrapper

    return super_wrapper
