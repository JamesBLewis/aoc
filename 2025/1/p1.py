from helpers.helpers import parse_txt_to_2d_array, valid_grid_pos

# with open("input") as input:
words = parse_txt_to_2d_array("input")
current = 50
ticks = 0
for word in words:
    direction = word[0]
    count = word[1:]
    if direction == "L":
        current = ( current - int(count) ) % 100
    elif direction == "R":
        current = ( current + int(count) ) % 100
    print(current)
    if current == 0:
        ticks += 1

print(ticks)