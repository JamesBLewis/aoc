from helpers.helpers import parse_txt_to_2d_array, valid_grid_pos

word_search = parse_txt_to_2d_array("input")

def find_xmas(i, j):
    if i < 1 or i >= len(word_search) - 1 or j < 1 or j >= len(word_search[0]) - 1:
        return 0
    for h in [1, -1]:
        if word_search[i-1][ j + h] == "S":
            if word_search[i+1][ j - h] != "M":
                return 0
        elif word_search[i-1][ j + h] == "M":
            if word_search[i+1][ j - h] != "S":
                return 0
        else:
            return 0
    return 1


hits = 0
for i in range(len(word_search)):
    new_hits = 0
    for j in range(len(word_search)):
        possible_word = 0
        # see if xmas begins here
        if word_search[i][j] == "A":
            new_hits += find_xmas(i, j)
    hits += new_hits
    print(new_hits)
print(hits)


# incorrect 1904