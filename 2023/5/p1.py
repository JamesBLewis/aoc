# 12 red cubes, 13 green cubes, and 14 blue cubes?
from helpers.helpers import parse_txt_to_2d_array, all_valid_adjacent_cells

input = parse_txt_to_2d_array('input.txt')
input[0] = input[0].strip('seeds: ')
cat_removed_map = [[] for _ in range(len(input))]
last_line_was_int = True
pointer = 0
for line in input:
    if len(line) > 0 and line[0] in '1234567890':
        if last_line_was_int == False:
            pointer += 1
        cat_removed_map[pointer].append(line)
        last_line_was_int = True
    else:
        last_line_was_int = False

for line_num in range(len(cat_removed_map)):
    if len(cat_removed_map[line_num]) == 0:
        cat_removed_map = cat_removed_map[:line_num]
        break


for i in range(len(cat_removed_map)):
    for j in range(len(cat_removed_map[i])):
        cat_removed_map[i][j] = cat_removed_map[i][j].split(' ')
print(cat_removed_map)

