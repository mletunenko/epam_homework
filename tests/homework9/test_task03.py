import tempfile
from pathlib import Path

from homework9.task03 import universal_file_counter


def test_universal_file_counter_without_tokenizer():
    with tempfile.TemporaryDirectory() as temp_directory:
        with tempfile.NamedTemporaryFile(mode='w+t', dir=temp_directory,
                                         suffix='.txt') as temp_file:
            temp_file.write("""1
            2
            4 5""")
            temp_file.flush()
            assert universal_file_counter(Path(temp_directory), 'txt') == 3


def test_universal_file_counter_with_tokenizer():
    with tempfile.TemporaryDirectory() as temp_directory:
        with tempfile.NamedTemporaryFile(mode='w+t', dir=temp_directory,
                                         suffix='.txt') as temp_file:
            temp_file.write("""1
            2
            4 5""")
            temp_file.flush()
            assert universal_file_counter(Path(temp_directory), 'txt',
                                          str.split) == 4


def test_universal_file_counter_no_goal_files_in_dir():
    with tempfile.TemporaryDirectory() as temp_directory:
        with tempfile.NamedTemporaryFile(mode='w+t', dir=temp_directory,
                                         suffix='.txt') as temp_file:
            temp_file.write("""1
            2
            4 5""")
            temp_file.flush()
            assert universal_file_counter(Path(temp_directory), 'json',
                                          str.split) == 0
