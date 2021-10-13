"""
Write a function that merges integer from sorted files and returns an iterator
file1.txt:
1
3
5
file2.txt:
2
4
6
[1, 2, 3, 4, 5, 6]
"""
from pathlib import Path
from typing import Iterator, List, Union


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    result_list = []
    for file in file_list:
        with open(file) as file:
            for row in file:
                row = row.strip()
                if row:
                    result_list.append(int(row))
    return iter(sorted(result_list))
