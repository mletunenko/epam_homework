from homework1.task02 import check_fibonacci


def test_positive_fibonacci_1():
    """Testing that list give True"""
    assert check_fibonacci([0])


def test_positive_fibonacci_2():
    """Testing that list give True"""
    assert check_fibonacci([0, 1])


def test_positive_fibonacci_3():
    """Testing that list give True"""
    assert check_fibonacci([89, 144, 233])


def test_negative_fibonacci_1():
    """Testing that empty list give False"""
    assert not check_fibonacci([])


def test_negative_fibonacci_2():
    """Testing that empty list give False"""
    assert not check_fibonacci([0, 1, 1, 5])


def test_negative_fibonacci_3():
    """Testing that empty list give False"""
    assert not check_fibonacci([-1])


def test_negative_fibonacci_4():
    """Testing that empty list give False"""
    assert not check_fibonacci([8, 13, -1])
