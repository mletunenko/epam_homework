"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
# >>> with supressor(IndexError):
...    [][2]
"""
from contextlib import contextmanager


class SupressorClass:

    def __init__(self, exception):
        self.exception = exception

    def __enter__(self):
        pass

    def __exit__(self, exctype, excinst, exctb):
        return exctype is not None and issubclass(exctype, self.exception)


@contextmanager
def supressor_generator(path, exception=None):
    file = None
    try:
        file = open(path)
        yield file
    except exception:
        pass
    finally:
        if file:
            file.close()
