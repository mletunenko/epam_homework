"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
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
        i = fi.readline()
        max_int = min_int = int(i)
        for line in fi:
            v = int(line)
            if v > max_int:
                max_int = v
            if v < min_int:
                min_int = v
        return min_int, max_int
