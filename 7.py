with open("text_files/7.txt", "r") as f:
    text = f.read()

# --- PART 1 --- #
text_strip = text.rstrip("\n")
text_split = text_strip.split("\n")
som = 0
answers_split = [[int(x), [int(a) for a in y.split(" ")]] for x, y in [z.split(": ") for z in text_split]]

for enum, (x, y) in enumerate(answers_split):
    print(f"{enum}/{len(answers_split)}", end="\r")
    for z in range(2**(len(y)-1)):
        equation = y[0]
        for i, op in enumerate(bin(z)[2:].zfill(len(y)-1).replace("0", "+").replace("1", "*")):
            if op == "+":
                equation += y[i+1]
            else:
                equation *= y[i+1]
        if equation == x:
            som += x
            break
    
print(som)

# --- PART 2 --- #
text_strip = text.rstrip("\n")
text_split = text_strip.split("\n")
som = 0
answers_split = [[int(x), [int(a) for a in y.split(" ")]] for x, y in [z.split(": ") for z in text_split]]

def ternary(n): # https://stackoverflow.com/questions/34559663/convert-decimal-to-ternarybase3-in-python
    if n == 0:
        return "0"
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return "".join(reversed(nums))

for enum, (x, y) in enumerate(answers_split):
    print(f"{enum}/{len(answers_split)}", end="\r")
    for z in range(3**(len(y)-1)):
        equation = y[0]
        for i, op in enumerate(ternary(z).zfill(len(y)-1).replace("0", "+").replace("1", "*").replace("2", "|")):
            if op == "+":
                equation += y[i+1]
            elif op == "*":
                equation *= y[i+1]
            else:
                equation = int(str(equation) + str(y[i+1]))
        if equation == x:
            som += x
            break
    
print(som)
