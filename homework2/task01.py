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
    # Create a storage list which contains a tuple (len of word, word)
    storage = []
    with open(file_path, encoding='unicode-escape') as file:
        for line in file:
            for word in line.split():
                # Cut the punctuation from word
                word = word.strip(r"""!"#$%&'()*+,-./:;<=>?@[]^_`\{|}~""")
                number = len(set(word))
                # Check if storage less then 10 words
                if len(storage) < 10:
                    # Put the word into storage
                    storage.append((number, word))
                    # Check if storage have 10 words
                    if len(storage) == 10:
                        # Sort a storage, to have shortest word in zero pos
                        storage.sort(key=lambda x: x[0], reverse=True)
                # Check if word enough good to put in storage
                elif number > storage[-1][0]:
                    # Looking for place for new word
                    for index, (stored_number, stored_word) in enumerate(
                            storage):
                        # Insert word by len
                        if number > stored_number:
                            storage.insert(index, (number, word))
                            # Take the 10 longest word in storage
                            storage = storage[:10]
                            break
    return [elem[1] for elem in storage]


def get_rarest_char(file_path: str) -> str:
    # Create a counter dictionary
    count_dict = {}
    # Open file data.txt
    with open(file_path, encoding='unicode-escape') as file:
        # Try to take a first char as rarest
        rarest_char = file.read(1)
        # Check if file is not empty
        if not rarest_char:
            return None
        # Move seek to the beginning of file
        file.seek(0)
        while True:
            # Read a file line by line
            line = file.readline()
            # Stop reading if a file is ended
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
    # Know every punctuation char
    punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    # Declare a counter
    counter = 0
    # Open a file
    with open(file_path, encoding='unicode-escape') as file:
        while True:
            # Read a file line by line
            line = file.readline()
            # Stop reading if a file is ended
            if not line:
                break
            # Read a line char by char
            for char in line:
                # Check if char is punctuation
                if char in punctuation:
                    counter += 1
    return counter


def count_non_ascii_chars(file_path: str) -> int:
    # Create a counter
    counter = 0
    with open(file_path, encoding='unicode-escape') as file:
        for line in file:
            for char in line:
                # Check if char is not ascii char
                if not char.isascii():
                    # Count if not
                    counter += 1
    return counter


def get_most_common_non_ascii_char(file_path: str) -> str:
    counter_dict = {}
    with open(file_path, encoding='unicode-escape') as file:
        while True:
            line = file.readline()
            if not line:
                break
            for char in line:
                if not char.isascii():
                    if char not in counter_dict:
                        counter_dict[char] = 0
                    counter_dict[char] += 1
    if counter_dict:
        most_common_char = max(counter_dict.items(), key=lambda x: x[1])[0]
    else:
        most_common_char = ''
    return most_common_char
