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
