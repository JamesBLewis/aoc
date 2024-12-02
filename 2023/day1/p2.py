# load content of input.txt into a 2d list
# input = [[]]
# with open('input.txt') as f:
#     index_pointer = 0
#     for line in f:
#         if line == '\n':
#             input.append([])
#             index_pointer += 1
#         else:
#             input[index_pointer].append(int(line.strip('\n')))
# max_food = 0
# for elf in input:
#     max_food = max(max_food, sum(elf))
# print(max_food)
import copy

valid_digits = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
                "eight": "8", "nine": "9"}
input = [[]]
with open('input.txt') as f:
    for line in f:
        input.append(line.strip('\n'))
input = input[1:]
total = 0

input1 = copy.deepcopy(input)
input2 = copy.deepcopy(input)

for i in range(len(input1)):
    start = "0"
    end = "0"
    while len(input1[i]) > 0:
        update = False
        if input1[i][0] in "0123456789":
            start = input1[i][0]
            update = True
        else:
            for key in valid_digits:
                if key in input1[i][:len(key)]:
                    start = valid_digits[key]
                    update = True
                    break
        if update:
            break
        input1[i] = input1[i][1:]

    while len(input2[i]) > 0:
        update = False
        if input2[i][-1] in "0123456789":
            end = input2[i][-1]
            update = True
        else:
            for key in valid_digits:
                if key in input2[i][len(input2[i])-len(key):]:
                    end = valid_digits[key]
                    update = True
                    break
        if update:
            break
        input2[i] = input2[i][:-1]

    total += int(start + end)
    print(int(start + end))
print(total)




# 54953
# 54925