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

count = 0
for id_row in ids:
    id_num = int(id_row)
    for rng in parsed_range:
        if int(rng[0]) <= id_num <= int(rng[1]):
            count += 1
            break
print(count)