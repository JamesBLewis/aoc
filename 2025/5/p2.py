from helpers.helpers import parse_txt_to_2d_array, all_valid_adjacent_cells

words = parse_txt_to_2d_array("input")
split = 0
for i, word in enumerate(words):
    if word == '':
        split = i
        break
ranges = words[:split]
ids = words[split + 1:]
#print(ranges)
parsed_range = []
for r in ranges:
    parsed_range.append(r.split('-'))
parsed_range = sorted(parsed_range, key=lambda x: int(x[0]))
print(parsed_range)
for i, str_num in enumerate(parsed_range[:-1]):
    num = int(str_num[1])
    if num >= int(parsed_range[i + 1][0]):
        parsed_range[i][1], parsed_range[i + 1][1] = int(parsed_range[i + 1][0]) - 1, max(int(parsed_range[i][1]), int(parsed_range[i + 1][1]))

count = 0
for r in parsed_range:
    print(r)
    diff = int(r[1]) - int(r[0]) + 1
    count += diff
    print('diff for ', r, ' was ', diff)
print(count)
# 332385323899380 is too low
# 367899984917516