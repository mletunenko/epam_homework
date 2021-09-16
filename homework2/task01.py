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
    storage = []
    with open(file_path, encoding='unicode-escape') as file:
        for line in file:
            for word in line.split():
                word = word.strip("""!"#$%&'()*+,-./:;<=>?@[]^_`\\{|}~""")
                number = len(set(word))
                if len(storage) < 10:
                    storage.append((number, word))
                    if len(storage) == 10:
                        storage.sort(key=lambda x: x[0], reverse=True)
                elif number > storage[-1][0]:
                    for index, (stored_number, stored_word) in enumerate(
                            storage):
                        if number > stored_number:
                            storage.insert(index, (number, word))
                            storage = storage[:10]
                            break
    return [elem[1] for elem in storage]


def get_rarest_char(file_path: str) -> str:
    count_dict = {}
    with open(file_path, encoding='unicode-escape') as file:
        rarest_char = file.read(1)
        if not rarest_char:
            return ''
        file.seek(0)
        for line in file:
            for char in line:
                count_dict.setdefault(char, 0)
                count_dict[char] += 1
    return min(count_dict, key=count_dict.get)


def count_punctuation_chars(file_path: str) -> int:
    punctuation = """!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"""
    counter = 0
    with open(file_path, encoding='unicode-escape') as file:
        for line in file:
            for char in line:
                if char in punctuation:
                    counter += 1
    return counter


def count_non_ascii_chars(file_path: str) -> int:
    counter = 0
    with open(file_path, encoding='unicode-escape') as file:
        for line in file:
            for char in line:
                if not char.isascii():
                    counter += 1
    return counter


def get_most_common_non_ascii_char(file_path: str) -> str:
    counter_dict = {}
    with open(file_path, encoding='unicode-escape') as file:
        for line in file:
            for char in line:
                if not char.isascii():
                    if char not in counter_dict:
                        counter_dict[char] = 0
                    counter_dict[char] += 1
    if counter_dict:
        most_common_char = max(counter_dict, key=counter_dict.get)
    else:
        most_common_char = ''
    return most_common_char
