def parse_txt_to_2d_array(filename: str) -> list[str]:
    with open(filename) as f:
        return [line.strip('\n') for line in f]


def valid_grid_pos(grid: list[list], row: int, col: int) -> bool:
    return -1 < row < len(grid) and -1 < col < len(grid[0])


def build_counter_for_input(input_map: list[list], default=-1) -> list[list]:
    return [[default] * len(input_map[0]) for _ in range(len(input_map))]


def all_adjacent_cells(row: int, col: int, include_diagonal=True) -> list[tuple[int, int]]:
    directions = [(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1] if include_diagonal or i == 0 or j == 0]
    return [(row + i, col + j) for i, j in directions if i != 0 or j != 0]


def all_valid_adjacent_cells(twoD_list: list[any], row: int, col: int, include_diagonal=True) -> list[
    tuple[int, int]]:
    is_valid = lambda i, j: valid_grid_pos(twoD_list, i, j)
    return filter(lambda x: is_valid(*x), all_adjacent_cells(row, col, include_diagonal))
