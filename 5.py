with open("text_files/5.txt", "r") as f:
    text = f.read()
    
# --- PART 1 --- #
text_cut = text.rstrip("\n").split("\n\n")
order_values = [item.split("|") for item in text_cut[0].split("\n")]
test_lines = [item.split(",") for item in text_cut[1].split("\n")]
som = 0

for line in test_lines:
    val = True
    for enum, item in enumerate(line):
        for order_try in order_values:
            if item == order_try[0] and (not (order_try[1] in line[enum+1:])) and order_try[1] in line:
                val = False
            if item == order_try[1] and (not (order_try[0] in line[:enum])) and order_try[0] in line:
                val = False
    
    if val == True:
        som += int(line[len(line) // 2])
    
print(som)

# --- PART 2 --- #
text_cut = text.rstrip("\n").split("\n\n")
order_values = [item.split("|") for item in text_cut[0].split("\n")]
test_lines = [item.split(",") for item in text_cut[1].split("\n")]
incorrect_lines = []
som = 0

def check_line(line):
    val = True
    for enum, item in enumerate(line):
        for order_try in order_values:
            if item == order_try[0] and (not (order_try[1] in line[enum+1:])) and order_try[1] in line:
                val = False
            if item == order_try[1] and (not (order_try[0] in line[:enum])) and order_try[0] in line:
                val = False
    return val

for line in test_lines:
    if check_line(line) == False:
        incorrect_lines.append(line)
        
for line in incorrect_lines:
    while check_line(line) == False:
        for order_try in order_values:
            if order_try[0] in line and order_try[1] in line:
                idx0, idx1 = line.index(order_try[0]), line.index(order_try[1])
                if idx1 < idx0:
                    line[idx0], line[idx1] = line[idx1], line[idx0]
                    
    som += int(line[len(line) // 2])

print(som)
    

