from homework7.task01 import find_occurrences


def test_find_occurrences_int():
    tree = {
        'first': [
            'second_layer', {
                1, True, 'string'
            }
        ]
    }
    assert find_occurrences(tree, 1) == 1


def test_find_occurrences_bool():
    tree = {
        'first': [
            'second_layer', {
                1, True, 'string'
            }
        ]
    }
    assert find_occurrences(tree, True) == 1


def test_find_occurrences_str():
    tree = {
        'first': [
            'second_layer', {
                1, True, 'string'
            }
        ]
    }
    assert find_occurrences(tree, 'string') == 1


def test_find_occurrences_non_existent():
    tree = {
        'first': [
            'second_layer', {
                1, True, 'string'
            }
        ]
    }
    assert find_occurrences(tree, "True") == 0
