import tempfile
from collections import Iterator
from pathlib import Path

from homework9.task01 import merge_sorted_files, merge_sorted_files_float


def test_merge_sorted_str_source():
    with tempfile.NamedTemporaryFile(mode='w+t') as temp_file1:
        temp_file1.write("""
        43
        1
        65
        """)
        temp_file1.flush()
        with tempfile.NamedTemporaryFile(mode='w+t') as temp_file2:
            temp_file2.write("""
            -9
            12
            0
            """)
            temp_file2.flush()
            assert list(
                merge_sorted_files([temp_file2.name, temp_file1.name])) == \
                [-9, 0, 1, 12, 43, 65]


def test_merge_sorted_path_source():
    with tempfile.NamedTemporaryFile(mode='w+t') as temp_file1:
        temp_file1.write("""
        43
        1
        65
        """)
        temp_file1.flush()
        with tempfile.NamedTemporaryFile(mode='w+t') as temp_file2:
            temp_file2.write("""
            -9
            12
            0
            """)
            temp_file2.flush()
            assert list(merge_sorted_files(
                [Path(temp_file2.name), Path(temp_file1.name)])) == \
                [-9, 0, 1, 12, 43, 65]


def test_merge_sorted_iterator_output():
    with tempfile.NamedTemporaryFile(mode='w+t') as temp_file1:
        temp_file1.write("""
        43
        1
        65
        """)
        temp_file1.flush()
        result = merge_sorted_files([temp_file1.name])
        assert isinstance(result, Iterator)


def test_merge_sorted_output_is_sort():
    with tempfile.NamedTemporaryFile(mode='w+t') as temp_file1:
        temp_file1.write("""
        76
        -1
        0
        """)
        temp_file1.flush()
        assert list(merge_sorted_files([temp_file1.name])) == [-1, 0, 76]


def test_merge_sorted_float_digit():
    with tempfile.NamedTemporaryFile(mode='w+t') as temp_file1:
        temp_file1.write("""
        1.2
        -1
        0
        """)
        temp_file1.flush()
        assert list(merge_sorted_files_float([temp_file1.name])) == [-1, 0,
                                                                     1.2]
