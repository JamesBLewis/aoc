import math

from helpers.helpers import parse_txt_to_2d_array, all_valid_adjacent_cells

words = parse_txt_to_2d_array("input")
#rint(words)
problems = [[] for i in range(len(words[0].split(' ')))]
for row in words:
    split_row = row.split(' ')
    #print(split_row)
    i = 0
    while i < len(split_row):
        if split_row[i] == '':
            split_row.pop(i)
        else:
            i += 1
    for i in range(len(split_row)):
        problems[i].append(split_row[i])


total = 0
for problem in problems:
    if len(problem) > 0:
        if problem[-1] == '+':
            total += sum(map(int, problem[:-1]))
        elif problem[-1] == '*':
            total += math.prod(map(int, problem[:-1]))
print(total)