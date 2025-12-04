from helpers.helpers import parse_txt_to_2d_array, valid_grid_pos

words = parse_txt_to_2d_array("input")
sum = 0

class Num:
    def __init__(self, val: int, idx: int):
        self.val = val
        self.idx = idx

for bank in words:
    largest = Num(0, 0)
    second_largest = Num(0, 0)
    for i, num in enumerate(bank):
        if int(num) > largest.val:
            if i + 1 != len(bank):
                second_largest = Num(0,0)
                largest = Num(int(num), i)
            else:
                second_largest = Num(int(num), i)
        elif int(num) > second_largest.val:
            second_largest = Num(int(num), i)
    sum += int(str(largest.val) + str(second_largest.val))
print(sum)