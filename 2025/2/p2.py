import math
import re

from helpers.helpers import parse_txt_to_2d_array, valid_grid_pos

words = parse_txt_to_2d_array("input")
sum = 0
ranges = []
for word in words:
    ranges += word.split(',')
clean_range = []
for word in ranges:
    if word != '':
        clean_range.append(word.split('-'))
for rng in clean_range:
    for i in range(int(rng[0]), int(rng[1]) + 1):
        i_str = str(i)
        for j in range(1, len(i_str)):
            substring = i_str[:j]
            matches = re.findall(substring, i_str)
            if len(matches) == len(i_str) / len(substring):
                sum += i
                break

print(sum)