import tempfile

import pytest

from homework4.task01 import read_magic_number


def test_read_magic_number_positive_true():
    with tempfile.NamedTemporaryFile(mode='w') as file:
        file.write('1')
        file.flush()
        assert read_magic_number(file.name) is True


def test_read_magic_number_positive_false():
    with tempfile.NamedTemporaryFile(mode='w') as file:
        file.write('6')
        file.flush()
        assert read_magic_number(file.name) is False


def test_read_magic_number_negative_text_file():
    with tempfile.NamedTemporaryFile(mode='w') as file:
        file.write('Hello')
        file.flush()
        with pytest.raises(ValueError):
            read_magic_number(file.name)


def test_read_magic_number_negaative_empty_file():
    with tempfile.NamedTemporaryFile(mode='w') as file:
        with pytest.raises(ValueError):
            read_magic_number(file.name)
