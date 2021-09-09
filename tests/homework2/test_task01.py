import tempfile

from homework2.task01 import (count_non_ascii_chars, count_punctuation_chars,
                              get_longest_diverse_words,
                              get_most_common_non_ascii_char, get_rarest_char)


def test_get_longest_diverse_word_data_txt_test():
    assert get_longest_diverse_words('homework2/data.txt') == \
           ['unmißverständliche', 'Bevölkerungsabschub', 'Kollektivschuldiger',
            'Werkstättenlandschaft', 'Schicksalsfiguren',
            'politisch-strategischen',
            'Selbstverständlich', 'Werkstättenlandschaft',
            'résistance-Bewegungen',
            'Fingerabdrucks']


def test_get_longest_diverse_word_10_word():
    with tempfile.NamedTemporaryFile(mode='w') as temporary_file:
        temporary_file.write("""Lorem ipsum dolor sit amet, consectetur
        adipiscing elit. Nunc blandit.""")
        temporary_file.flush()
        assert set(get_longest_diverse_words(temporary_file.name)) == \
               {'Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur',
                'adipiscing', 'elit', 'Nunc', 'blandit'}


def test_get_longest_diverse_many_punctuation():
    with tempfile.NamedTemporaryFile(mode='w') as temporary_file:
        temporary_file.write("""
        @Lorem@ ipsum$% &* )(dolor": sit<>< <amet,
        ><consectetur adipiscing>< elit. Nunc^&* %^ blandit.
        """)
        temporary_file.flush()
        assert set(get_longest_diverse_words(temporary_file.name)) == \
               {'Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur',
                'adipiscing', 'elit', 'Nunc', 'blandit'}


def test_get_rarest_char_common_test():
    assert get_rarest_char('homework2/data.txt') == '›'


def test_get_rarest_char_in_single_char_file():
    with tempfile.NamedTemporaryFile(mode='w') as temporary_file:
        temporary_file.write('a')
        temporary_file.flush()
        assert get_rarest_char(temporary_file.name) == 'a'


def test_get_rarest_char_in_empty_file():
    with tempfile.NamedTemporaryFile() as temporary_file:
        assert get_rarest_char(temporary_file.name) is None


def test_count_punctuation_common_test():
    assert count_punctuation_chars('homework2/data.txt') == 5305


def test_count_punctuation_in_single_char_file():
    with tempfile.NamedTemporaryFile(mode='w') as temporary_file:
        temporary_file.write("*")
        temporary_file.flush()
        assert count_punctuation_chars(temporary_file.name) == 1


def test_count_punctuation_in_empty_file():
    with tempfile.NamedTemporaryFile() as temporary_file:
        assert count_punctuation_chars(temporary_file.name) == 0


def test_count_non_ascii_common_test():
    assert count_non_ascii_chars('homework2/data.txt') == 2972


def test_count_non_ascii_in_only_ascii_char_file():
    with tempfile.NamedTemporaryFile(mode='w') as temporary_file:
        temporary_file.write('Lorem ipsum dolor sit amet, consectetuer '
                             'adipiscing elit. Aenean commodo ligula '
                             'eget dolor.')
        temporary_file.flush()
        assert count_non_ascii_chars(temporary_file.name) == 0


def test_count_non_ascii_in_empty_file():
    with tempfile.NamedTemporaryFile() as temporary_file:
        assert count_non_ascii_chars(temporary_file.name) == 0


def test_get_most_common_non_ascii_char_common_test():
    assert get_most_common_non_ascii_char('homework2/data.txt') == 'ä'


def test_get_most_common_non_ascii_char_empty_file():
    with tempfile.NamedTemporaryFile() as empty_file:
        assert get_most_common_non_ascii_char(empty_file.name) is None


def test__get_most_common_non_ascii_char_only_ascii():
    with tempfile.NamedTemporaryFile(mode='w') as temporary_file:
        temporary_file.write('Qwerty 1234 <>?:"')
        temporary_file.flush()
        assert get_most_common_non_ascii_char(temporary_file.name) is None
