from homework1.task03 import find_maximum_and_minimum
import tempfile


def test_positive_find():
    """Common testcase"""
    fd, path = tempfile.mkstemp(suffix='.txt', text=True)
    with open(path, 'w') as fpw:
        fpw.write('-1\n3\n-9\n432\n-32\n783')
    assert find_maximum_and_minimum(path) == (-32, 783)
