with open("input") as input:
    safe_count = 0
    levels = []
    for line in input:
        nums = line.strip().split(" ")
        i_nums = []
        for n in nums:
            i_nums.append(int(n))
        levels.append(i_nums)
    for level in levels:
        direction = 0
        if level[0] < level[1]:
            direction = 1
        else:
            direction = -1
        for i in range(1, len(level)):
            if direction == 1:
                if level[i] <= level[i - 1]:
                    direction = 0
                    break
            elif direction == -1:
                if level[i] >= level[i - 1]:
                    direction = 0
                    break
            if abs(level[i] - level[i - 1]) > 3:
                direction = 0
                break
        if direction != 0:
            safe_count += 1
    print(safe_count)

