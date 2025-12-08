from helpers.helpers import parse_txt_to_2d_array, all_valid_adjacent_cells

words = parse_txt_to_2d_array("input")
total_paper = 0
for i in range(len(words)):
    for j in range(len(words[0])):
        if words[i][j] == '@':
            counter = 0
            for row, col in all_valid_adjacent_cells(words, i, j):
                if words[row][col] == '@':
                    counter += 1
            if counter < 4:
                total_paper += 1
print(total_paper)