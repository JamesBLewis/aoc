from helpers.helpers import parse_txt_to_2d_array, valid_grid_pos

word_search = parse_txt_to_2d_array("input")
valid_words = ["XMAS", "SAMX"]

def find_xmas(i, j, which_word, index, directioni, directionj):
    if index >= len(valid_words[which_word]):
        # this word must have been matched so return true
        return 1
    if not valid_grid_pos(word_search, i, j):
        return 0
    if word_search[i][j] == valid_words[which_word][index]:
        # continue
        return find_xmas(i + directioni, j + directionj, which_word, index+1, directioni, directionj)
    return 0

hits = 0
for i in range(len(word_search)):
    new_hits = 0
    for j in range(len(word_search)):
        possible_word = 0
        # see if xmas begins here
        if word_search[i][j] == valid_words[0][0]:
            which_word = 0
        elif word_search[i][j] == valid_words[1][0]:
            which_word = 1
        else:
            continue
        # check all directions

        new_hits += find_xmas(i, j, which_word, 0, 0, 1) # horizontal
        new_hits += find_xmas(i, j, which_word, 0, 1, 0) # vertical
        new_hits += find_xmas(i, j, which_word, 0, 1, 1) # diagonal
        new_hits += find_xmas(i, j, which_word, 0, 1, -1)  # diagonal
    hits += new_hits
    print(new_hits)
print(hits)