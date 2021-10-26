import pytest

from homework8.task01 import KeyValueStorage


@pytest.fixture()
def example_file(tmpdir):
    temporary_file = tmpdir.join('example_file.txt')
    temporary_file.write(
        """name=kek
        last_name=top
        power=9001
        song=shadilay"""
    )
    return temporary_file


def test_key_value_storage_get_item(example_file):
    storage = KeyValueStorage(example_file)
    assert storage['name'] == 'kek'


def test_key_value_storage_built_in_attr_conflict(example_file):
    storage = KeyValueStorage(example_file)
    atr_before = id(storage.__doc__)
    storage.__doc__ = 123
    atr_after = id(storage.__doc__)
    assert atr_before == atr_after


def test_key_value_storage_built_in_attr_no_conflict(example_file):
    storage = KeyValueStorage(example_file)
    atr_before = id(storage.__str__)
    storage.__str__ = 123
    atr_after = id(storage.__str__)
    assert atr_before != atr_after


def test_key_value_storage_integer_key_tmpdir(tmpdir):
    temporary_file = tmpdir.join('something.txt')
    temporary_file.write('1=qwerty')
    with pytest.raises(ValueError):
        KeyValueStorage(temporary_file)
