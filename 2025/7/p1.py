import math

from helpers.helpers import parse_txt_to_2d_array, valid_grid_pos

words = parse_txt_to_2d_array("input")
words =  [list(s) for s in words]
counter = 0
for i in range(len(words)):
    for j, cell in enumerate(words[i]):
        #print(words[i])
        if cell == '^':
            if valid_grid_pos(words, i - 1, j):
                if words[i - 1][j] not in ['|', 'S']:
                    continue
            left = j - 1
            right = j + 1
            counter += 1
            if valid_grid_pos(words, i, left):
                if words[i][j - 1] == '.':
                    words[i][j - 1] = '|'
            if valid_grid_pos(words, i, right):
                if words[i][j + 1] == '.':
                    words[i][j + 1] = '|'
        else:
            if valid_grid_pos(words, i - 1, j):
                if words[i - 1][j] not in ['|', 'S']:
                    continue
                words[i][j] = '|'
for i in range(len(words)):
    print(''.join(words[i]))
print(counter)