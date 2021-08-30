import random
a = [random.randint(-100, 100) for x in range(20)]
print(a)
minind, maxind = min(a.index(min(a)), a.index(max(a))), max(a.index(min(a)), a.index(max(a)))
print(f"Сумма массива между элементами {minind} и {maxind} равна: {str(sum(a[minind:maxind]) - a[minind])}")

