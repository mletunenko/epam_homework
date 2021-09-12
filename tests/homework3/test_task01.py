from homework3.task01 import cache


def test_cache_positive():
    counter = 0

    @cache(3)
    def summer(*args):
        nonlocal counter
        counter += 1
        return sum(args)

    for _ in range(6):
        assert summer(1, 2) == 3
    assert counter == 2
