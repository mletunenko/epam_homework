import tempfile

from homework1.task03 import find_maximum_and_minimum


def test_positive_find():
    """Common positive testcase"""
    with tempfile.NamedTemporaryFile(mode='w') as temporary_file:
        temporary_file.write('-1\n3\n-9\n432\n-32\n783')
        temporary_file.flush()
        assert find_maximum_and_minimum(temporary_file.name) == (-32, 783)


def test_positive_find_empty_file():
    """Testing that empty file gives None"""
    with tempfile.NamedTemporaryFile(mode='w') as temporary_file:
        assert find_maximum_and_minimum(temporary_file.name) is None


def test_positive_find_one_value():
    """Testing that file with one value gives the same maximum and minimum"""
    with tempfile.NamedTemporaryFile(mode='w') as temporary_file:
        temporary_file.write('-1')
        temporary_file.flush()
        assert find_maximum_and_minimum(temporary_file.name) == (-1, -1)
