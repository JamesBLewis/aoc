with open("input") as input:
    sum = 0
    l_list = []
    r_list = []
    for line in input:
        l, r = line.split("   ")
        l_list.append(int(l))
        r_list.append(int(r))
    l_list.sort()
    r_list.sort()
    for i in range(len(l_list)):
        sum += (max(l_list[i], r_list[i]) - min(l_list[i], r_list[i]))
    print(sum)