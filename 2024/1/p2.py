with open("input") as input:
    l_list = []
    l_count = []
    r_list = []
    for line in input:
        l, r = line.split("   ")
        l_list.append(int(l))
        r_list.append(int(r))
    l_list.sort()
    r_list.sort()
    for l in l_list:
        count = 0
        for r in r_list:
            if r == l:
                count += 1
        l_count.append(l * count)
    print(sum(l_count))
