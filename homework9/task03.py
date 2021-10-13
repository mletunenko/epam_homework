"""
Write a function that takes directory path, a file extension and an optional
tokenizer. It will count lines in all files with that extension if there are no
tokenizer. If a the tokenizer is not none, it will count tokens.
For dir with two files from hw1.py:
# >>> universal_file_counter(test_dir, "txt")
6
# >>> universal_file_counter(test_dir, "txt", str.split)
6
"""
import os
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(
        dir_path: Path, file_extension: str,
        tokenizer: Optional[Callable] = None
) -> int:
    files = os.listdir(dir_path)
    goal_files = list(filter(lambda x: x.endswith(file_extension), files))
    counter = 0
    for file in goal_files:
        with open(dir_path + '/' + file) as fl:
            for row in fl:
                if tokenizer:
                    counter += len(tokenizer(row))
                else:
                    counter += 1
    return counter
