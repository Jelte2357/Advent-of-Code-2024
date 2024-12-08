with open("text_files/8.txt", "r") as f:
    text = f.read()
    
# --- PART ONE --- #
def find_all_indexes(text, sub):
    return [divmod(i, len(text.split("\n"))) for i in range(len(text.replace("\n",""))) if text.replace("\n","").startswith(sub, i)]

text_strip = text.rstrip("\n")
text_split = [list(line) for line in text_strip.split("\n")]
empty_grid = [list(line) for line in (("." * len(text_split[0])+ "\n") * len(text_split)).rstrip("\n").split("\n")]

unique_chars = set()
for char in text_strip:
    if char != "." and char != "\n":
        unique_chars.add(char)

unique_chars = sorted(list(unique_chars)) # just for my own ease of testing

for char in unique_chars:
    indexes = find_all_indexes(text_strip, char)
    for index1 in indexes:
        for index2 in indexes:
            if index1 != index2:
                try:
                    new_index = (index1[0] - (index2[0] - index1[0]), index1[1] - (index2[1] - index1[1]))
                    if new_index[0] < 0 or new_index[1] < 0:
                        raise IndexError
                    
                    if empty_grid[new_index[0]][new_index[1]] == ".":
                        empty_grid[new_index[0]][new_index[1]] = "#"
                except:
                    pass
                
print("\n".join(["".join(line) for line in empty_grid]).count("#"))

# --- PART TWO --- #
def find_all_indexes(text, sub):
    return [divmod(i, len(text.split("\n"))) for i in range(len(text.replace("\n",""))) if text.replace("\n","").startswith(sub, i)]

text_strip = text.rstrip("\n")
text_split = [list(line) for line in text_strip.split("\n")]
empty_grid = [list(line) for line in (("." * len(text_split[0])+ "\n") * len(text_split)).rstrip("\n").split("\n")]

unique_chars = set()
for char in text_strip:
    if char != "." and char != "\n":
        unique_chars.add(char)

unique_chars = sorted(list(unique_chars)) # just for my own ease of testing

for char in unique_chars:
    indexes = find_all_indexes(text_strip, char)
    for index1 in indexes:
        empty_grid[index1[0]][index1[1]] = "#" # add an antinode to every antenna
        for index2 in indexes:
            if index1 != index2:
                try:
                    mult = 1
                    while True: # add an antinode to every multiplication that fits inside of the grid.
                        new_index = (index1[0] - mult*(index2[0] - index1[0]), index1[1] - mult*(index2[1] - index1[1]))
                        if new_index[0] < 0 or new_index[1] < 0:
                            raise IndexError
                        
                        if empty_grid[new_index[0]][new_index[1]] == ".":
                            empty_grid[new_index[0]][new_index[1]] = "#"
                        mult += 1
                except:
                    pass

print("\n".join(["".join(line) for line in empty_grid]).count("#"))