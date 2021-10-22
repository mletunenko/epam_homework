from homework7.task02 import backspace_compare, second_backspace_compare


def test_backspace_compare_true_case():
    assert backspace_compare("ab#c", "ad#c") is True


def test_backspace_compare_false_case():
    assert backspace_compare("ab#c00", "ad#crr") is False


def test_second_backspace_compare_true_case():
    assert second_backspace_compare("ab#c", "ad#c") is True


def test_second_backspace_compare_false_case():
    assert second_backspace_compare("ab#c00", "ad#crr") is False


def test_backspace_compare_empty_case():
    assert backspace_compare('', '') is True


def test_second_backspace_compare_empty_case():
    assert second_backspace_compare('', '') is True


def test_backspace_compare_only_backspace_case():
    assert backspace_compare('###', '#') is True


def test_second_backspace_compare_only_backspace_case():
    assert second_backspace_compare('###', '#') is True
