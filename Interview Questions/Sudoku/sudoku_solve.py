# sudokusolve.py
""" Sudoku Solver
    Note: A description of the sudoku puzzle can be found at:

        https://en.wikipedia.org/wiki/Sudoku

    Given a string in SDM format, described below, write a program to find and
    return the solution for the sudoku puzzle in the string. The solution should
    be returned in the same SDM format as the input.

    Some puzzles will not be solvable. In that case, return the string
    "Unsolvable".

    The general SDM format is described here:

        http://www.sudocue.net/fileformats.php

    For our purposes, each SDM string will be a sequence of 81 digits, one for
    each position on the sudoku puzzle. Known numbers will be given, and unknown
    positions will have a zero value.

    For example, assume you're given this string of digits (split into two lines
    for readability):

        0040060790000006020560923000780610305090004
             06020540890007410920105000000840600100

    The string represents this starting sudoku puzzle:

             0 0 4   0 0 6   0 7 9
             0 0 0   0 0 0   6 0 2
             0 5 6   0 9 2   3 0 0

             0 7 8   0 6 1   0 3 0
             5 0 9   0 0 0   4 0 6
             0 2 0   5 4 0   8 9 0

             0 0 7   4 1 0   9 2 0
             1 0 5   0 0 0   0 0 0
             8 4 0   6 0 0   1 0 0

    The provided unit tests may take a while to run, so be patient.
"""