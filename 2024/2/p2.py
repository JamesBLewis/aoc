import copy

def is_safe(level: list):
    direction = 0
    if level[0] < level[1]:
        direction = 1
    else:
        direction = -1
    for i in range(1, len(level)):
        if direction == 1:
            if level[i] <= level[i - 1]:
                return False
        elif direction == -1:
            if level[i] >= level[i - 1]:
                return False
        if abs(level[i] - level[i - 1]) > 3:
            return False
    return True

def can_be_made_safe(level: list):
    for i in range(len(level)):
        level_copy = copy.copy(level)
        level_copy.pop(i)
        if is_safe(level_copy):
            return True
    return False

with open("input") as input:
    safe_count = 0
    levels = []
    for line in input:
        nums = line.strip().split(" ")
        i_nums = []
        for n in nums:
            i_nums.append(int(n))
        levels.append(i_nums)
    new_levels = []
    for level in levels:
        if is_safe(level):
            safe_count += 1
        elif can_be_made_safe(level):
            safe_count += 1
    print(safe_count)

# 681 wrong