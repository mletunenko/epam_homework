"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    with open(file_path, encoding='unicode-escape') as file:
        pass



def get_rarest_char(file_path: str) -> str:
    # Create a counter dictionary
    count_dict = {}
    # Open file data.txt
    with open(file_path, encoding='unicode-escape') as file:
        rarest_char = file.read(1)
        while True:
            # Read a file line by line
            line = file.readline()
            # Stop While loop if a file is ended
            if not line:
                break
            # Read line char by char
            for char in line:
                # Create a key if char is new
                if char not in count_dict:
                    count_dict[char] = 0
                # Count a char
                count_dict[char] += 1
    # Looking for rarest char in counter dict
    for key in count_dict:
        if count_dict[key] < count_dict[rarest_char]:
            rarest_char = key
    return rarest_char


def count_punctuation_chars(file_path: str) -> int:
    pass


def count_non_ascii_chars(file_path: str) -> int:
    pass


def get_most_common_non_ascii_char(file_path: str) -> str:
    pass
