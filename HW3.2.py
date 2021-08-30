import random
a = [random.randint(1, 100) for x in range(100)]
b = []
for index, value in enumerate(a):
    if value % 2 == 0:
        b.append(index)
print(a)
print(b)
