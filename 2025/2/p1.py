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
        if len(i_str) % 2 == 0:
            #print("even", i)
            #print(i_str[0:len(i_str)//2])
            if len(i_str) == 2:
                if i_str[0] == i_str[1]:
                    sum += i
            elif i_str[0:len(i_str)//2] == i_str[len(i_str)//2:]:
                sum += i
print(sum)