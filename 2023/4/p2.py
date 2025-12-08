from helpers.helpers import parse_txt_to_2d_array, all_valid_adjacent_cells

input = parse_txt_to_2d_array('input.txt')
for i in range(len(input)):
    input[i] = input[i].split(':')[1]
    input[i] = input[i].split('|')
    for j in range(len(input[i])):
        input[i][j] = input[i][j].strip(' ').split(' ')

cards_cache = {}

for i in range(len(input)-1, -1, -1):
    temp_score = 0
    winning_nums = input[i][0]
    your_nums = input[i][1]
    for num in your_nums:
        if num != '' and num in winning_nums:
            temp_score += 1
    cards_cache[i] = 1
    for j in range(temp_score):
            cards_cache[i] += cards_cache[i + j + 1]

print(cards_cache)

total = 0
for item in cards_cache:
    total += cards_cache[item]
print(total)