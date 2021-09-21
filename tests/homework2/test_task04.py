from homework2.task04 import cache


def test_chache_sum_func():
    def func(a, b):
        return (a + b)

    cache_func = cache(func)
    some = 100, 200
    val_1 = cache_func(*some)
    val_2 = cache_func(*some)
    assert val_1 is val_2


def test_chache_complex_func():
    def func(a, b, c):
        return (a * b) ** 2 + c

    cache_func = cache(func)
    some = 10, 2, 10
    val_1 = cache_func(*some)
    val_2 = cache_func(*some)
    assert val_1 is val_2
