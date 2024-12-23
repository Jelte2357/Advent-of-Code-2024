with open("text_files/6.txt", "r") as f:
    text = f.read()
    
# --- PART 1 --- #
text_cut = text.rstrip("\n")
text_split = [list(line) for line in text_cut.split("\n")]
finished = False

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

print("\n".join(["".join(line) for line in text_split]).count("X")+1)

# --- PART 2 --- #
# Is this inefficient? YES. In fact, it totally sucks, and took about 2.5 hours to run on my machine. However, it got the right output, so good enough I guess.
text_cut = text.rstrip("\n")
text_split = [list(line) for line in text_cut.split("\n")]
finished = False
start_pos = [(i, j) for i, line in enumerate(text_split) for j, char in enumerate(line) if char == "^"][0]
known_positions = []

while finished == False:
    for enum_line, line in enumerate(text_split):
        for enum_char, char in enumerate(line):
            try:
                if char == "^":
                    known_positions.append((enum_line, enum_char, "^"))
                    if enum_line-1 < 0: # refuse -1 indexing
                        raise ValueError
                    if text_split[enum_line-1][enum_char] != "#":
                        text_split[enum_line][enum_char] = "X"
                        text_split[enum_line-1][enum_char] = "^"
                    else:
                        text_split[enum_line][enum_char] = ">"
                if char == ">":
                    known_positions.append((enum_line, enum_char, ">"))
                    if text_split[enum_line][enum_char+1] != "#":
                        text_split[enum_line][enum_char] = "X"
                        text_split[enum_line][enum_char+1] = ">"
                    else:
                        text_split[enum_line][enum_char] = "v"
                if char == "v":
                    known_positions.append((enum_line, enum_char, "v"))
                    if text_split[enum_line+1][enum_char] != "#":
                        text_split[enum_line][enum_char] = "X"
                        text_split[enum_line+1][enum_char] = "v"
                    else:
                        text_split[enum_line][enum_char] = "<"
                if char == "<":
                    known_positions.append((enum_line, enum_char, "<"))
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
    print(f"Position {enum_pos+1}/{amount_of_x}, som as of now: {som}", end="\r")
    text_split = [list(line) for line in "\n".join(["".join(line) for line in original_text_split]).split("\n")]
    text_split[pos[0]][pos[1]] = "#"
    text_split[start_pos[0]][start_pos[1]] = "."
    finished = False
    for enum_position, postition in enumerate(known_positions):
        pos_x, pos_y, pos_char = postition
        if pos == (pos_x, pos_y):
            new_x, new_y, new_char = known_positions[enum_position-1]
            text_split[new_x][new_y] = new_char
            # print("\n".join(["".join(line) for line in text_split]))
            # exit()
            break
    cur_known_positions = []
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
                            if len(set(cur_known_positions)) != len(cur_known_positions):
                                som += 1
                                raise ValueError
                            
                            text_split[enum_line][enum_char] = "U"
                            text_split[enum_line-1][enum_char] = "^"
                            cur_known_positions.append((enum_line, enum_char, "^"))
                        else:
                            text_split[enum_line][enum_char] = ">"
                    if char == ">":
                        if text_split[enum_line][enum_char+1] == "R":
                            som += 1
                            raise ValueError
                        elif text_split[enum_line][enum_char+1] != "#":
                            if len(set(cur_known_positions)) != len(cur_known_positions):
                                som += 1
                                raise ValueError

                            text_split[enum_line][enum_char] = "R"
                            text_split[enum_line][enum_char+1] = ">"
                            cur_known_positions.append((enum_line, enum_char, ">"))
                        else:
                            text_split[enum_line][enum_char] = "v"
                    if char == "v":
                        if text_split[enum_line+1][enum_char] == "D":
                            som += 1
                            raise ValueError
                        elif text_split[enum_line+1][enum_char] != "#":
                            if len(set(cur_known_positions)) != len(cur_known_positions):
                                som += 1
                                raise ValueError
                            
                            text_split[enum_line][enum_char] = "D"
                            text_split[enum_line+1][enum_char] = "v"
                            cur_known_positions.append((enum_line, enum_char, "v"))
                        else:
                            text_split[enum_line][enum_char] = "<"
                    if char == "<":
                        if enum_char-1 < 0: # refuse -1 indexing
                            raise ValueError
                        if text_split[enum_line][enum_char-1] == "L":
                            som += 1
                            raise ValueError
                        elif text_split[enum_line][enum_char-1] != "#":
                            if len(set(cur_known_positions)) != len(cur_known_positions):
                                som += 1
                                raise ValueError
                            
                            text_split[enum_line][enum_char] = "L"
                            text_split[enum_line][enum_char-1] = "<"
                            cur_known_positions.append((enum_line, enum_char, "<"))
                        else:
                            text_split[enum_line][enum_char] = "^"
                except:
                    finished = True
                    break
print(som)