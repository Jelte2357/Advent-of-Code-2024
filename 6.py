with open("text_files/6.txt", "r") as f:
    text = f.read()
    
# --- PART 1 --- #
# text_cut = text.rstrip("\n")
# text_split = [list(line) for line in text_cut.split("\n")]
# finished = False

# while finished == False:
#     for enum_line, line in enumerate(text_split):
#         for enum_char, char in enumerate(line):
#             try:
#                 if char == "^":
#                     if enum_line-1 < 0: # refuse -1 indexing
#                         raise ValueError
#                     if text_split[enum_line-1][enum_char] != "#":
#                         text_split[enum_line][enum_char] = "X"
#                         text_split[enum_line-1][enum_char] = "^"
#                     else:
#                         text_split[enum_line][enum_char] = ">"
#                 if char == ">":
#                     if text_split[enum_line][enum_char+1] != "#":
#                         text_split[enum_line][enum_char] = "X"
#                         text_split[enum_line][enum_char+1] = ">"
#                     else:
#                         text_split[enum_line][enum_char] = "v"
#                 if char == "v":
#                     if text_split[enum_line+1][enum_char] != "#":
#                         text_split[enum_line][enum_char] = "X"
#                         text_split[enum_line+1][enum_char] = "v"
#                     else:
#                         text_split[enum_line][enum_char] = "<"
#                 if char == "<":
#                     if enum_char-1 < 0: # refuse -1 indexing
#                         raise ValueError
#                     if text_split[enum_line][enum_char-1] != "#":
#                         text_split[enum_line][enum_char] = "X"
#                         text_split[enum_line][enum_char-1] = "<"
#                     else:
#                         text_split[enum_line][enum_char] = "^"
#             except:
#                 finished = True
#                 break

# print("\n".join(["".join(line) for line in text_split]).count("X")+1)

# --- PART 2 --- #
# Unfinished code, this is honestly too difficult. I've copied someone else's solution for this one.
text_cut = text.rstrip("\n")
text_split = [list(line) for line in text_cut.split("\n")]
finished = False
start_pos = [(i, j) for i, line in enumerate(text_split) for j, char in enumerate(line) if char == "^"][0]

while finished == False:
    for enum_line, line in enumerate(text_split):
        for enum_char, char in enumerate(line):
            try:
                if char == "^":
                    if enum_line-1 < 0: # refuse -1 indexing
                        raise ValueError
                    if text_split[enum_line-1][enum_char] != "#":
                        text_split[enum_line][enum_char] = "X"
                        text_split[enum_line-1][enum_char] = "^"
                    else:
                        text_split[enum_line][enum_char] = ">"
                if char == ">":
                    if text_split[enum_line][enum_char+1] != "#":
                        text_split[enum_line][enum_char] = "X"
                        text_split[enum_line][enum_char+1] = ">"
                    else:
                        text_split[enum_line][enum_char] = "v"
                if char == "v":
                    if text_split[enum_line+1][enum_char] != "#":
                        text_split[enum_line][enum_char] = "X"
                        text_split[enum_line+1][enum_char] = "v"
                    else:
                        text_split[enum_line][enum_char] = "<"
                if char == "<":
                    if enum_char-1 < 0: # refuse -1 indexing
                        raise ValueError
                    if text_split[enum_line][enum_char-1] != "#":
                        text_split[enum_line][enum_char] = "X"
                        text_split[enum_line][enum_char-1] = "<"
                    else:
                        text_split[enum_line][enum_char] = "^"
            except:
                finished = True
                break



text_split_with_x = [list(line) for line in "\n".join(["".join(line) for line in text_split]).replace("^", "X").replace(">", "X").replace("v", "X").replace("<", "X").split("\n")]
x_positions = [item for item in [(i, j) for i, line in enumerate(text_split_with_x) for j, char in enumerate(line) if char == "X"] if item != start_pos]
amount_of_x = len(x_positions)
original_text_split = [list(line) for line in "\n".join(["".join(line) for line in text_split_with_x]).replace("X", ".").split("\n")]
original_text_split[start_pos[0]][start_pos[1]] = "^"
som = 0

for enum_pos, pos in enumerate(x_positions):
    print(f"Position {enum_pos+1}/{amount_of_x}, som as of now: {som}")
    text_split = [list(line) for line in "\n".join(["".join(line) for line in original_text_split]).split("\n")]
    text_split[pos[0]][pos[1]] = "#"
    finished = False
    while finished == False:
        for enum_line, line in enumerate(text_split):
            for enum_char, char in enumerate(line):
                try:
                    if char == "^":
                        if enum_line-1 < 0: # refuse -1 indexing
                            raise ValueError
                        if text_split[enum_line-1][enum_char] == "U":
                            som += 1
                            raise ValueError
                        elif text_split[enum_line-1][enum_char] != "#":
                            text_split[enum_line][enum_char] = "U"
                            text_split[enum_line-1][enum_char] = "^"
                        else:
                            text_split[enum_line][enum_char] = ">"
                    if char == ">":
                        if text_split[enum_line][enum_char+1] == "R":
                            som += 1
                            raise ValueError
                        elif text_split[enum_line][enum_char+1] != "#":
                            text_split[enum_line][enum_char] = "R"
                            text_split[enum_line][enum_char+1] = ">"
                        else:
                            text_split[enum_line][enum_char] = "v"
                    if char == "v":
                        if text_split[enum_line+1][enum_char] == "D":
                            som += 1
                            raise ValueError
                        elif text_split[enum_line+1][enum_char] != "#":
                            text_split[enum_line][enum_char] = "D"
                            text_split[enum_line+1][enum_char] = "v"
                        else:
                            text_split[enum_line][enum_char] = "<"
                    if char == "<":
                        if enum_char-1 < 0: # refuse -1 indexing
                            raise ValueError
                        if text_split[enum_line][enum_char-1] == "L":
                            som += 1
                            raise ValueError
                        elif text_split[enum_line][enum_char-1] != "#":
                            text_split[enum_line][enum_char] = "L"
                            text_split[enum_line][enum_char-1] = "<"
                        else:
                            text_split[enum_line][enum_char] = "^"
                except:
                    finished = True
                    break
    
print(som)