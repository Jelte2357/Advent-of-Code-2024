with open("text_files/3.txt", "r") as f:
    text = f.read()
    
# --- PART 1 --- #
som = 0
for i in text.rstrip("\n").split("mul("):
    try:
        if all(char in ",1234567890" for char in i[:i.index(")")]):
            som += int((j:=i[:i.index(")")].split(","))[0]) * int(j[1])
    except ValueError:
        pass
    
print(som)

# --- PART 2 --- #
som = 0

for i in text.rstrip("\n").split("do()"):
    try:
        i = i[:i.index("don't()")]
    except ValueError:
        pass
    
    for j in i.split("mul("):
        try:
            if all(char in ",1234567890" for char in j[:j.index(")")]):
                som += int((k:=j[:j.index(")")].split(","))[0]) * int(k[1])
        except ValueError:
            pass
        
print(som)
    