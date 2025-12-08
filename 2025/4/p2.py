from helpers.helpers import parse_txt_to_2d_array, all_valid_adjacent_cells

words_old = parse_txt_to_2d_array("input")
words_array = [list(s) for s in words_old]

total_paper_removed = 0
something_was_removed = True

while something_was_removed:
    #print('loop')
    something_was_removed = False
    for i in range(len(words_array)):
        #print('len(words_array[0]) ', len(words_array[0]))
        for j in range(len(words_array[0])):
            if words_array[i][j] == '@':
                counter = 0
                for row, col in all_valid_adjacent_cells(words_array, i, j):
                    if words_array[row][col] == '@':
                        counter += 1
                if counter < 4:
                    words_array[i][j] = 'x'
                    total_paper_removed += 1
                    something_was_removed = True
print(total_paper_removed)