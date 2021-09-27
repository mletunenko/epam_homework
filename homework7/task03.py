"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""
from typing import List


def get_coords(board: List[List], symbol: str) -> set:
    coords_set = set()
    counter_coords = 1
    for string in board:
        for element in string:
            if element == symbol:
                coords_set.add(counter_coords)
            counter_coords += 1
    return coords_set


def tic_tac_toe_checker(board: List[List]) -> str:
    win_cases = ({1, 2, 3}, {4, 5, 6}, {7, 8, 9},
                 {1, 4, 7}, {2, 5, 8}, {3, 6, 9},
                 {1, 5, 9}, {3, 5, 7})
    x_team_coords = get_coords(board, 'x')
    o_team_coords = get_coords(board, 'o')
    empty_coords = get_coords(board, '-')
    if len(x_team_coords) >= 3 or len(o_team_coords):
        for case in win_cases:
            if case.issubset(x_team_coords):
                return ('x wins!')
            if case.issubset(o_team_coords):
                return ('o wins!')
    if len(empty_coords) > 0:
        return ('unfinished!')
    else:
        return ('draw!')
