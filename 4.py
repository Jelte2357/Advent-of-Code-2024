with open("text_files/4.txt", "r") as f:
    text = f.read()
    
# --- PART 1 --- #

text = text.rstrip("\n")
line_length = len(text.split("\n")[0])
som = 0

# Left Right
som += text.count("XMAS")
som += text.count("SAMX")

# Up Down
rotated = "\n".join(["".join(item) for item in list(zip(*text.split("\n")[::-1]))])
som += rotated.count("XMAS")
som += rotated.count("SAMX")

# Shift the text 1 line at a time and rotate it
lshift = "\n".join([i*" "+text.replace("\n", "")[i*line_length:(i+1)*line_length:1] + (line_length-i-1)*" " for i in range(line_length)])
lshift_r = "\n".join(["".join(item) for item in zip(*lshift.split("\n")[::-1])])

som += lshift_r.count("XMAS")
som += lshift_r.count("SAMX")

# do the same but to the right
rshift = "\n".join([(line_length-i-1)*" "+text.replace("\n", "")[i*line_length:(i+1)*line_length:1] + i*" " for i in range(line_length)])
rshift_r = "\n".join(["".join(item) for item in list(zip(*[list(line) for line in rshift.split("\n")][::-1]))])
som += rshift_r.count("XMAS")
som += rshift_r.count("SAMX")

print(som)

# --- PART 2 --- #
text = text.rstrip("\n")
line_length = len(text.split("\n")[0])
som = 0
split_text = text.split("\n")

for enum_line in range(1, len(split_text)-1):
    for enum_char in range(1, line_length-1):
        if text[enum_line*(line_length+1)+enum_char] == "A" and \
        text[enum_line*(line_length+1)+enum_char-line_length-2] != text[enum_line*(line_length+1)+enum_char+line_length+2] and \
        text[enum_line*(line_length+1)+enum_char-line_length-2] in ["M", "S"] and \
        text[enum_line*(line_length+1)+enum_char+line_length+2] in ["M", "S"] and \
        text[enum_line*(line_length+1)+enum_char-line_length] != text[enum_line*(line_length+1)+enum_char+line_length] and \
        text[enum_line*(line_length+1)+enum_char-line_length] in ["M", "S"] and text[enum_line*(line_length+1)+enum_char+line_length] in ["M", "S"]:
            som += 1

print(som)
                    