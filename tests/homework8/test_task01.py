import pytest

from homework8.task01 import KeyValueStorage


def test_key_value_storage_get_item():
    storage = KeyValueStorage('tests/homework8/example.txt')
    assert storage['name'] == 'kek'


def test_key_value_storage_built_in_attr_conflict():
    storage = KeyValueStorage('tests/homework8/example.txt')
    atr_before = storage.__str__()
    storage.__str__ = 123
    atr_after = storage.__str__()
    assert atr_before == atr_after


def test_key_value_storage_integer_key_tmpdir(tmpdir):
    temporary_file = tmpdir.join('something.txt')
    temporary_file.write('1=qwerty')
    with pytest.raises(ValueError):
        KeyValueStorage(temporary_file)
