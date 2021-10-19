import sqlite3 as sq

import pytest

from homework8.task02 import TableData


def test_tabledata_get_len():
    presidents = TableData('tests/homework8/example.sqlite', 'presidents')
    assert len(presidents) == 3


def test_tabledata_getitem():
    presidents = TableData('tests/homework8/example.sqlite', 'presidents')
    assert presidents['Yeltsin'] == 999


def test_tabledata_iter():
    books = TableData('tests/homework8/example.sqlite', 'books')
    books_iterator = iter(books)
    assert next(books_iterator)


@pytest.fixture
def delete_new_row():
    yield None
    with sq.connect('tests/homework8/example.sqlite') as connect:
        cursor = connect.cursor()
        cursor.execute('DELETE FROM books WHERE author="King"')


def test_tabledata_new_row(delete_new_row):
    books = TableData('tests/homework8/example.sqlite', 'books')
    with sq.connect(books.database_name) as connect:
        cursor = connect.cursor()
        len_before = len(books)
        cursor.execute(
            f'INSERT INTO {books.table_name} VALUES ("It", "King")'
        )
        connect.commit()
        len_after = len(books)
        assert len_after == len_before + 1
