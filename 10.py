with open("text_files/10.txt", "r") as f:
    text = f.read()
    
# --- PART ONE --- #
# --- PART TWO --- #
# did both parts cuz it is literally one line of difference in the code.
text_strip = text.rstrip("\n")
text_split = [list(line) for line in text_strip.split("\n")]

def expand(index_row, index_column, cur_num, text_split):
    if index_row < 0 or index_row >= len(text_split) or index_column < 0 or index_column >= len(text_split[0]):
        raise IndexError("Index out of bounds")
    expanded_list = []
    #UP
    if index_row - 1 >= 0:
        if text_split[index_row - 1][index_column] == str(int(cur_num) + 1):
            expanded_list.append((index_row - 1, index_column, str(int(cur_num) + 1)))
    #DOWN
    if index_row + 1 < len(text_split):
        if text_split[index_row + 1][index_column] == str(int(cur_num) + 1):
            expanded_list.append((index_row + 1, index_column, str(int(cur_num) + 1)))
    #LEFT
    if index_column - 1 >= 0:
        if text_split[index_row][index_column - 1] == str(int(cur_num) + 1):
            expanded_list.append((index_row, index_column - 1, str(int(cur_num) + 1)))
    #RIGHT
    if index_column + 1 < len(text_split[0]):
        if text_split[index_row][index_column + 1] == str(int(cur_num) + 1):
            expanded_list.append((index_row, index_column + 1, str(int(cur_num) + 1)))
            
    return expanded_list
    
        

xy_locations_of_0 = [divmod(i, len(text_split[0])) for i, char in enumerate(text_strip.replace("\n", "")) if char == '0']
som_part_1 = 0
som_part_2 = 0
for (x, y) in xy_locations_of_0:
    expandable_list = []
    new_x_y_num_list = expand(x, y, '0', text_split)
    expandable_list += new_x_y_num_list
    final_list = []
    for (x, y, num) in expandable_list:
        if num == "9":
            final_list.append((x, y))
            continue
        new_x_y_num_list = expand(x, y, num, text_split)
        expandable_list += new_x_y_num_list
    
    som_part_1 += len(set(final_list))
    som_part_2 += len(final_list)
    
print(som_part_1)
print(som_part_2)