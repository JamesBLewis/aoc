# 12 red cubes, 13 green cubes, and 14 blue cubes?
from helpers.helpers import parse_txt_to_2d_array, all_valid_adjacent_cells

input = parse_txt_to_2d_array('input.txt')


def valid_part(i, j):
    # check up down left right and diagonal to see if symbol is valid
    for row, col in all_valid_adjacent_cells(input, i, j):
        if input[row][col] not in '1234567890.':
            return True
    return False

print(input)
running_sum = 0
for i in range(len(input)):
    j, num = 0, ''
    while j < len(input[i]):
        if input[i][j] in '1234567890':
            num += input[i][j]
            if valid_part(i, j):
                # parse remaining num and skip j ahead
                while j + 1 < len(input[0]) and input[i][j+1] in '1234567890':
                    num += input[i][j+1]
                    j += 1
                running_sum += int(num)
        else:
            num = ''
        j += 1
print(running_sum)


# 528817
# 528819