with open("text_files/2.txt", "r") as f:
    text = f.read()
    
# --- PART 1 --- #
print(sum([not any([abs(x[j] - x[j+1]) > 3 or x[j] == x[j+1] for j in range(len(x)-1)]) if (x:=[int(j) for j in i.split()]) == sorted(x) or x == sorted(x, reverse=True) else 0 for i in text.rstrip("\n").split("\n")]))
            
# --- PART 2 --- #
som = 0
for i in text.rstrip("\n").split("\n"):
    m = [int(k) for k in i.split()]
    if m == sorted(m) or m == sorted(m, reverse=True):
        if all([abs(m[j] - m[j+1]) <= 3 and m[j] != m[j+1] for j in range(len(m)-1)]):
            som += 1
        else:
            for j in range(len(m)):
                n = m[::]
                n.pop(j)
                if all([abs(n[j] - n[j+1]) <= 3 and n[j] != n[j+1] for j in range(len(n)-1)]):
                    som += 1
                    break
    else:
        for j in range(len(m)):
            n = m[::]
            n.pop(j)
            if n == sorted(n) or n == sorted(n, reverse=True):
                if all([abs(n[j] - n[j+1]) <= 3 and n[j] != n[j+1] for j in range(len(n)-1)]):
                    som += 1
                    break
                

print(som)
