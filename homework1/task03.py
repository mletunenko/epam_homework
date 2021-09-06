"""
Write down the function, which reads input line-by-line,
and find maximum and minimum values.
Function should return a tuple with the max and min values.
For example for [1, 2, 3, 4, 5], function should return [1, 5]
We guarantee, that file exists and contains line-delimited integers.
To read file line-by-line you can use this snippet:
with open(file_name) as fi:
    for line in fi:
        ...
"""
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    with open(file_name) as fi:
        first_str = fi.readline()
        if not first_str:
            return None
        maximum = minimum = int(first_str)
        for line in fi:
            value = int(line)
            if value > maximum:
                maximum = value
            if value < minimum:
                minimum = value
        return minimum, maximum
