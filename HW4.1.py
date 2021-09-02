import numpy as np
import random
import time
import timeit
import cProfile

def matrix():
    rows = 5
    strings = 4
    a = []
    for i in range(strings):
        b = []
        for j in range(rows):
            b.append(random.randint(-100, 100))
        a.append(b)
    m = np.array(a)
    print(m)
    m = m.T
    print(max(min(m[i]) for i in range(0,rows)))

t1 = time.time()
matrix()
t2 = time.time()
print(f"Способ 1: {t2 - t1}")

t3 = timeit.timeit("matrix()", setup="from __main__ import matrix", number = 10)/10
print(f"Способ 2: {t3}")

def matrix10():
    for i in range(10):
        matrix()

print("Способ 3: ")
cProfile.run('matrix10()')
