from homework3.task04 import is_armstrong


# Common positive test
def test_is_armstrong_positive():
    assert is_armstrong(370) is True


# Common negative test
def test_is_armstrong_negative():
    assert is_armstrong(10) is False
