import math

from helpers.helpers import valid_grid_pos

parsed_numbers = []
with open("input") as f:
    lines = f.readlines()
    for line in lines:
        if line:
            parsed_numbers.append(line.rstrip('\n'))

#print(parsed_numbers)
new_math = []
last_operator = ''
for i in range(len(parsed_numbers[0])):
    equation = []
    for j in range(len(parsed_numbers)):
        if not valid_grid_pos(parsed_numbers, j, i):
            continue
        try:
            int(parsed_numbers[j][i])
            equation.append(parsed_numbers[j][i])
        except Exception:
            if parsed_numbers[j][i] in ['+', '*']:
                last_operator = parsed_numbers[j][i]
            pass
    new_math.append((equation, last_operator))
#print(new_math)

total = 0
#print('size:', size)
running_total = 0
print(new_math)
for i, problem in enumerate(new_math):
    if len(problem[0]) > 0:
        number_str = ''.join(problem[0])
        operator = problem[1]
        #print('number:', number_str)
        if operator == '+':
            running_total += int(number_str)
        elif operator == '*':
            running_total = max(1, running_total)
            running_total *= int(number_str)
        else:
            raise ValueError('Invalid operator: ', operator)
        #print('running total:', running_total)
    else:
        total += running_total
        print('running total: ', running_total)
        print('total: ', total)
        running_total = 0
total += running_total
print('running total: ', running_total)
print('total: ', total)
print(total)