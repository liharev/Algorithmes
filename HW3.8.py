a = []
for i in range(4):
    b = []
    for j in range(4):
        b.append(float(input(f"Введите {j} элемент строки {i}: ")))
    b.append(sum((b[k] for k in range(0, 4))))
    a.append(b)
for i in range(4):
    print(a[i])