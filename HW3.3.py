import random
a = [random.randint(1, 100) for x in range(10)]
minind = a.index(min(a))
maxind = a.index(max(a))
print(a)
a[minind], a[maxind] = a[maxind], a[minind]
print(a)