# 12 red cubes, 13 green cubes, and 14 blue cubes?
from helpers.helpers import parse_txt_to_2d_array, all_valid_adjacent_cells

input = parse_txt_to_2d_array('input.txt')
for i in range(len(input)):
    input[i] = input[i].split(':')[1]
    input[i] = input[i].split('|')
    for j in range(len(input[i])):
        input[i][j] = input[i][j].strip(' ').split(' ')

total_score = 0

for card in input:
    score = 0
    winning_nums = card[0]
    your_nums = card[1]
    for num in your_nums:
        if num != '' and num in winning_nums:
            if score > 0:
                score *= 2
            else:
                score = 1
    total_score += score

print(total_score)
# 24160