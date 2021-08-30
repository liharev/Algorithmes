import random
a = [random.randint(-100, 100) for x in range(20)]
print(a)
a.sort()
print(a[0],a[1])
