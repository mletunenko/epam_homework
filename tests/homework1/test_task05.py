from homework1.task05 import find_maximal_subarray_sum

"""Some positive testcases"""


def test_positive_find_1():
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], k=3) == 16


def test_positive_find_2():
    assert find_maximal_subarray_sum([1, 3], k=3) == 4


def test_positive_find_3():
    assert find_maximal_subarray_sum([], k=3) is None
