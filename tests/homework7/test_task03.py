from homework7.task03 import tic_tac_toe_checker


def test_checker_empty_board():
    example = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]
    assert tic_tac_toe_checker(example) == 'unfinished!'


def test_checker_empty_x_wins():
    example = [
        ['x', '-', 'o'],
        ['-', 'x', '-'],
        ['o', '-', 'x']
    ]
    assert tic_tac_toe_checker(example) == 'x wins!'


def test_checker_empty_o_wins():
    example = [
        ['x', '-', 'o'],
        ['-', 'o', '-'],
        ['o', '-', 'x']
    ]
    assert tic_tac_toe_checker(example) == 'o wins!'


def test_checker_empty_draw():
    example = [
        ['o', 'x', 'o'],
        ['x', 'x', 'o'],
        ['o', 'o', 'x']
    ]
    assert tic_tac_toe_checker(example) == 'draw!'
