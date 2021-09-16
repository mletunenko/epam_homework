from homework5.task02 import print_result


def test_deco_print_save_doc():
    @print_result
    def func():
        """Some doc"""
        return 3

    assert func.__doc__ == 'Some doc'


def test_deco_print_save_name():
    @print_result
    def func():
        return 3

    assert func.__name__ == 'func'


def test_deco_print_save_function():
    @print_result
    def func():
        """Some doc"""
        return id(func)

    assert func() == id(func)
