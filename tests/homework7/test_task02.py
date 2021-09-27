from homework7.task02 import backspace_compare


def test_backspace_compare_true_case():
    assert backspace_compare("ab#c", "ad#c") is True


def test_backspace_compare_false_case():
    assert backspace_compare("ab#c00", "ad#crr") is False
