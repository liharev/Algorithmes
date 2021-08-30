import numpy as np
import random
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
