from homework2.task02 import major_and_minor_elem


def test_positive_list_of_one_elem():
    assert major_and_minor_elem([1]) == (1, 1)


def test_positive_list_of_two_same_elem():
    assert major_and_minor_elem([1, 1]) == (1, 1)


def test_positive_complex_list():
    assert major_and_minor_elem([1, 2, 3, 1, 2, 1, 4, 4]) == (1, 3)


def test_positive_complex_list_with_negative_number():
    assert major_and_minor_elem([-2, -2, 1]) == (-2, 1)