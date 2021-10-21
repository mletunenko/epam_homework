from homework11.task01 import SimplifiedEnum


def test_color_enum_key():
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")

    assert ColorsEnum.RED == 'RED'


def test_color_enum_non_key():
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")
        HOME = 'WORK'

    assert ColorsEnum.HOME == 'WORK'
