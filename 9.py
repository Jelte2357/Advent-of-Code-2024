with open("text_files/9.txt") as f:
    text = f.read()
    
# --- PART ONE --- #
text_strip = text.rstrip("\n")
counter = 0

numbers = []
dots = []
for enum_char, char in enumerate(text_strip):
    if enum_char % 2 == 0:
        numbers.append(int(char)*[str(counter)])
        counter += 1
    else:
        dots.append(int(char))

correct_nums = [num for sublist in numbers[::-1] for num in sublist]

final_list = []
for i in range(len(dots)):
    final_list+=numbers[i]
    for j in range(dots[i]):
        final_list.append(correct_nums.pop(0))


final_list = final_list[:len(correct_nums)+sum(dots)]

som = 0
for enum, num in enumerate(final_list):
    som += enum*int(num)

print(som)

# # --- PART TWO --- #
# Teribbly ineficcient, I really don't know how this works, cant really understand my own code tbh (wrote in multiple sittings), takes about 30 seconds to run (on my machine)
text_strip = text.rstrip("\n")
counter = 0

numbers = []
dots = []
for enum_char, char in enumerate(text_strip):
    if enum_char % 2 == 0:
        numbers.append(int(char)*[str(counter)])
        counter += 1
    else:
        dots.append(int(char))
dots += [0]
rev_numbers = numbers[::-1]

zipped = [item for sublist in list(zip(numbers, dots)) for item in sublist if item != 0]

for enum_z, z in enumerate(rev_numbers):
    current_index = zipped.index(z)
    for enum_r, r in enumerate(zipped):
        if enum_r < current_index:
            if isinstance(r, int):
                if len(z)<=r:
                    zipped.insert(enum_r, z)
                    try:
                        zipped[enum_r+1] -= len(z)
                    except:
                        zipped.append(len(z))
                    break

known_items = []      
for enum, item in enumerate(zipped):
    if isinstance(item, int):
        continue
    if item not in known_items:
        known_items.append(item)
    else:
        zipped.insert(enum, len(zipped.pop(enum)))

unzipped = [str(i) for x in zipped for i in (x if isinstance(x, list) else ["0"] * x)]

som = 0
for enum, num in enumerate(unzipped):
    som += enum*int(num)

print(som)