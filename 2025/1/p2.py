from helpers.helpers import parse_txt_to_2d_array

words = parse_txt_to_2d_array("input")
current = 50
ticks = 0
for word in words:
    direction = word[0]
    count = int(word[1:])
    for _ in range(count):
        if direction == "L":
            current -= 1
        elif direction == "R":
            current += 1
        if current < 0:
            current += 100
        elif current > 99:
            current -= 100
        if current == 0:
            ticks += 1
    print(current, ticks)
print(ticks)
# 7437
# 7446
# 6974
# 7371?????
# 6911
# 6892