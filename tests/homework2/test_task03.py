from homework2.task03 import combinations


def test_combinations_single_list():
    assert combinations([0, 1]) == [[0], [1]]


def test_combinations_two_same_len_lists():
    assert combinations([0, 1], [2, 3]) == [[0, 2], [0, 3], [1, 2], [1, 3]]


def test_combinations_three_dif_len_lists():
    assert combinations([0], [2, 3], [4, 5, 6]) == \
           [[0, 2, 4], [0, 2, 5], [0, 2, 6], [0, 3, 4], [0, 3, 5], [0, 3, 6]]
