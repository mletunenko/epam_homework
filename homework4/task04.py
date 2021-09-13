"""
Write a function that takes a number N as an input and
returns N FizzBuzz numbers*
Write a doctest for that function.
Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - doctests are run with pytest command
You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
assert fizzbuzz(5) == ["1", "2", "fizz", "4", "buzz"]
* https://en.wikipedia.org/wiki/Fizz_buzz
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    Return a list of N Fizz Buzz numbers

    >>> fizzbuzz(3)
    [1, 2, 'Fizz']

    >>> fizzbuzz(15)
    [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'Fizz Buzz']

    """
    multiple_three = 'Fizz'
    multiple_five = 'Buzz'
    result = []

    for elem in range(1, n + 1):
        if elem % 5 == 0 and elem % 3 == 0:
            result.append(multiple_three + ' ' + multiple_five)
        elif elem % 3 == 0:
            result.append(multiple_three)
        elif elem % 5 == 0:
            result.append(multiple_five)
        else:
            result.append(elem)
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
