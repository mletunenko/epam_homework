# supressor_generator
import io

from homework9.task02 import SupressorClass


def test_supressor_class_index_error():
    with SupressorClass(IndexError):
        assert [][2] is None


def test_supressor_class_file_not_found_error():
    with SupressorClass(FileNotFoundError):
        f = open('some_path.txt', 'w')
        assert isinstance(f, io.TextIOWrapper)
