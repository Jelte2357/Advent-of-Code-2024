with open("text_files/1.txt", "r") as f:
    text = f.read()
    
# --- PART 1 --- #     
print(sum([abs(int(i) - int(j)) for i, j in zip(sorted([int(i.split()[0]) for i in text.rstrip("\n").split("\n")]), sorted([int(i.split()[1]) for i in text.rstrip("\n").split("\n")]))]))

# --- PART 2 --- #
print(sum([i*[int(i.split()[1]) for i in text.rstrip("\n").split("\n")].count(i) for i in [int(i.split()[0]) for i in text.rstrip("\n").split("\n")]]))