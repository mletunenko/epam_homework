from homework1.task04 import check_sum_of_four

"""Some positive testcases"""


def test_positive_check_1():
    assert check_sum_of_four([-1, 100], [-1, 200], [2, 100], [0, 300]) == 1


def test_positive_check_2():
    assert check_sum_of_four([-1, 100], [-1, 200], [], [0, 300]) == 0


def test_positive_check_3():
    assert check_sum_of_four(
        [1, 2, 3], [-1, -2, -3], [4, 5, 6], [-4, -3, -2]) == 10
