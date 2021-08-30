import random
a = [random.randint(-100, 100) for x in range(10)]
print(a)
k = -min(a)
for index, value in enumerate(a):
    if value >= 0:
         a[index] = k
    else:
        a[index] = -value
print(f"Максимальный отрицательный элемент {-1*min(a)} находится на {a.index(min(a))+1} месте")
