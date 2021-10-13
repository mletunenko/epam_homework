from homework9.task03 import universal_file_counter


def test_universal_file_counter_without_tokenizer():
    assert universal_file_counter('/Users/maria/epam/epam_homework/'
                                  'tests/homework9', 'txt') == 4


def test_universal_file_counter_with_tokenizer():
    assert universal_file_counter('/Users/maria/epam/epam_homework/'
                                  'tests/homework9', 'txt', str.split) == 10


def test_universal_file_counter_no_goal_files_in_dir():
    assert universal_file_counter('/Users/maria/epam/epam_homework/'
                                  'tests/homework9', 'json', str.split) == 0
