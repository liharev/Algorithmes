a = [x+2 for x in range(97)]
b = [x+2 for x in range(7)]
multiplicity = lambda x, y: 1 if x % y == 0 else 0
count = 0
for i in a:
    for j in b:
        if j > i:
            continue
        count = count + multiplicity(i,j)
print(count)