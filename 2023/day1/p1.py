import copy

sol1_lines = []
sol2_lines = []


def solution1():
    valid_digits = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6",
                    "seven": "7", "eight": "8", "nine": "9"}
    input = [[]]
    with open('input.txt') as f:
        for line in f:
            input.append(line.strip('\n'))
    input = input[1:]
    total = 0
    for i in range(len(input)):
        chars = []
        upper_bound = 0
        # while upper_bound < len(input[i]):
        #     for key in valid_digits:
        #         if key in input[i][:upper_bound]:
        #             input[i] = input[i][:upper_bound].replace(key, valid_digits[key]) + input[upper_bound+1:]
        #         else:
        #

        #        upper_bound += 1
        for j in range(len(input[i])):
            for key in valid_digits:
                output = input[i][j:min(j + 5, len(input[i]))].replace(key, valid_digits[key])
                input[i] = input[i][:j] + output + input[i][min(j + 5, len(input[i])):]
        for letter in input[i]:
            if letter in "0123456789":
                chars.append(letter)
        sol1_lines.append(int(chars[0] + chars[-1]))
        total += int(chars[0] + chars[-1])
    print(total)


def solution2():
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
                    if key in input2[i][len(input2[i]) - len(key):]:
                        end = valid_digits[key]
                        update = True
                        break
            if update:
                break
            input2[i] = input2[i][:-1]

        total += int(start + end)
        sol2_lines.append(start + end)
    print(total)

