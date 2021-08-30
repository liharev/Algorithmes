import random
a = [random.randint(1, 100) for x in range(1000)]
b = [0 for x in range(max(a))]
for i in a:
    b[i-1] += 1
print(f"Число {b.index(max(b))+1} встречается {max(b)} раз")