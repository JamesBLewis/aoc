from helpers.helpers import parse_txt_to_2d_array, valid_grid_pos

words = parse_txt_to_2d_array("input")
sum = 0


class Num:
    val = 0
    idx = 0
    def __init__(self, val: int, idx: int):
        self.val = val
        self.idx = idx

for bank in words:
    battery = []
    # now find the largest number between largest.idx and len(bank)- (11 - N)
    for i in range(11, -1, -1):
        # base case
        largest = 0
        if i == 11:
            largest = Num(0, 0)
        # general case
        else:
            largest = Num(0, battery[-1].idx + 1)
        #print("range ", largest.idx, len(bank)-i)
        cached_largest = largest.idx + 0
        for j, num in enumerate(bank[cached_largest:len(bank)-i]):
            if int(num) > largest.val:
                new_idx = j + cached_largest
                #print("new largest ", num, new_idx, j)
                largest = Num(int(num), new_idx)
        #print("largest ", largest.val, largest.idx)
        battery.append(largest)
        #print("battery so far ", [x.val for x in battery])

    # dissolve battery and sum the compoents
    battery_val = int(''.join([str(x.val) for x in battery]))
    print(battery_val)
    sum += battery_val
print(sum)
# 171948025805102 was too low