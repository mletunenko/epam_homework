import string

from homework2.task05 import custom_range


def test_custom_range_string_with_two_arg():
    assert custom_range(string.ascii_lowercase, 'c') == ['a', 'b']


def test_custom_range_list_with_three_args():
    assert custom_range([1, 2, 3, 4, 5, 6], 1, 5) == [1, 2, 3, 4]


def test_custom_range_list_with_all_args():
    assert custom_range([1, 2, 3, 4, 5, 6], 1, 5, 2) == [1, 3]


def test_custom_range_list_with_negative_step():
    assert custom_range([1, 2, 3, 4, 5, 6], 5, 1, -2) == [5, 3]
