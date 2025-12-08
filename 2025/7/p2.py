import functools
import math

from helpers.helpers import parse_txt_to_2d_array, valid_grid_pos

words = parse_txt_to_2d_array("input")
words =  [list(s) for s in words]

@functools.lru_cache(maxsize=None)
def dfs(row: int, col: int) -> int:
    # invariant: there must be a leading into us
    if not valid_grid_pos(words, row, col):
        # is the col at least in bounds?
        if 0 <= col < len(words[0]):
            return 1
        return 0
    if words[row][col] == '^':
        return dfs(row, col - 1) + dfs(row, col + 1)
    else:
        return dfs(row + 1, col)


# find the start of the beam
for i, char in enumerate(words[0]):
    if char == 'S':
        print(dfs(1, i))
        break
