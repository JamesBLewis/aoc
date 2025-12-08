import math

from helpers.helpers import parse_txt_to_2d_array, build_counter_for_input

input = parse_txt_to_2d_array('input.txt')

proximity_map = build_counter_for_input(input)

# mark all digits on the proximity_map as the overall number
for i in range(len(input)):
    j, num = 0, ''
    while j < len(input[i]):
        if input[i][j] in '1234567890':
            num += input[i][j]
            # parse remaining num and skip j ahead
            while j + 1 < len(input[0]) and input[i][j+1] in '1234567890':
                num += input[i][j+1]
                j += 1
            # go back through these digits and mark them as this part on the proximity_map
            k = 0
            while k < len(num):
                proximity_map[i][j - k] = int(num)
                k += 1
        num = ''
        j += 1

gear_ratio_sum = 0

for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == '*':
            nearby_parts = []
            for row in [i, i + 1, i - 1]:
                for col in [j, j + 1, j - 1]:
                    if -1 < row < len(input) and -1 < col < len(input[0]) and proximity_map[row][col] != -1:
                        if proximity_map[row][col] not in nearby_parts:
                            nearby_parts.append(proximity_map[row][col])
            if len(nearby_parts) == 2:
                gear_ratio_sum += math.prod(nearby_parts)
print(gear_ratio_sum)