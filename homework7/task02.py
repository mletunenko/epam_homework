"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".
    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".
    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

"""


def backspace_compare(first: str, second: str):
    return backspace(first) == backspace(second)


def backspace(string: str):
    back = 0
    result = []
    for symbol in string[::-1]:
        if symbol == '#':
            back += 1
        else:
            if not back:
                result.append(symbol)
            else:
                back -= 1
    return result


def second_backspace_compare(first: str, second: str):
    first_generator = second_backspace(first)
    second_generator = second_backspace(second)
    symbol_pairs = zip(first_generator, second_generator)
    for pair in symbol_pairs:
        if pair[0] == pair[1]:
            continue
        else:
            return False
    return True


def second_backspace(string: str):
    back = 0
    list_string = list(string)
    for position, symbol in enumerate(list_string[::-1]):
        if symbol == '#':
            back += 1
        else:
            if back:
                back -= 1
            else:
                yield symbol
